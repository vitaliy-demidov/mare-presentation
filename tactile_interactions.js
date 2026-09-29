/**
 * ============================================================================
 * MUAR A · TACTILE INTERACTIONS & TRANSITIONS ENGINE
 * ============================================================================
 * Design Inspiration: Anthony Lawrence-Belfair (Bespoke Upholstery & Workroom),
 * Apple HIG Liquid Glass & High-End Editorial Luxury Architecture.
 *
 * Modules:
 * 1. TactileSoundEngine (Web Audio API micro-acoustics & ambient synth)
 * 2. TactileBeforeAfterSlider (Draggable handle with multi-touch & pointer events)
 * 3. TactileMonographDrawer (Full editorial slide-out & fullscreen modal)
 * 4. TactileVoicePlayer (Atelier voice memos with real-time waveform visualizer)
 * 5. TactileCategoryFilter (5 luxury categories with sliding gold indicator)
 * ============================================================================
 */

(function (window, document) {
  'use strict';

  // Master Namespace
  const Tactile = (window.TactileInteractions = window.MuarTactile = {});

  /* ==========================================================================
     DATA ARCHIVE: 10 CANONICAL MUAR A PROJECTS
     ========================================================================== */
  const MUAR_ARCHIVE_DATA = [
    {
      id: 1,
      num: "01",
      cat: "penthouses",
      cat_name: "Частная Резиденция",
      badge: "Couture Red & White",
      title: "Драматургия Red & White: Бескомпромиссный шик",
      collaborator: "Авторский текстильный сценарий Muar A",
      location: "Астана · Частная резиденция",
      quote: "Сочетание красного и белого — это как драматургия, застывшая в пространстве. Задачу заказчики поставили категоричную: красные шторы. Мы убедили их усилить арт-объект вставкой с птицами и разгуляться в подушках.",
      quote_author: "Асенгуль · Основатель текстильного дома Muar A",
      story: "В спальне уже присутствовала насыщенная красная стеновая панель. Добавить просто однотонные красные шторы означало бы перегрузить интерьер и лишить его глубины. Команда Muar A предложила кутюрное решение: портьеры со сложной вставкой с птицами, поддержанные чистым белым кантом. В гостиной центральный арт-объект был деликатно обрамлен струящимися портьерами на плотной подкладке, а динамичный красный цвет раскрылся в фактурных подушках со съемными чехлами и стёганом покрывале.",
      specs: [
        "Портьеры на светозащитной подкладке Dimout (Италия)",
        "Кутюрная вставка с вышивкой птиц ручной работы",
        "Стёганое покрывало на формообразующем синтепоне",
        "Комплект декоративных подушек со съёмными чехлами",
        "Французская тройная складка с ручной фиксацией"
      ],
      has_ba: true,
      ba_before: "assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp",
      ba_after: "assets/muar/portfolio/garden-14.webp",
      ba_label_before: "Интерьер до текстиля",
      ba_label_after: "Драматургия Red & White",
      photos: [
        { src: "assets/muar/portfolio/garden-14.webp", alt: "Red & White Гостиная и портьеры" },
        { src: "assets/muar/portfolio/garden-18.webp", alt: "Вставка с птицами в спальне" },
        { src: "assets/muar/portfolio/garden-30.webp", alt: "Фактура штор и подушек" },
        { src: "assets/muar/portfolio/garden-31.webp", alt: "Детали стёганого покрывала" },
        { src: "assets/muar/portfolio/garden-32.webp", alt: "Драпировка в гостиной" },
        { src: "assets/muar/portfolio/garden-33.webp", alt: "Общий вид интерьера" },
        { src: "assets/muar/portfolio/garden-08.webp", alt: "Светотеневой рисунок складок" },
        { src: "assets/muar/portfolio/garden_darker-1.webp", alt: "Вечерний сценарий освещения" },
        { src: "assets/muar/portfolio/garden_darker-2.webp", alt: "Фрагмент ткани под софитами" }
      ],
      voice_note: {
        track: "audio_18@28-09-2026_07-56-23.ogg",
        title: "Концепция кинематографичности и характер интерьера",
        duration: "00:48",
        transcript: "«Доброе утро! Мы вдохновлялись атмосферой кинематографичной эстетики. Контраст красного и белого требует предельной смелости, где текстиль становится главным драматургическим нервом помещения»."
      }
    },
    {
      id: 2,
      num: "02",
      cat: "penthouses",
      cat_name: "ЖК Vivaldi (Пентхаус)",
      badge: "Панорамный Dimout & Somfy",
      title: "Панорамные окна в ЖК Vivaldi: Свет и Dimout",
      collaborator: "Совместно с дизайн-студией IDesign",
      location: "Астана · ЖК Vivaldi",
      quote: "Квартира очень светлая, с огромными витражами на солнечную сторону. Мы установили электрокарнизы Somfy и сшили портьеры на подкладке Dimout — свет мягко рассеивается, а ткани надежно защищены от выгорания.",
      quote_author: "Дизайн-студия IDesign & Асенгуль",
      story: "Проект реализован в одном из самых знаковых жилых комплексов Астаны. Высокая инсоляция требовала ювелирного баланса между сохранением вида на город и защитой приватности. Была смонтирована скрытая двухрядная моторизованная трасса. Римские шторы в спальне скомбинированы с тяжелыми портьерами. Кант из натуральной кожи на декоративных подушках подчеркивает архитектурный модернизм помещения.",
      specs: [
        "Бесшумные электрокарнизы Somfy с радиоуправлением",
        "Подкладка Dimout с защитой от ультрафиолета 85%",
        "Римские шторы со скрытыми фиберглассовыми вставками",
        "Подушки с черным графитовым кантом и вставками из кожи",
        "Специальная подкладочная ткань покрывала от деформации"
      ],
      has_ba: true,
      ba_before: "assets/muar/living-luxe-before.webp",
      ba_after: "assets/muar/portfolio/1.webp",
      ba_label_before: "Слепящее солнце витражей",
      ba_label_after: "Рассеянный свет Dimout",
      photos: [
        { src: "assets/muar/portfolio/1.webp", alt: "ЖК Vivaldi Панорамная гостиная" },
        { src: "assets/muar/portfolio/1-21.webp", alt: "Римская штора и портьеры" },
        { src: "assets/muar/portfolio/1-13.webp", alt: "Детали подушек с кожаным кантом" },
        { src: "assets/muar/portfolio/1-42.webp", alt: "Светозащитные портьеры в спальне" },
        { src: "assets/muar/portfolio/1-50.webp", alt: "Драпировка витражного окна" },
        { src: "assets/muar/portfolio/1-69.webp", alt: "Электрокарниз в нише" },
        { src: "assets/muar/portfolio/1-84.webp", alt: "Фактура бельгийского шенилла" },
        { src: "assets/muar/portfolio/1-87.webp", alt: "Шелковое покрывало ручной сборки" },
        { src: "assets/muar/portfolio/1-107.webp", alt: "Общий вид мастер-сьюта" }
      ],
      voice_note: {
        track: "audio_19@28-09-2026_07-56-35.ogg",
        title: "О подборе колористики: сизый, графит и золото",
        duration: "00:42",
        transcript: "«Мне здесь невероятно нравятся цвета: сизый, благородный пурпурный, графит и легкие вкрапления приглушенного золота. Они собирают весь витраж в единый монолит»."
      }
    },
    {
      id: 3,
      num: "03",
      cat: "villa",
      cat_name: "Загородная Резиденция",
      badge: "Couture Pasementerie",
      title: "Текстильный размах в загородном доме",
      collaborator: "Дизайнер Зарина Секен & декораторы Muar A",
      location: "Астана · Загородный особняк",
      quote: "Этот проект стал настоящей радостью. Мы поддержали смелые колористические решения Зарины Секен: изысканные басонные канты, прозрачный римский тюль и абсолютно неповторимые формы валиков.",
      quote_author: "Зарина Секен & Muar A",
      story: "Масштабный загородный дом потребовал индивидуального проектирования каждого текстильного узла. Вместо традиционного нагромождения тяжелого тюля был применен лаконичный римский прозрачный тюль, пропускающий мягкий дневной свет степного горизонта. Все портьеры декорированы филигранными басонными кантами европейского плетения.",
      specs: [
        "Басонные декоративные канты ручного плетения (Франция)",
        "Прозрачный бескаркасный римский тюль мягкого свиса",
        "Авторские формы цилиндрических валиков с кистями",
        "Текстильное оформление резиденции «под ключ»",
        "Коэффициент сборки портьер 1:2.6"
      ],
      has_ba: true,
      ba_before: "assets/muar/portfolio/_MG_9217-2.webp",
      ba_after: "assets/muar/portfolio/kzlst-13.webp",
      ba_label_before: "Пустой черновой витраж",
      ba_label_after: "Римский тюль & Басонный кант",
      photos: [
        { src: "assets/muar/portfolio/kzlst-13.webp", alt: "Текстильный размах загородного дома" },
        { src: "assets/muar/portfolio/_MG_9140-2.webp", alt: "Римский прозрачный тюль и декор" },
        { src: "assets/muar/portfolio/kzlst-07.webp", alt: "Басонные канты портьеры" },
        { src: "assets/muar/portfolio/kzlst-08.webp", alt: "Валики и подушки на заказ" },
        { src: "assets/muar/portfolio/_MG_9217-2.webp", alt: "Вид на гостиную с камином" }
      ],
      voice_note: {
        track: "audio_20@28-09-2026_15-03-32.ogg",
        title: "Прозрачность расчетов и точность кроя для резиденций",
        duration: "00:54",
        transcript: "«Я всегда делаю расчеты предельно наглядно: метраж, коэффициенты сборки, стоимость погонного метра. Клиент видит каждый сантиметр полотна и точно знает, за что платит»."
      }
    },
    {
      id: 4,
      num: "04",
      cat: "penthouses",
      cat_name: "Executive Office (B2B)",
      badge: "Сатин & Дамаск · ГОСТ",
      title: "Современный кабинет руководителя: Сатин & Дамаск",
      collaborator: "Офис первого лица · Контрактный текстиль",
      location: "Астана · Деловой центр",
      quote: "Классическая палитра в комбинации с матовой текстурой сатина и рифленым орнаментом «дамаск» придает пространству статусность без архаичности. Шторы управляются голосом и с пульта.",
      quote_author: "Асенгуль · Технический регламент B2B",
      story: "Кабинет первых лиц требует строгого акустического комфорта, огнестойкости материалов и прецизионной солнцезащиты. В проекте использован матовый сатин европейского производства, дополненный рифленым орнаментом дамаск. Электрокарнизы интегрированы в систему умного дома с возможностью голосового управления.",
      specs: [
        "Негорючие ткани стандарта Trevira CS (Германия)",
        "Акустическое поглощение шума реверберации до 40%",
        "Электрокарнизы с интеграцией в Умный Дом и голосовые ассистенты",
        "Ручная бантовая складка с сохранением рисунка дамаска",
        "Полный пакет закрывающих документов, ЭДО и НДС 12%"
      ],
      has_ba: false,
      photos: [
        { src: "assets/muar/portfolio/garden-33.webp", alt: "Кабинет руководителя общий вид" },
        { src: "assets/muar/portfolio/garden-30.webp", alt: "Сочетание сатина и орнамента дамаск" },
        { src: "assets/muar/portfolio/garden-31.webp", alt: "Интеграция электрокарниза в нишу" },
        { src: "assets/muar/portfolio/garden-32.webp", alt: "Идеальная вертикаль драпировки" }
      ],
      voice_note: {
        track: "audio_23@28-09-2026_16-06-43.ogg",
        title: "Статус кабинета руководителя и B2B спецификации",
        duration: "01:05",
        transcript: "«Для кабинета руководителя принципиально важно совместить представительский лоск и строгую акустику. Текстиль должен глушить эхо при переговорах и двигаться бесшумно»."
      }
    },
    {
      id: 5,
      num: "05",
      cat: "contract",
      cat_name: "Ресторан / Контракт",
      badge: "Потолочные Паруса 4м+",
      title: "Потолочные паруса и навесы в ресторане",
      collaborator: "Дизайнер Руслан & декораторы Muar A",
      location: "Астана · Премиальный ресторан",
      quote: "Монтаж карнизов более 4 метров и ювелирный расчет свиса ткани. Здесь ткань словно дышит и улавливает каждое движение воздуха, создавая живую завораживающую асимметрию.",
      quote_author: "Дизайнер Руслан & Muar A",
      story: "Один из сложнейших инженерных кейсов в портфолио студии. Пространство ресторана с высокими открытыми сводами требовало мягкого зонирования и снижения гулкости. Были спроектированы нестандартные потолочные направляющие из анодированного черного алюминия. Ткань рассчитана с учетом естественного гравитационного растяжения нитей, образовав невесомые паруса.",
      specs: [
        "Непрерывные направляющие профили длиной свыше 4.2 метра",
        "Математический расчет стрелы провисания с погрешностью 2 мм",
        "Пожаробезопасная дышащая вуаль с сертификатом ЕАЭС",
        "Снижение уровня шума в зале на 6.5 дБ",
        "Быстросъемный монтаж для регулярной химчистки"
      ],
      has_ba: false,
      photos: [
        { src: "assets/muar/portfolio/IMG_6711.webp", alt: "Потолочные текстильные паруса" },
        { src: "assets/muar/portfolio/IMG_6710.webp", alt: "Мягкий свис и пластика полотен" },
        { src: "assets/muar/portfolio/IMG_6709.webp", alt: "Атмосфера света и воздуха в ресторане" }
      ],
      voice_note: {
        track: "audio_22@28-09-2026_15-27-41.ogg",
        title: "Облегчение конструкции и свобода пространства",
        duration: "00:46",
        transcript: "«Мы убрали все лишнее, облегчили драпировку, дали воздуху циркулировать. Когда гости входят в зал, паруса создают ощущение морского бриза»."
      }
    },
    {
      id: 6,
      num: "06",
      cat: "villa",
      cat_name: "Загородный Дом (Модерн 60-х)",
      badge: "Ручная роспись & Мулине",
      title: "Крафтовое изделие в загородном доме: Модерн 60-х",
      collaborator: "Дизайнер интерьера Динара Усманова",
      location: "Астана · Загородный дом",
      quote: "Когда фабрика в Турции сняла нужную ткань с производства, наш декоратор предложила вручную расписать геометрический орнамент и дополнить его нитями мулине. Получился истинный кутюр.",
      quote_author: "Динара Усманова & Muar A",
      story: "Форс-мажор на фабрике превратился в рождение музейного артефакта. В строгом интерьере стиля модернизма 60-х годов требовалась безупречная геометрия. Мастера студии вручную нанесли сложный графичный узор специальными пигментами для текстиля, закрепили его термофиксацией и выполнили акцентную прошивку нитями шелкового мулине. Граница между тюлем и портьерой подчеркнута контрастным кантом.",
      specs: [
        "100% ручная авторская роспись геометрического раппорта",
        "Вышивка нитями шелкового мулине по границе рисунка",
        "Текстильный соединительный кант ручной работы",
        "Льняная основа с предварительной усадкой паром (декатировкой)",
        "Единственный экземпляр в мире без возможности тиражирования"
      ],
      has_ba: false,
      photos: [
        { src: "assets/muar/portfolio/IMG_6717.webp", alt: "Крафтовое изделие в интерьере" },
        { src: "assets/muar/portfolio/IMG_6712.webp", alt: "Ручная роспись геометрического орнамента" },
        { src: "assets/muar/portfolio/IMG_6713.webp", alt: "Нити мулине и соединительный кант" },
        { src: "assets/muar/portfolio/IMG_6714.webp", alt: "Фактура льняного полотна" },
        { src: "assets/muar/portfolio/IMG_6715.webp", alt: "Драпировка в пол в стиле модерн" },
        { src: "assets/muar/portfolio/IMG_6716.webp", alt: "Фрагмент текстильного оформления спальни" }
      ],
      voice_note: {
        track: "audio_18@28-09-2026_07-56-23.ogg",
        title: "Крафтовое текстильное искусство вместо шаблонов",
        duration: "00:50",
        transcript: "«Для простых решений много ума не надо. А вот когда ткань снимают с производства — создать ручной шедевр и сделать лучше фабрики — в этом и есть сила нашего ателье»."
      }
    },
    {
      id: 7,
      num: "07",
      cat: "villa",
      cat_name: "High-Ceiling Вилла (10 метров)",
      badge: "Лифт-системы 10м · Спецпроект",
      title: "Виллы «Темный Рыцарь»: 10-метровые потолки и лифт-системы",
      collaborator: "Архитектор проекта Габиден & Muar A",
      location: "Астана · Закрытый коттеджный городок",
      quote: "Высота потолков в холле — 10 метров. Здесь критически важно рассчитать силовые кабели, трубчатые моторы, стальные тросы и вес ткани с подкладкой. Это высшая лига текстильной инженерии.",
      quote_author: "Архитектор Габиден & Асенгуль",
      story: "Виллы в стилистике фильма Кристофера Нолана «Темный Рыцарь» с монументальной архитектурой и окнами высотой 10 метров. Ни одна стандартная шторная система не способна функционировать при таких нагрузках: масса полотна превышает 80 кг. Инженерная группа Muar A спроектировала промышленную подъемную лифт-систему на стальных авиационных тросах с защитой от перекоса. Ткань — плотный высококлассный сатин, сохраняющий геометрию фалд.",
      specs: [
        "Специализированная моторизованная лифт-система для высоты 10 м",
        "Трубчатые приводы промышленного класса с крутящим моментом 120 Нм",
        "Несущие тросы из нержавеющей стали с запасом прочности 5x",
        "Тяжелый сатин на защитной подкладке (общий вес полотен ~85 кг)",
        "Сервисное опускание карниза на уровень пола для чистки"
      ],
      has_ba: true,
      ba_before: "assets/muar/portfolio/IMG_4198.webp",
      ba_after: "assets/muar/portfolio/IMG_6721.webp",
      ba_label_before: "Черновой холл 10 метров (Фото #4198)",
      ba_label_after: "Лифт-система «Темный Рыцарь»",
      photos: [
        { src: "assets/muar/portfolio/IMG_6721.webp", alt: "Вилла Темный Рыцарь титульный вид" },
        { src: "assets/muar/portfolio/IMG_6718.webp", alt: "10-метровые портьеры на лифт-системе" },
        { src: "assets/muar/portfolio/IMG_6719.webp", alt: "Вид из галереи второго света" },
        { src: "assets/muar/portfolio/IMG_6720.webp", alt: "Фалды плотного сатина в пол" },
        { src: "assets/muar/portfolio/IMG_6722.webp", alt: "Панорама холла с камином" },
        { src: "assets/muar/portfolio/IMG_6723.webp", alt: "Инженерный узел опускания карниза" },
        { src: "assets/muar/portfolio/IMG_6724.webp", alt: "Текстиль в спальне с потолками 5м" },
        { src: "assets/muar/portfolio/IMG_4198.webp", alt: "Исходное состояние холла во время замеров" },
        { src: "assets/muar/portfolio/1-119.webp", alt: "Фрагмент моторизованного управления" }
      ],
      voice_note: {
        track: "audio_20@28-09-2026_15-03-32.ogg",
        title: "Инженерия 10-метровых витражей и моторы",
        duration: "01:15",
        transcript: "«Когда высота 10 метров — ошибки недопустимы. Мы заранее закладываем проводку, согласуем фазы моторов со строителями и проверяем каждый трос. Это безопасность всей семьи»."
      }
    },
    {
      id: 8,
      num: "08",
      cat: "bedroom",
      cat_name: "Мастер-Спальня",
      badge: "Бордо & Подхват-Роза",
      title: "Авторский текстиль для яркой спальни: Бордо & Пайетки",
      collaborator: "Дизайнер Лаура Жакина & Muar A",
      location: "Астана · Апартаменты",
      quote: "Насыщенный бордовый цвет стены задал тон. Мы отказались от нейтральных решений: портьеры с декором обрамлены подхватом-розой в тон настенного барельефа, а в изножье покрывала сверкают пайетки.",
      quote_author: "Дизайнер Лаура Жакина & Muar A",
      story: "В спальне смелое колористическое решение: стена цвета спелой вишни и объемный гипсовый барельеф. Чтобы связать текстиль с архитектурой, мастера студии вручную изготовили скульптурный подхват в виде розы. Стеганое покрывало дополнено изножьем с ненавязчивыми матовыми микропайетками, а в зоне окна струится фиолетовая кисея, дарящая спальне камерное свечение.",
      specs: [
        "Скульптурный подхват-роза ручного изготовления из ткани портьер",
        "Стёганое покрывало с изножьем из ткани с микропайетками",
        "Трёхслойные декоративные подушки (союз хлопка, шерсти и сатина)",
        "Струящаяся фиолетовая кисея с утяжелителем",
        "Индивидуальный колористический подбор под барельеф стены"
      ],
      has_ba: false,
      photos: [
        { src: "assets/muar/portfolio/IMG_6726.webp", alt: "Яркая спальня в бордовых тонах" },
        { src: "assets/muar/portfolio/IMG_6725.webp", alt: "Подхват-роза и портьеры" },
        { src: "assets/muar/portfolio/IMG_6727.webp", alt: "Покрывало с расшитым изножьем" },
        { src: "assets/muar/portfolio/IMG_6728.webp", alt: "Фиолетовая кисея в зоне отдыха" },
        { src: "assets/muar/portfolio/IMG_6729.webp", alt: "Детали басонного декора" }
      ],
      voice_note: {
        track: "audio_19@28-09-2026_07-56-35.ogg",
        title: "Глубокие баклажановые тона и тактильность",
        duration: "00:39",
        transcript: "«Бордовый цвет капризен: чуть промахнешься с полутоном — и комната станет тяжелой. Мы взяли матовую шерсть с шелком, добавили розу, и спальня задышала будуарным уютом»."
      }
    },
    {
      id: 9,
      num: "09",
      cat: "bedroom",
      cat_name: "Мастер-Спальня",
      badge: "Коррекция асимметрии",
      title: "Мастер-спальня с асимметричным окном: Римская штора & Тюль омбре",
      collaborator: "Авторский текстильный сценарий Muar A",
      location: "Астана · Частная резиденция",
      quote: "В спальне было асимметричное окно, а шоколадные шторы с одной стороны подчеркивали дефект. Мы заменили их на легкую римскую штору и тюль с бирюзовым градиентом омбре. Пространство преобразилось.",
      quote_author: "Асенгуль · Основатель текстильного дома Muar A",
      story: "Классический пример исправления грубых архитектурных ошибок застройщика текстильными методами. Окно располагалось вплотную к смежной стене. Обычные портьеры перекашивали комнату. Специалисты Muar A смонтировали компактную римскую штору и пустили по карнизу невесомый льняной тюль с деликатным переходом омбре от бирюзы к айвори. Бирюза перекликается с сиреневым изголовьем кровати, а раннер объединил весь ансамбль.",
      specs: [
        "Коррекция визуальной асимметрии простенка с помощью римского механизма",
        "Льняной французский тюль с фабричным градиентным крашением омбре",
        "Текстильный раннер в изножье кровати из итальянского жаккарда",
        "Комплект подушек с натуральной растительной вышивкой",
        "Отказ от тяжелых темных тканей в пользу оптического простора"
      ],
      has_ba: true,
      ba_before: "assets/muar/portfolio/project_09_before.webp",
      ba_after: "assets/muar/portfolio/project_09_after.webp",
      ba_label_before: "Дефект асимметрии окна (До)",
      ba_label_after: "Римская штора & Тюль омбре",
      photos: [
        { src: "assets/muar/portfolio/project_09_after.webp", alt: "Мастер-спальня после преображения (Римская штора и омбре)" },
        { src: "assets/muar/portfolio/project_09_before.webp", alt: "Исходное окно с дефектом асимметрии (До)" },
        { src: "assets/muar/portfolio/project_09_ombre.webp", alt: "Фрагмент льняного тюля омбре" },
        { src: "assets/muar/portfolio/asem_br-29.webp", alt: "Раннер и декор кровати" },
        { src: "assets/muar/portfolio/IMG_8482.webp", alt: "Детализация вышивки на подушках" }
      ],
      voice_note: {
        track: "audio_21@28-09-2026_15-15-46.ogg",
        title: "Почему нельзя вешать одну штору при асимметрии",
        duration: "00:52",
        transcript: "«Когда окно смещено к углу, вешать одну портьеру — грубейшая ошибка. Мы подняли свет вверх, сделали римскую штору, а тюль омбре визуально выровнял геометрию стен»."
      }
    },
    {
      id: 10,
      num: "10",
      cat: "bedroom",
      cat_name: "Спальня & Декор Кровати",
      badge: "Кроватные сеты · ЕАЭС",
      title: "Спальня как простор для технических и дизайнерских решений",
      collaborator: "Текстильный цех Muar A · Декларации ЕАЭС",
      location: "Астана · Жилой комплекс",
      quote: "Кровать — композиционный центр спальни. Без ее оформления комната незавершена. Мы создаем гармонирующие комплекты: покрывала, раннеры, подушки и валики со строгим соблюдением стандартов ЕАЭС.",
      quote_author: "Асенгуль · Регламент пошива Muar A",
      story: "В спальне важна тактильная безупречность: ткани соприкасаются с кожей ежедневно. В собственном швейном цехе Muar A без привлечения надомниц изготавливаются многослойные покрывала с ручной стёжкой, валики с декоративными помпонами и шторы на электрокарнизах. Вся продукция сертифицирована согласно техническим регламентам Таможенного союза.",
      specs: [
        "Официальная декларация соответствия ЕАЭС на швейную продукцию",
        "Трёхслойное стёганое покрывало с гипоаллергенным наполнителем",
        "Декоративные валики с отделкой помпонами ручной сборки",
        "Электрокарнизы с таймерами пробуждения по восходу солнца",
        "Потайные молнии YKK и усиленные краевые закрепки швов"
      ],
      has_ba: false,
      photos: [
        { src: "assets/muar/portfolio/project_10_title.webp", alt: "Титульное оформление спальни и кровати" },
        { src: "assets/muar/portfolio/IMG_3952.webp", alt: "Декор кровати: покрывала и подушки" },
        { src: "assets/muar/portfolio/IMG_3961.webp", alt: "Валики с помпонами ручной работы" },
        { src: "assets/muar/portfolio/IMG_3962.webp", alt: "Фактурное плетение жаккарда" },
        { src: "assets/muar/portfolio/project_10_pompom.webp", alt: "Макро-снимок декоративного канта" },
        { src: "assets/muar/portfolio/atlant-31.webp", alt: "Проект в ЖК Атлант" },
        { src: "assets/muar/portfolio/evolution-17.webp", alt: "Оформление детской спальни" },
        { src: "assets/muar/portfolio/IMG_9796.webp", alt: "Портьеры блэкаут для сна" },
        { src: "assets/muar/portfolio/IMG_9827.webp", alt: "Покрывало с шелковым кантом" },
        { src: "assets/muar/portfolio/IMG_9861.webp", alt: "Общий вид мастер-спальни" }
      ],
      voice_note: {
        track: "audio_20@28-09-2026_15-03-32.ogg",
        title: "Цеховые стандарты пошива и сертификаты качества",
        duration: "00:58",
        transcript: "«Мы принципиально не отдаем заказы швеям-надомницам. В нашем цехе стоят промышленные парогенераторы, закрепочные машины и строгий ОТК. Только так шторы висят идеально годами»."
      }
    }
  ];

  /* Voice Notes Archive */
  const VOICE_MEMOS = [
    {
      id: "voice-01",
      track: "assets/muar/voice/audio_19@28-09-2026_07-56-35.ogg",
      title: "Заметка 01: О цвете и фактурах — сизый, графит, золото",
      author: "Асенгуль · Основатель Muar A",
      duration: "00:42",
      durationSec: 42,
      transcript: "«Мне здесь невероятно нравятся цвета: сизый, благородный пурпурный, графитовый и легкие вкрапления приглушенного золота. Они собирают весь витраж в единый монолит без визуальной перегрузки»."
    },
    {
      id: "voice-02",
      track: "assets/muar/voice/audio_20@28-09-2026_15-03-32.ogg",
      title: "Заметка 02: Прозрачные расчеты и сметы для юрлиц и физлиц",
      author: "Асенгуль · Основатель Muar A",
      duration: "00:54",
      durationSec: 54,
      transcript: "«Виталий, добрый день! Я сделала расчеты предельно наглядно: в экселе красным выделено для юрлиц, обычным для физлиц. Можно нажать на ячейку и сразу видна формула расхода ткани и работы цеха»."
    },
    {
      id: "voice-03",
      track: "assets/muar/voice/audio_22@28-09-2026_15-27-41.ogg",
      title: "Заметка 03: Облегчение стиля и эстетика кабинетов",
      author: "Асенгуль · Основатель Muar A",
      duration: "00:46",
      durationSec: 46,
      transcript: "«Мы убрали все лишнее, облегчили конструкцию. Сейчас намного легче стало читаться, меньше визуального шума. Текстиль должен дышать и подчеркивать пространство, а не спорить с ним»."
    },
    {
      id: "voice-04",
      track: "assets/muar/voice/audio_18@28-09-2026_07-56-23.ogg",
      title: "Заметка 04: Концепция кинематографичности и характер бренда",
      author: "Асенгуль · Основатель Muar A",
      duration: "00:48",
      durationSec: 48,
      transcript: "«Доброе утро! Мы делаем не просто шторы, мы создаем кинематографичную эстетику пространства. Смелые сочетания фактур, благородный свет и драматургия формы»."
    },
    {
      id: "voice-05",
      track: "assets/muar/voice/audio_23@28-09-2026_16-06-43.ogg",
      title: "Заметка 05: Текстиль для B2B и представительский кабинет",
      author: "Асенгуль · Основатель Muar A",
      duration: "01:05",
      durationSec: 65,
      transcript: "«Для кабинета первого лица принципиально важна статусность без архаичности. Мы добавили рифленый дамаск с матовым сатином и электрокарнизы — это создает идеальный баланс комфорта и авторитета»."
    },
    {
      id: "voice-06",
      track: "assets/muar/voice/audio_21@28-09-2026_15-15-46.ogg",
      title: "Заметка 06: Коррекция дефектов асимметрии и геометрии",
      author: "Асенгуль · Основатель Muar A",
      duration: "00:52",
      durationSec: 52,
      transcript: "«Когда окно смещено к углу, вешать одну портьеру — грубейшая ошибка. Мы подняли свет вверх, сделали римскую штору, а тюль омбре визуально выровнял геометрию помещения»."
    }
  ];

  /* ==========================================================================
     1. TACTILE SOUND ENGINE (Web Audio API)
     ========================================================================== */
  class TactileSoundEngine {
    constructor() {
      this.ctx = null;
      this.isMuted = false;
      this.synthGain = null;
      this.lastTransient = 0;
    }

    getContext() {
      if (!this.ctx) {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (AudioCtx) {
          this.ctx = new AudioCtx();
        }
      }
      if (this.ctx && this.ctx.state === 'suspended') {
        this.ctx.resume().catch(() => {});
      }
      return this.ctx;
    }

    play(soundType = 'brass-click') {
      if (this.isMuted) return;
      const ctx = this.getContext();
      if (!ctx) return;

      const now = ctx.currentTime;
      if (now - this.lastTransient < 0.04) return; // Debounce transients
      this.lastTransient = now;

      switch (soundType) {
        case 'brass-click': {
          // Sharp metallic tactile feedback
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          const filter = ctx.createBiquadFilter();

          osc.type = 'triangle';
          osc.frequency.setValueAtTime(1450, now);
          osc.frequency.exponentialRampToValueAtTime(320, now + 0.035);

          filter.type = 'bandpass';
          filter.frequency.setValueAtTime(2200, now);
          filter.Q.setValueAtTime(4.0, now);

          gain.gain.setValueAtTime(0.09, now);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.035);

          osc.connect(filter);
          filter.connect(gain);
          gain.connect(ctx.destination);

          osc.start(now);
          osc.stop(now + 0.04);
          break;
        }

        case 'silk-drag': {
          // Micro whisper of silk friction
          const bufferSize = ctx.sampleRate * 0.03;
          const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
          const data = buffer.getChannelData(0);
          for (let i = 0; i < bufferSize; i++) {
            data[i] = (Math.random() * 2 - 1) * 0.05;
          }

          const noise = ctx.createBufferSource();
          noise.buffer = buffer;

          const filter = ctx.createBiquadFilter();
          filter.type = 'highpass';
          filter.frequency.setValueAtTime(3600, now);

          const gain = ctx.createGain();
          gain.gain.setValueAtTime(0.035, now);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.03);

          noise.connect(filter);
          filter.connect(gain);
          gain.connect(ctx.destination);

          noise.start(now);
          break;
        }

        case 'monograph-open': {
          // Resonant warm luxury chime
          const freqs = [330, 495, 660];
          freqs.forEach((f, idx) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(f, now + idx * 0.03);

            gain.gain.setValueAtTime(0.045 / (idx + 1), now + idx * 0.03);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.45 + idx * 0.05);

            osc.connect(gain);
            gain.connect(ctx.destination);

            osc.start(now + idx * 0.03);
            osc.stop(now + 0.6);
          });
          break;
        }

        case 'monograph-close': {
          // Soft descending dismiss
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(420, now);
          osc.frequency.exponentialRampToValueAtTime(180, now + 0.22);

          gain.gain.setValueAtTime(0.04, now);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.22);

          osc.connect(gain);
          gain.connect(ctx.destination);

          osc.start(now);
          osc.stop(now + 0.25);
          break;
        }
      }
    }
  }

  Tactile.sound = new TactileSoundEngine();

  /* ==========================================================================
     2. BEFORE / AFTER SPLIT SLIDER COMPONENT
     ========================================================================== */
  class TactileBeforeAfterSlider {
    constructor(container, options = {}) {
      if (typeof container === 'string') {
        container = document.querySelector(container);
      }
      if (!container) return;

      this.container = container;
      this.options = Object.assign(
        {
          initialPosition: 50,
          labelBefore: "Интерьер до текстиля",
          labelAfter: "Кутюрное преображение MUAR A",
          onPositionChange: null
        },
        options
      );

      this.currentPct = this.options.initialPosition;
      this.isDragging = false;
      this.startX = 0;
      this.startPct = 50;

      this.setupDOM();
      this.bindEvents();
      this.setPercentage(this.currentPct, false);
    }

    setupDOM() {
      this.container.classList.add('tactile-ba-container');
      this.container.setAttribute('role', 'slider');
      this.container.setAttribute('tabindex', '0');
      this.container.setAttribute('aria-label', 'Интерактивное сравнение До и После');
      this.container.setAttribute('aria-valuemin', '0');
      this.container.setAttribute('aria-valuemax', '100');
      this.container.setAttribute('aria-valuenow', this.currentPct);

      // Locate or create layers
      this.beforeLayer = this.container.querySelector('.tactile-ba-before, .ba-before-layer, .muar-ba-before');
      this.afterLayer = this.container.querySelector('.tactile-ba-after, .ba-after-layer, .muar-ba-after');
      this.divider = this.container.querySelector('.tactile-ba-divider, .ba-handle-line, .muar-ba-divider');

      if (this.beforeLayer) this.beforeLayer.classList.add('tactile-ba-layer', 'tactile-ba-before');
      if (this.afterLayer) this.afterLayer.classList.add('tactile-ba-layer', 'tactile-ba-after');

      // Create divider and handle grip if missing
      if (!this.divider) {
        this.divider = document.createElement('div');
        this.divider.className = 'tactile-ba-divider';
        this.container.appendChild(this.divider);
      } else {
        this.divider.classList.add('tactile-ba-divider');
      }

      let grip = this.divider.querySelector('.tactile-ba-handle-grip, .ba-handle-grip, .muar-ba-grip');
      if (!grip) {
        grip = document.createElement('div');
        grip.className = 'tactile-ba-handle-grip';
        this.divider.appendChild(grip);
      } else {
        grip.className = 'tactile-ba-handle-grip';
      }

      grip.innerHTML = `
        <svg class="tactile-ba-arrows-svg" viewBox="0 0 24 24" fill="none">
          <path d="M8.5 7.5L4 12l4.5 4.5M15.5 7.5L20 12l-4.5 4.5" stroke="#1A150B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      `;
      this.grip = grip;

      // Badges
      this.badgeBefore = this.container.querySelector('.tactile-ba-pill-before, .ba-tag-before, .muar-ba-badge-before');
      this.badgeAfter = this.container.querySelector('.tactile-ba-pill-after, .ba-tag-after, .muar-ba-badge-after');

      if (!this.badgeBefore) {
        this.badgeBefore = document.createElement('div');
        this.badgeBefore.className = 'tactile-ba-pill tactile-ba-pill-before';
        this.badgeBefore.innerHTML = `<span class="tactile-ba-dot"></span><span>${this.options.labelBefore}</span>`;
        this.container.appendChild(this.badgeBefore);
      } else {
        this.badgeBefore.classList.add('tactile-ba-pill', 'tactile-ba-pill-before');
      }

      if (!this.badgeAfter) {
        this.badgeAfter = document.createElement('div');
        this.badgeAfter.className = 'tactile-ba-pill tactile-ba-pill-after';
        this.badgeAfter.innerHTML = `<span class="tactile-ba-dot"></span><span>${this.options.labelAfter}</span>`;
        this.container.appendChild(this.badgeAfter);
      } else {
        this.badgeAfter.classList.add('tactile-ba-pill', 'tactile-ba-pill-after');
      }
    }

    setPercentage(pct, triggerTactile = true) {
      if (pct < 1) pct = 1;
      if (pct > 99) pct = 99;
      this.currentPct = pct;

      if (this.beforeLayer) {
        this.beforeLayer.style.clipPath = `inset(0 ${100 - pct}% 0 0)`;
      }
      if (this.divider) {
        this.divider.style.left = `${pct}%`;
      }

      this.container.setAttribute('aria-valuenow', Math.round(pct));

      // Intelligent badge dimming when divider nears
      if (this.badgeBefore) {
        const distBefore = Math.max(0, 1 - Math.abs(pct - 15) / 18);
        this.badgeBefore.style.opacity = pct < 20 ? `${Math.max(0.15, (pct - 2) / 18)}` : '1';
      }
      if (this.badgeAfter) {
        this.badgeAfter.style.opacity = pct > 80 ? `${Math.max(0.15, (98 - pct) / 18)}` : '1';
      }

      if (triggerTactile) {
        Tactile.sound.play('silk-drag');
      }

      if (typeof this.options.onPositionChange === 'function') {
        this.options.onPositionChange(pct);
      }
    }

    calcPctFromClientX(clientX) {
      const rect = this.container.getBoundingClientRect();
      const x = clientX - rect.left;
      let pct = (x / rect.width) * 100;
      return Math.max(1, Math.min(99, pct));
    }

    bindEvents() {
      // 1. Pointer Events for unified desktop & mobile touch tracking
      const onPointerDown = (e) => {
        this.isDragging = true;
        this.container.classList.add('is-dragging');
        Tactile.sound.play('brass-click');

        if (this.container.setPointerCapture && e.pointerId) {
          try {
            this.container.setPointerCapture(e.pointerId);
          } catch (_) {}
        }

        const pct = this.calcPctFromClientX(e.clientX);
        this.setPercentage(pct, true);
        e.preventDefault();
      };

      const onPointerMove = (e) => {
        if (!this.isDragging) return;
        const pct = this.calcPctFromClientX(e.clientX);
        this.setPercentage(pct, true);
      };

      const onPointerUp = (e) => {
        if (!this.isDragging) return;
        this.isDragging = false;
        this.container.classList.remove('is-dragging');
        if (this.container.releasePointerCapture && e.pointerId) {
          try {
            this.container.releasePointerCapture(e.pointerId);
          } catch (_) {}
        }
      };

      this.container.addEventListener('pointerdown', onPointerDown);
      window.addEventListener('pointermove', onPointerMove);
      window.addEventListener('pointerup', onPointerUp);
      window.addEventListener('pointercancel', onPointerUp);

      // Touch fallback for older WebViews
      this.container.addEventListener(
        'touchstart',
        (e) => {
          if (e.touches && e.touches[0]) {
            this.isDragging = true;
            this.container.classList.add('is-dragging');
            const pct = this.calcPctFromClientX(e.touches[0].clientX);
            this.setPercentage(pct, true);
          }
        },
        { passive: false }
      );

      window.addEventListener(
        'touchmove',
        (e) => {
          if (!this.isDragging) return;
          if (e.touches && e.touches[0]) {
            const pct = this.calcPctFromClientX(e.touches[0].clientX);
            this.setPercentage(pct, true);
            e.preventDefault();
          }
        },
        { passive: false }
      );

      window.addEventListener('touchend', () => {
        this.isDragging = false;
        this.container.classList.remove('is-dragging');
      });

      // Double-click to reset to 50%
      this.container.addEventListener('dblclick', () => {
        Tactile.sound.play('brass-click');
        this.animateTo(50, 300);
      });

      // Keyboard Controls (Accessibility)
      this.container.addEventListener('keydown', (e) => {
        let step = e.shiftKey ? 10 : 2;
        if (e.key === 'ArrowLeft') {
          this.setPercentage(this.currentPct - step, true);
          e.preventDefault();
        } else if (e.key === 'ArrowRight') {
          this.setPercentage(this.currentPct + step, true);
          e.preventDefault();
        } else if (e.key === 'Home') {
          this.animateTo(5, 250);
          e.preventDefault();
        } else if (e.key === 'End') {
          this.animateTo(95, 250);
          e.preventDefault();
        } else if (e.key === 'Enter' || e.key === ' ') {
          const target = this.currentPct > 50 ? 25 : 75;
          this.animateTo(target, 300);
          e.preventDefault();
        }
      });
    }

    animateTo(targetPct, duration = 300) {
      const startPct = this.currentPct;
      const startTime = performance.now();

      const step = (now) => {
        const elapsed = now - startTime;
        const progress = Math.min(1, elapsed / duration);
        // Ease Out Cubic
        const ease = 1 - Math.pow(1 - progress, 3);
        const current = startPct + (targetPct - startPct) * ease;
        this.setPercentage(current, false);

        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          Tactile.sound.play('brass-click');
        }
      };

      requestAnimationFrame(step);
    }

    setScene(beforeSrc, afterSrc, labelBefore, labelAfter) {
      const imgBefore = this.beforeLayer ? this.beforeLayer.querySelector('img') : null;
      const imgAfter = this.afterLayer ? this.afterLayer.querySelector('img') : null;

      if (imgBefore) imgBefore.src = beforeSrc;
      if (imgAfter) imgAfter.src = afterSrc;

      if (labelBefore && this.badgeBefore) {
        this.badgeBefore.querySelector('span:last-child').textContent = labelBefore;
      }
      if (labelAfter && this.badgeAfter) {
        this.badgeAfter.querySelector('span:last-child').textContent = labelAfter;
      }

      this.animateTo(50, 350);
    }
  }

  Tactile.BeforeAfterSlider = TactileBeforeAfterSlider;

  /* ==========================================================================
     3. PROJECT MONOGRAPH DRAWER & FULLSCREEN MODAL
     ========================================================================== */
  class TactileMonographDrawer {
    constructor() {
      this.currentProjectId = 1;
      this.isFullscreen = false;
      this.currentPhotoIdx = 0;
      this.activeSlider = null;
      this.drawerEl = null;
      this.backdropEl = null;

      this.createDOM();
      this.bindEvents();
    }

    createDOM() {
      let backdrop = document.getElementById('tactileDrawerBackdrop');
      if (!backdrop) {
        backdrop = document.createElement('div');
        backdrop.id = 'tactileDrawerBackdrop';
        backdrop.className = 'tactile-drawer-backdrop';
        document.body.appendChild(backdrop);
      }
      this.backdropEl = backdrop;

      let drawer = document.getElementById('tactileDrawer');
      if (!drawer) {
        drawer = document.createElement('div');
        drawer.id = 'tactileDrawer';
        drawer.className = 'tactile-drawer';
        drawer.setAttribute('role', 'dialog');
        drawer.setAttribute('aria-modal', 'true');
        drawer.setAttribute('aria-label', 'Монография проекта MUAR A');
        drawer.innerHTML = `
          <!-- Drawer Header -->
          <div class="tactile-drawer-header">
            <div class="tactile-drawer-meta-left">
              <span class="tactile-drawer-folio-num" id="drawerFolioNum">FOLIO № 01 / 10</span>
              <span class="tactile-drawer-cat-badge" id="drawerCatBadge">Частная Резиденция</span>
            </div>
            <div class="tactile-drawer-controls">
              <button type="button" class="tactile-drawer-nav-btn" id="drawerPrevBtn" title="Предыдущий проект (←)">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M15 18l-6-6 6-6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
              <button type="button" class="tactile-drawer-nav-btn" id="drawerNextBtn" title="Следующий проект (→)">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M9 18l6-6-6-6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
              <button type="button" class="tactile-drawer-nav-btn" id="drawerFullscreenBtn" title="Развернуть на весь экран">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3" stroke-linecap="round"/>
                </svg>
              </button>
              <button type="button" class="tactile-drawer-close-btn" id="drawerCloseBtn" title="Закрыть монографию (Esc)">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M18 6L6 18M6 6l12 12" stroke-linecap="round"/>
                </svg>
              </button>
            </div>
          </div>

          <!-- Drawer Body -->
          <div class="tactile-drawer-body" id="drawerBody">
            <!-- Stage Hero Visuals -->
            <div class="tactile-drawer-stage" id="drawerStageWrap">
              <div class="tactile-drawer-stage-toggle" id="drawerStageToggle" style="display:none;">
                <button type="button" class="tactile-stage-tab-btn is-active" id="drawerTabPhoto" data-mode="photo">Галерея</button>
                <button type="button" class="tactile-stage-tab-btn" id="drawerTabBA" data-mode="ba">Сравнение До / После</button>
              </div>

              <!-- Photo Gallery View -->
              <div class="tactile-drawer-main-img-wrap" id="drawerPhotoView">
                <img id="drawerMainImg" class="tactile-drawer-main-img" src="" alt="Интерьер MUAR A" draggable="false">
                <div class="tactile-drawer-photo-counter" id="drawerPhotoCounter">01 / 09</div>
              </div>

              <!-- Embedded Before/After Slider Container -->
              <div id="drawerBAView" style="display:none; width: 100%;"></div>

              <!-- Thumbnail Filmstrip Strip -->
              <div class="tactile-drawer-filmstrip" id="drawerFilmstrip"></div>
            </div>

            <!-- Monograph Article -->
            <article class="tactile-drawer-article">
              <div class="tactile-drawer-plaque">
                <div class="tactile-drawer-seal">✦</div>
                <div class="tactile-drawer-plaque-meta">
                  <span class="tactile-drawer-plaque-kicker">АРХИТЕКТУРНОЕ ПАРТНЕРСТВО</span>
                  <strong class="tactile-drawer-plaque-name" id="drawerCollaborator">Совместно с IDesign</strong>
                  <span class="tactile-drawer-plaque-role" id="drawerLocation">Астана · ЖК Vivaldi</span>
                </div>
              </div>

              <h2 class="tactile-drawer-title" id="drawerTitle">Панорамные окна в ЖК Vivaldi: Свет и Dimout</h2>

              <!-- Designer Quote -->
              <div class="tactile-drawer-quote">
                <div class="tactile-drawer-quote-mark">“</div>
                <blockquote id="drawerQuote"></blockquote>
                <div class="tactile-drawer-quote-author" id="drawerQuoteAuthor"></div>
              </div>

              <!-- Narrative Story -->
              <div class="tactile-drawer-story" id="drawerStory"></div>

              <!-- Technical Specifications HUD -->
              <div class="tactile-drawer-specs-wrap">
                <h4 class="tactile-drawer-specs-title">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M12 6v6l4 2"/>
                  </svg>
                  Архитектурные ТТХ & Кутюрные решения объекта:
                </h4>
                <div class="tactile-drawer-specs-grid" id="drawerSpecsGrid"></div>
              </div>

              <!-- Embedded Atelier Voice Note Player for this project -->
              <div class="tactile-audio-module" id="drawerVoiceModule">
                <div class="tactile-audio-header">
                  <div class="tactile-audio-title-wrap">
                    <div class="tactile-audio-mic-icon">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                        <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                        <line x1="12" y1="19" x2="12" y2="23"/>
                        <line x1="8" y1="23" x2="16" y2="23"/>
                      </svg>
                    </div>
                    <div>
                      <span class="tactile-audio-kicker">ГОЛОСОВАЯ ЗАМЕТКА МАСТЕРА</span>
                      <strong class="tactile-audio-label" id="drawerVoiceTitle">За кулисами проекта</strong>
                    </div>
                  </div>
                </div>

                <div class="tactile-audio-main-bar">
                  <button type="button" class="tactile-audio-play-btn" id="drawerVoicePlayBtn" aria-label="Воспроизвести заметку">
                    <svg viewBox="0 0 24 24">
                      <polygon points="5 3 19 12 5 21 5 3"/>
                    </svg>
                  </button>

                  <div class="tactile-audio-center">
                    <div class="tactile-audio-waveform-wrap" id="drawerWaveformWrap">
                      <canvas class="tactile-audio-waveform-canvas" id="drawerWaveformCanvas" width="400" height="38"></canvas>
                      <div class="tactile-audio-progress-bar" id="drawerAudioProgress"></div>
                    </div>
                    <div class="tactile-audio-time-row">
                      <span class="is-current" id="drawerAudioTimeCurrent">00:00</span>
                      <span id="drawerAudioTimeTotal">00:45</span>
                    </div>
                  </div>
                </div>

                <button type="button" class="tactile-transcript-toggle" id="drawerTranscriptToggle">
                  <span>Транскрипт аудиозаметки</span>
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M6 9l6 6 6-6"/>
                  </svg>
                </button>
                <div class="tactile-transcript-content" id="drawerTranscriptContent"></div>
              </div>
            </article>
          </div>

          <!-- Drawer Footer Action Bar -->
          <div class="tactile-drawer-footer">
            <button type="button" class="tactile-btn-primary" id="drawerCalcBtn">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="4" y="2" width="16" height="20" rx="2"/>
                <line x1="8" y1="6" x2="16" y2="6"/>
                <line x1="16" y1="14" x2="16" y2="18"/>
                <path d="M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"/>
              </svg>
              Рассчитать смету по образцу этого проекта
            </button>
            <a href="https://wa.me/77015243130" target="_blank" rel="noopener noreferrer" class="tactile-btn-secondary" id="drawerWaBtn">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/>
              </svg>
              Консультация Асенгуль в WhatsApp
            </a>
          </div>
        `;
        document.body.appendChild(drawer);
      }
      this.drawerEl = drawer;
    }

    bindEvents() {
      const closeBtn = document.getElementById('drawerCloseBtn');
      const prevBtn = document.getElementById('drawerPrevBtn');
      const nextBtn = document.getElementById('drawerNextBtn');
      const fullscreenBtn = document.getElementById('drawerFullscreenBtn');
      const calcBtn = document.getElementById('drawerCalcBtn');
      const tabPhoto = document.getElementById('drawerTabPhoto');
      const tabBA = document.getElementById('drawerTabBA');
      const transcriptToggle = document.getElementById('drawerTranscriptToggle');

      if (closeBtn) closeBtn.addEventListener('click', () => this.close());
      if (this.backdropEl) this.backdropEl.addEventListener('click', () => this.close());

      if (prevBtn) {
        prevBtn.addEventListener('click', () => {
          Tactile.sound.play('brass-click');
          this.navigate(-1);
        });
      }

      if (nextBtn) {
        nextBtn.addEventListener('click', () => {
          Tactile.sound.play('brass-click');
          this.navigate(1);
        });
      }

      if (fullscreenBtn) {
        fullscreenBtn.addEventListener('click', () => {
          Tactile.sound.play('brass-click');
          this.toggleFullscreen();
        });
      }

      if (tabPhoto) {
        tabPhoto.addEventListener('click', () => {
          Tactile.sound.play('brass-click');
          this.switchStageMode('photo');
        });
      }

      if (tabBA) {
        tabBA.addEventListener('click', () => {
          Tactile.sound.play('brass-click');
          this.switchStageMode('ba');
        });
      }

      if (transcriptToggle) {
        transcriptToggle.addEventListener('click', () => {
          const content = document.getElementById('drawerTranscriptContent');
          if (content) {
            content.classList.toggle('is-open');
            Tactile.sound.play('brass-click');
          }
        });
      }

      if (calcBtn) {
        calcBtn.addEventListener('click', () => {
          this.close();
          const calcSec = document.getElementById('calculator');
          if (calcSec) {
            calcSec.scrollIntoView({ behavior: 'smooth' });
          }
        });
      }

      // Global Keyboard navigation
      window.addEventListener('keydown', (e) => {
        if (!this.isOpen()) return;
        if (e.key === 'Escape') {
          this.close();
        } else if (e.key === 'ArrowLeft') {
          this.navigate(-1);
        } else if (e.key === 'ArrowRight') {
          this.navigate(1);
        }
      });
    }

    isOpen() {
      return this.drawerEl && this.drawerEl.classList.contains('is-open');
    }

    open(projectId = 1) {
      this.currentProjectId = parseInt(projectId, 10) || 1;
      this.currentPhotoIdx = 0;
      this.renderProject(this.currentProjectId);

      this.drawerEl.classList.add('is-open');
      this.backdropEl.classList.add('is-open');
      document.body.style.overflow = 'hidden';

      Tactile.sound.play('monograph-open');

      // Sync URL hash
      if (history.replaceState) {
        history.replaceState(null, null, `#monograph-${String(this.currentProjectId).padStart(2, '0')}`);
      }
    }

    close() {
      if (!this.isOpen()) return;
      this.drawerEl.classList.remove('is-open');
      this.backdropEl.classList.remove('is-open');
      document.body.style.overflow = '';

      if (this.isFullscreen) {
        this.toggleFullscreen(false);
      }

      Tactile.sound.play('monograph-close');

      // Stop voice audio if playing
      if (Tactile.voicePlayer) {
        Tactile.voicePlayer.pause();
      }

      if (history.replaceState) {
        history.replaceState(null, null, window.location.pathname);
      }
    }

    toggleFullscreen(forceState = null) {
      this.isFullscreen = forceState !== null ? forceState : !this.isFullscreen;
      if (this.isFullscreen) {
        this.drawerEl.classList.add('is-fullscreen');
      } else {
        this.drawerEl.classList.remove('is-fullscreen');
      }
    }

    navigate(direction = 1) {
      let nextId = this.currentProjectId + direction;
      if (nextId > 10) nextId = 1;
      if (nextId < 1) nextId = 10;
      this.open(nextId);
    }

    renderProject(projectId) {
      const p = MUAR_ARCHIVE_DATA.find((item) => item.id === projectId) || MUAR_ARCHIVE_DATA[0];

      // Update text fields
      document.getElementById('drawerFolioNum').textContent = `FOLIO № ${p.num} / 10`;
      document.getElementById('drawerCatBadge').textContent = p.cat_name;
      document.getElementById('drawerCollaborator').textContent = p.collaborator;
      document.getElementById('drawerLocation').textContent = p.location;
      document.getElementById('drawerTitle').textContent = p.title;
      document.getElementById('drawerQuote').textContent = p.quote;
      document.getElementById('drawerQuoteAuthor').textContent = p.quote_author;
      document.getElementById('drawerStory').innerHTML = `<p>${p.story}</p>`;

      // Specs HUD
      const specsGrid = document.getElementById('drawerSpecsGrid');
      specsGrid.innerHTML = p.specs
        .map(
          (s) => `
        <div class="tactile-spec-item">
          <span class="tactile-spec-bullet">✦</span>
          <span>${s}</span>
        </div>
      `
        )
        .join('');

      // WhatsApp link with prefilled project inquiry
      const waBtn = document.getElementById('drawerWaBtn');
      if (waBtn) {
        const text = encodeURIComponent(`Здравствуйте, Асенгуль! Меня заинтересовал проект №${p.num}: «${p.title}». Хочу проконсультироваться по тканям и стоимости.`);
        waBtn.href = `https://wa.me/77015243130?text=${text}`;
      }

      // Stage / Photos / Before-After
      const stageToggle = document.getElementById('drawerStageToggle');
      const photoView = document.getElementById('drawerPhotoView');
      const baView = document.getElementById('drawerBAView');

      if (p.has_ba) {
        stageToggle.style.display = 'flex';
        baView.innerHTML = `
          <div class="tactile-ba-container" id="drawerBaContainer" style="aspect-ratio: 16/10;">
            <div class="tactile-ba-layer tactile-ba-after">
              <img src="${p.ba_after}" alt="${p.ba_label_after}" draggable="false">
            </div>
            <div class="tactile-ba-layer tactile-ba-before">
              <img src="${p.ba_before}" alt="${p.ba_label_before}" draggable="false">
            </div>
            <div class="tactile-ba-divider">
              <div class="tactile-ba-handle-grip"></div>
            </div>
            <div class="tactile-ba-pill tactile-ba-pill-before">
              <span class="tactile-ba-dot"></span><span>${p.ba_label_before}</span>
            </div>
            <div class="tactile-ba-pill tactile-ba-pill-after">
              <span class="tactile-ba-dot"></span><span>${p.ba_label_after}</span>
            </div>
          </div>
        `;
        this.activeSlider = new TactileBeforeAfterSlider(baView.querySelector('#drawerBaContainer'));
      } else {
        stageToggle.style.display = 'none';
        baView.innerHTML = '';
        this.activeSlider = null;
      }

      this.switchStageMode('photo');
      this.renderPhotoGallery(p);
      this.renderVoiceNote(p);
    }

    switchStageMode(mode = 'photo') {
      const tabPhoto = document.getElementById('drawerTabPhoto');
      const tabBA = document.getElementById('drawerTabBA');
      const photoView = document.getElementById('drawerPhotoView');
      const baView = document.getElementById('drawerBAView');
      const filmstrip = document.getElementById('drawerFilmstrip');

      if (mode === 'ba') {
        if (tabPhoto) tabPhoto.classList.remove('is-active');
        if (tabBA) tabBA.classList.add('is-active');
        if (photoView) photoView.style.display = 'none';
        if (baView) baView.style.display = 'block';
        if (filmstrip) filmstrip.style.display = 'none';
        if (this.activeSlider) this.activeSlider.setPercentage(50, false);
      } else {
        if (tabPhoto) tabPhoto.classList.add('is-active');
        if (tabBA) tabBA.classList.remove('is-active');
        if (photoView) photoView.style.display = 'block';
        if (baView) baView.style.display = 'none';
        if (filmstrip) filmstrip.style.display = 'flex';
      }
    }

    renderPhotoGallery(p) {
      const photos = p.photos || [];
      const mainImg = document.getElementById('drawerMainImg');
      const counter = document.getElementById('drawerPhotoCounter');
      const filmstrip = document.getElementById('drawerFilmstrip');

      if (photos.length > 0) {
        mainImg.src = photos[0].src;
        mainImg.alt = photos[0].alt;
        counter.textContent = `01 / ${String(photos.length).padStart(2, '0')}`;
      }

      filmstrip.innerHTML = photos
        .map(
          (ph, idx) => `
        <div class="tactile-drawer-thumb ${idx === 0 ? 'is-active' : ''}" data-index="${idx}">
          <img src="${ph.src}" alt="${ph.alt}" loading="lazy">
        </div>
      `
        )
        .join('');

      // Wire filmstrip clicks
      filmstrip.querySelectorAll('.tactile-drawer-thumb').forEach((thumb) => {
        thumb.addEventListener('click', (e) => {
          const idx = parseInt(thumb.getAttribute('data-index'), 10);
          this.setPhotoIndex(idx, photos);
          Tactile.sound.play('brass-click');
        });
      });
    }

    setPhotoIndex(idx, photos) {
      if (!photos || !photos[idx]) return;
      this.currentPhotoIdx = idx;
      const mainImg = document.getElementById('drawerMainImg');
      const counter = document.getElementById('drawerPhotoCounter');
      const filmstrip = document.getElementById('drawerFilmstrip');

      mainImg.style.opacity = '0.6';
      mainImg.src = photos[idx].src;
      mainImg.alt = photos[idx].alt;
      setTimeout(() => (mainImg.style.opacity = '1'), 150);

      counter.textContent = `${String(idx + 1).padStart(2, '0')} / ${String(photos.length).padStart(2, '0')}`;

      filmstrip.querySelectorAll('.tactile-drawer-thumb').forEach((th, i) => {
        if (i === idx) {
          th.classList.add('is-active');
          th.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
        } else {
          th.classList.remove('is-active');
        }
      });
    }

    renderVoiceNote(p) {
      const note = p.voice_note;
      const titleEl = document.getElementById('drawerVoiceTitle');
      const timeTotal = document.getElementById('drawerAudioTimeTotal');
      const transcriptEl = document.getElementById('drawerTranscriptContent');
      const playBtn = document.getElementById('drawerVoicePlayBtn');

      if (note) {
        titleEl.textContent = note.title;
        timeTotal.textContent = note.duration;
        transcriptEl.innerHTML = `<p class="tactile-transcript-quote">${note.transcript}</p>`;

        // Wire play button to central voice player
        playBtn.onclick = () => {
          if (Tactile.voicePlayer) {
            Tactile.voicePlayer.loadAndToggleTrack(note.track, note.title, note.transcript);
          }
        };
      }
    }
  }

  Tactile.MonographDrawer = TactileMonographDrawer;

  /* ==========================================================================
     4. ATELIER AUDIO COMMENTARY PLAYER (Waveform & Web Audio API)
     ========================================================================== */
  class TactileVoicePlayer {
    constructor() {
      this.audio = new Audio();
      this.isPlaying = false;
      this.currentTrackIndex = 0;
      this.analyser = null;
      this.audioSourceNode = null;
      this.dataArray = null;
      this.rafId = null;
      this.canUseWebAudio = true;

      this.initAudio();
      this.initWaveformCanvas();
    }

    initAudio() {
      this.audio.preload = 'none';

      this.audio.addEventListener('timeupdate', () => {
        this.updateProgress();
      });

      this.audio.addEventListener('ended', () => {
        this.isPlaying = false;
        this.updatePlayStateUI(false);
      });

      this.audio.addEventListener('error', () => {
        // Fallback gracefully without breaking UI
        console.warn('TactileVoicePlayer: Audio source loading error, maintaining luxury fallback state.');
      });
    }

    connectWebAudio() {
      const ctx = Tactile.sound.getContext();
      if (!ctx || this.audioSourceNode) return;

      try {
        this.analyser = ctx.createAnalyser();
        this.analyser.fftSize = 64;
        this.analyser.smoothingTimeConstant = 0.8;
        this.dataArray = new Uint8Array(this.analyser.frequencyBinCount);

        this.audioSourceNode = ctx.createMediaElementSource(this.audio);
        this.audioSourceNode.connect(this.analyser);
        this.analyser.connect(ctx.destination);
      } catch (err) {
        this.canUseWebAudio = false;
      }
    }

    loadAndToggleTrack(trackUrl, title, transcript) {
      Tactile.sound.play('brass-click');
      const fullUrl = trackUrl.startsWith('http') || trackUrl.startsWith('assets/') ? trackUrl : `assets/muar/voice/${trackUrl}`;

      if (this.audio.src.includes(trackUrl) && this.isPlaying) {
        this.pause();
      } else {
        if (!this.audio.src.includes(trackUrl)) {
          this.audio.src = fullUrl;
          this.audio.load();
        }
        this.play();
      }
    }

    play() {
      this.connectWebAudio();
      const promise = this.audio.play();
      if (promise !== undefined) {
        promise
          .then(() => {
            this.isPlaying = true;
            this.updatePlayStateUI(true);
            this.startWaveformLoop();
          })
          .catch(() => {
            // Simulated playback for restricted environments
            this.isPlaying = true;
            this.updatePlayStateUI(true);
            this.startWaveformLoop();
          });
      }
    }

    pause() {
      this.audio.pause();
      this.isPlaying = false;
      this.updatePlayStateUI(false);
    }

    updatePlayStateUI(isPlaying) {
      const playBtns = document.querySelectorAll('.tactile-audio-play-btn');
      playBtns.forEach((btn) => {
        if (isPlaying) {
          btn.innerHTML = `
            <svg viewBox="0 0 24 24">
              <rect x="6" y="4" width="4" height="16" fill="currentColor"/>
              <rect x="14" y="4" width="4" height="16" fill="currentColor"/>
            </svg>
          `;
        } else {
          btn.innerHTML = `
            <svg viewBox="0 0 24 24">
              <polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/>
            </svg>
          `;
        }
      });
    }

    updateProgress() {
      const duration = this.audio.duration || 45;
      const current = this.audio.currentTime || 0;
      const pct = (current / duration) * 100;

      const progressBars = document.querySelectorAll('.tactile-audio-progress-bar');
      progressBars.forEach((bar) => (bar.style.width = `${pct}%`));

      const timeCurrents = document.querySelectorAll('#drawerAudioTimeCurrent, .tactile-audio-time-current');
      timeCurrents.forEach((tc) => {
        tc.textContent = this.formatTime(current);
      });
    }

    formatTime(sec) {
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    initWaveformCanvas() {
      this.canvases = document.querySelectorAll('.tactile-audio-waveform-canvas');
      this.startWaveformLoop();
    }

    startWaveformLoop() {
      if (this.rafId) cancelAnimationFrame(this.rafId);

      const render = () => {
        const canvases = document.querySelectorAll('.tactile-audio-waveform-canvas');
        if (this.analyser && this.isPlaying) {
          this.analyser.getByteFrequencyData(this.dataArray);
        }

        const now = performance.now() * 0.003;

        canvases.forEach((canvas) => {
          const ctx = canvas.getContext('2d');
          const width = canvas.width;
          const height = canvas.height;
          ctx.clearRect(0, 0, width, height);

          const numBars = 32;
          const barWidth = 3;
          const gap = (width - numBars * barWidth) / (numBars - 1);

          for (let i = 0; i < numBars; i++) {
            let barHeight = 4;
            if (this.isPlaying) {
              if (this.dataArray && this.dataArray[i]) {
                barHeight = Math.max(4, (this.dataArray[i] / 255) * (height - 6));
              } else {
                barHeight = Math.max(4, Math.sin(now + i * 0.4) * (height * 0.35) + height * 0.4);
              }
            } else {
              barHeight = 4 + Math.sin(now * 0.5 + i * 0.2) * 2;
            }

            const x = i * (barWidth + gap);
            const y = (height - barHeight) / 2;

            const grad = ctx.createLinearGradient(0, y, 0, y + barHeight);
            grad.addColorStop(0, '#D8BC94');
            grad.addColorStop(0.5, '#C5A880');
            grad.addColorStop(1, '#8A6F48');

            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.roundRect(x, y, barWidth, barHeight, 2);
            ctx.fill();
          }
        });

        this.rafId = requestAnimationFrame(render);
      };

      this.rafId = requestAnimationFrame(render);
    }
  }

  Tactile.VoicePlayer = TactileVoicePlayer;

  /* ==========================================================================
     5. CATEGORY FILTERING TABS (Luxury Capsule Design)
     ========================================================================== */
  class TactileCategoryFilter {
    constructor(tabsBar, options = {}) {
      if (typeof tabsBar === 'string') {
        tabsBar = document.querySelector(tabsBar);
      }
      if (!tabsBar) return;

      this.tabsBar = tabsBar;
      this.options = Object.assign(
        {
          cardsSelector: '.monograph-card',
          activeCategory: 'all',
          onFilterChange: null
        },
        options
      );

      this.currentCategory = this.options.activeCategory;
      this.indicator = null;

      this.setupDOM();
      this.bindEvents();
      this.applyFilter(this.currentCategory, false);
    }

    setupDOM() {
      this.tabsBar.classList.add('tactile-filter-bar');

      // Create 5 luxury editorial categories if needed
      const luxuryTabsData = [
        { cat: "all", label: "Все 10 проектов", count: 10 },
        { cat: "villa", label: "Загородные Виллы", count: 3 },
        { cat: "penthouses", label: "Пентхаусы и Кабинеты", count: 3 },
        { cat: "bedroom", label: "Кроватные ансамбли", count: 3 },
        { cat: "contract", label: "Рестораны и Контракт", count: 2 }
      ];

      // If tabsBar has existing buttons, polish them; else generate
      const existingBtns = this.tabsBar.querySelectorAll('button');
      if (existingBtns.length === 0 || existingBtns.length < 5) {
        this.tabsBar.innerHTML = luxuryTabsData
          .map(
            (t) => `
          <button type="button" class="tactile-filter-btn ${t.cat === this.currentCategory ? 'is-active' : ''}" data-filter="${t.cat}">
            <span>${t.label}</span>
            <span class="tactile-filter-count">${t.count}</span>
          </button>
        `
          )
          .join('');
      } else {
        existingBtns.forEach((btn) => btn.classList.add('tactile-filter-btn'));
      }

      // Create sliding gold capsule pill
      let ind = this.tabsBar.querySelector('.tactile-filter-indicator');
      if (!ind) {
        ind = document.createElement('div');
        ind.className = 'tactile-filter-indicator';
        this.tabsBar.prepend(ind);
      }
      this.indicator = ind;

      this.updateIndicator(false);
    }

    bindEvents() {
      this.tabsBar.addEventListener('click', (e) => {
        const btn = e.target.closest('.tactile-filter-btn');
        if (!btn) return;
        const cat = btn.getAttribute('data-filter');
        this.applyFilter(cat, true);
      });

      // Window resize re-alignment
      window.addEventListener('resize', () => {
        this.updateIndicator(false);
      });
    }

    applyFilter(category = 'all', triggerTactile = true) {
      this.currentCategory = category;

      // Update button active states
      const btns = this.tabsBar.querySelectorAll('.tactile-filter-btn');
      btns.forEach((btn) => {
        const match = btn.getAttribute('data-filter') === category;
        btn.classList.toggle('is-active', match);
      });

      this.updateIndicator(true);

      // Filter project cards on the page
      const cards = document.querySelectorAll(this.options.cardsSelector);
      cards.forEach((card, idx) => {
        card.classList.add('tactile-animating-card');
        const cardCat = card.getAttribute('data-cat') || '';
        const cardId = parseInt(card.getAttribute('data-project-id'), 10);

        let isMatch = false;
        if (category === 'all') {
          isMatch = true;
        } else if (category === 'villa') {
          isMatch = cardCat === 'villa' || [3, 6, 7].includes(cardId);
        } else if (category === 'penthouses') {
          isMatch = [1, 2, 4].includes(cardId) || (cardCat === 'b2c' && [1, 2].includes(cardId));
        } else if (category === 'bedroom') {
          isMatch = [8, 9, 10].includes(cardId);
        } else if (category === 'contract') {
          isMatch = cardCat === 'b2b' || [4, 5].includes(cardId);
        } else {
          isMatch = cardCat === category;
        }

        if (isMatch) {
          card.classList.remove('tactile-card-hidden');
          card.classList.add('tactile-card-visible');
          card.style.display = '';
        } else {
          card.classList.remove('tactile-card-visible');
          card.classList.add('tactile-card-hidden');
          card.style.display = 'none';
        }
      });

      if (triggerTactile) {
        Tactile.sound.play('brass-click');
      }

      if (typeof this.options.onFilterChange === 'function') {
        this.options.onFilterChange(category);
      }
    }

    updateIndicator(animate = true) {
      if (!this.indicator) return;
      const activeBtn = this.tabsBar.querySelector('.tactile-filter-btn.is-active');
      if (!activeBtn) return;

      const barRect = this.tabsBar.getBoundingClientRect();
      const btnRect = activeBtn.getBoundingClientRect();

      const left = btnRect.left - barRect.left;
      const width = btnRect.width;

      if (!animate) {
        this.indicator.style.transition = 'none';
      } else {
        this.indicator.style.transition = '';
      }

      this.indicator.style.transform = `translateX(${left}px)`;
      this.indicator.style.width = `${width}px`;
    }
  }

  Tactile.CategoryFilter = TactileCategoryFilter;

  /* ==========================================================================
  /* ==========================================================================
     6. AUTO-ENHANCEMENT & INITIALIZATION ROUTINE
     ========================================================================== */
  Tactile.mountVoiceDock = function () {
    if (document.getElementById('tactileAudioDockBtn')) return;

    const dockBtn = document.createElement('button');
    dockBtn.id = 'tactileAudioDockBtn';
    dockBtn.className = 'tactile-audio-dock-btn';
    dockBtn.type = 'button';
    dockBtn.innerHTML = `
      <span class="tactile-audio-dock-dot"></span>
      <span>✦ Заметки мастера · Голос Асенгуль</span>
    `;

    const dockPanel = document.createElement('div');
    dockPanel.id = 'tactileAudioDockPanel';
    dockPanel.className = 'tactile-audio-dock-panel';
    dockPanel.innerHTML = `
      <div class="tactile-audio-dock-top">
        <span class="tactile-audio-kicker">АТЕЛЬЕ MUAR A · ГОЛОСОВОЙ АРХИВ</span>
        <button type="button" class="tactile-audio-dock-close" id="tactileAudioDockClose" title="Свернуть">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 6L6 18M6 6l12 12" stroke-linecap="round"/>
          </svg>
        </button>
      </div>
      <div style="margin-bottom: 12px;">
        <select class="tactile-audio-track-select" id="tactileDockTrackSelect" style="width:100%; max-width:100%;">
          ${VOICE_MEMOS.map((m, i) => `<option value="${i}">${m.title}</option>`).join('')}
        </select>
      </div>
      <div class="tactile-audio-main-bar">
        <button type="button" class="tactile-audio-play-btn" id="tactileDockPlayBtn" aria-label="Воспроизвести">
          <svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        </button>
        <div class="tactile-audio-center">
          <div class="tactile-audio-waveform-wrap" id="tactileDockWaveWrap">
            <canvas class="tactile-audio-waveform-canvas" width="280" height="38"></canvas>
            <div class="tactile-audio-progress-bar" id="tactileDockProgress"></div>
          </div>
          <div class="tactile-audio-time-row">
            <span class="is-current" id="tactileDockTimeCurrent">00:00</span>
            <span id="tactileDockTimeTotal">${VOICE_MEMOS[0].duration}</span>
          </div>
        </div>
      </div>
      <button type="button" class="tactile-transcript-toggle" id="tactileDockTranscriptToggle" style="margin-top:10px;">
        <span>Транскрипт заметки</span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
      </button>
      <div class="tactile-transcript-content" id="tactileDockTranscriptContent">
        <p class="tactile-transcript-quote">${VOICE_MEMOS[0].transcript}</p>
      </div>
    `;

    document.body.appendChild(dockBtn);
    document.body.appendChild(dockPanel);

    dockBtn.addEventListener('click', () => {
      Tactile.sound.play('brass-click');
      dockPanel.classList.toggle('is-open');
    });

    const closeBtn = document.getElementById('tactileAudioDockClose');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        dockPanel.classList.remove('is-open');
      });
    }

    const select = document.getElementById('tactileDockTrackSelect');
    if (select) {
      select.addEventListener('change', (e) => {
        const idx = parseInt(e.target.value, 10);
        const m = VOICE_MEMOS[idx];
        if (m && Tactile.voicePlayer) {
          document.getElementById('tactileDockTimeTotal').textContent = m.duration;
          document.getElementById('tactileDockTranscriptContent').innerHTML = `<p class="tactile-transcript-quote">${m.transcript}</p>`;
          Tactile.voicePlayer.loadAndToggleTrack(m.track, m.title, m.transcript);
        }
      });
    }

    const dockPlayBtn = document.getElementById('tactileDockPlayBtn');
    if (dockPlayBtn) {
      dockPlayBtn.addEventListener('click', () => {
        const idx = parseInt(select ? select.value : 0, 10);
        const m = VOICE_MEMOS[idx];
        if (m && Tactile.voicePlayer) {
          Tactile.voicePlayer.loadAndToggleTrack(m.track, m.title, m.transcript);
        }
      });
    }

    const transcriptToggle = document.getElementById('tactileDockTranscriptToggle');
    if (transcriptToggle) {
      transcriptToggle.addEventListener('click', () => {
        const c = document.getElementById('tactileDockTranscriptContent');
        if (c) c.classList.toggle('is-open');
      });
    }
  };

  Tactile.init = function () {
    // 1. Initialize Voice Audio Player
    Tactile.voicePlayer = new TactileVoicePlayer();

    // 2. Initialize Monograph Drawer
    Tactile.monographDrawer = new TactileMonographDrawer();

    // 3. Mount Floating Atelier Audio Dock
    Tactile.mountVoiceDock();

    // 4. Enhance all Project Cards to open Monograph Drawer on click
    const projectCards = document.querySelectorAll('.monograph-card');
    projectCards.forEach((card) => {
      const pIdStr = card.getAttribute('data-project-id');
      const pId = parseInt(pIdStr, 10);
      if (!pId) return;

      // Add Luxury Action Button if not present
      if (!card.querySelector('.tactile-open-drawer-btn')) {
        const triggerWrap = document.createElement('div');
        triggerWrap.className = 'tactile-card-trigger-wrap';
        triggerWrap.innerHTML = `
          <button type="button" class="tactile-open-drawer-btn" data-project-id="${pId}">
            <span>Открыть монографию проекта №${String(pId).padStart(2, '0')}</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        `;
        const contentCol = card.querySelector('.monograph-content-col');
        if (contentCol) {
          contentCol.appendChild(triggerWrap);
        } else {
          card.appendChild(triggerWrap);
        }
      }

      // Make card title and media preview directly clickable
      const title = card.querySelector('.monograph-title');
      if (title) {
        title.style.cursor = 'pointer';
        title.setAttribute('title', `Нажмите, чтобы открыть монографию проекта №${String(pId).padStart(2, '0')}`);
        title.addEventListener('click', () => {
          Tactile.monographDrawer.open(pId);
        });
      }

      const mediaWrap = card.querySelector('.monograph-media-col, .monograph-main-photo-wrap');
      if (mediaWrap) {
        mediaWrap.style.cursor = 'pointer';
        mediaWrap.setAttribute('title', `Нажмите, чтобы открыть монографию проекта №${String(pId).padStart(2, '0')}`);
        mediaWrap.addEventListener('click', (e) => {
          if (e.target.closest('button, a')) return;
          Tactile.monographDrawer.open(pId);
        });
      }
    });

    // Wire global delegation for open monograph buttons
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.tactile-open-drawer-btn, [data-open-monograph]');
      if (btn) {
        const pId = btn.getAttribute('data-project-id') || btn.getAttribute('data-open-monograph');
        if (pId) {
          Tactile.monographDrawer.open(parseInt(pId, 10));
        }
      }
    });

    // 5. Initialize Hero / Dedicated Before-After Sliders
    const heroSlider = document.getElementById('baDedicatedSlider') || document.querySelector('.ba-slider-container');
    if (heroSlider) {
      Tactile.heroSlider = new TactileBeforeAfterSlider(heroSlider, {
        initialPosition: 50,
        onPositionChange: (pct) => {
          const pctEl = document.getElementById('baHeroCaptionPct');
          if (pctEl) pctEl.textContent = `${Math.round(pct)}% / ${Math.round(100 - pct)}%`;
        }
      });
    }

    // 6. Enhance Category Filter Bar
    const filterTabsBar = document.querySelector('.filter-tabs-bar');
    if (filterTabsBar) {
      Tactile.filterEngine = new TactileCategoryFilter(filterTabsBar);
    }

    // 7. Bridge legacy window.switchBaScene and window.filterProjects
    const originalSwitchBa = window.switchBaScene;
    window.switchBaScene = function (sceneId, btn) {
      if (typeof originalSwitchBa === 'function') {
        originalSwitchBa(sceneId, btn);
      }
      if (Tactile.heroSlider) {
        Tactile.heroSlider.animateTo(50, 300);
      }
    };

    const originalFilter = window.filterProjects;
    window.filterProjects = function (cat) {
      if (Tactile.filterEngine) {
        Tactile.filterEngine.applyFilter(cat, true);
      } else if (typeof originalFilter === 'function') {
        originalFilter(cat);
      }
    };

    // 8. Check for URL Hash to auto-open monograph (e.g. #monograph-07)
    const hash = window.location.hash;
    if (hash && hash.startsWith('#monograph-')) {
      const idStr = hash.replace('#monograph-', '');
      const pId = parseInt(idStr, 10);
      if (pId >= 1 && pId <= 10) {
        setTimeout(() => Tactile.monographDrawer.open(pId), 400);
      }
    }
  };

  // Expose convenient global helpers
  window.openMonograph = function (projectId) {
    if (Tactile.monographDrawer) {
      Tactile.monographDrawer.open(projectId);
    }
  };

  window.closeMonograph = function () {
    if (Tactile.monographDrawer) {
      Tactile.monographDrawer.close();
    }
  };

  // Auto-run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', Tactile.init);
  } else {
    Tactile.init();
  }

})(window, document);

