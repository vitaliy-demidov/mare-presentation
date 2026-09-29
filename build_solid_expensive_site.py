#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for MUAR A Ultra-Luxury Solid Presentation Website (v5.0 Solid Quiet Luxury).
Strictly implements the user's directive:
"не то вообще не красиво удаляй эту версию и переделывай и солидном лорогом стиле 5 агентов вкоючай и делай"

Architectural Benchmarks: Armani/Casa, Loro Piana Interiors, Dedar Milano, Pierre Frey.
Integrates outputs from all 5 specialized subagents:
1. Haute Artistic Director (Warm Cashmere Alabaster, Obsidian & Velvet Plum, Venetian Antique Gold, Cormorant Garamond)
2. Grand Monograph Curator (10 Real Projects, all 56 WebP photos, authentic stories, architect collaborator badges)
3. Tactile Motion Engineer (Before/After tactile slider, fullscreen Lightbox, ambient soundscape with Web Audio API)
4. Atelier & Engineering Architect (Real videos of Maral, 10m villa lift system, order journey, 6 couture quality pillars)
5. Precision Commerce Engineer (Exact Asengul Excel formulas, 508 800 ₸ target test, 3x2 fabric selector, B2B VAT 12%)
"""

import json
import urllib.parse
import os
import sys

from build_new_index import PROJECTS


COLLAB_DATA = {
    1: {
        "badge": "АВТОРСКИЙ СЦЕНАРИЙ MUAR A",
        "name": "MUAR A Haute Atelier",
        "role": "Текстильная драматургия Red & White · Шторы на светозащитной подкладке"
    },
    2: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Дизайн-студия IDesign",
        "role": "ЖК Vivaldi · Панорамный пентхаус, рассеивающий Dimout & Somfy"
    },
    3: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Дизайнер Зарина Секен",
        "role": "Загородная резиденция · Прозрачный римский тюль & Басонный кант"
    },
    4: {
        "badge": "КОНТРАКТНЫЙ СТАТУС B2B",
        "name": "Executive Cabinet First Lady / CEO",
        "role": "Кабинет первого лица · Сатин, Дамаск & Ручная кутюрная складка"
    },
    5: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Дизайнер Руслан",
        "role": "Гастрономическое пространство · Текстильные паруса свыше 4м"
    },
    6: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Дизайнер Динара Усманова",
        "role": "Загородный дом · Крафтовое панно Модерн 60-х & Нити мулине"
    },
    7: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Архитектор Габиден",
        "role": "Виллы «Темный Рыцарь» · 10-метровые моторизованные лифт-системы"
    },
    8: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Дизайнер Лаура Жакина",
        "role": "VIP-Спальня · Бордовый бархат, барельефная роза & Пайетки"
    },
    9: {
        "badge": "АВТОРСКИЙ СЦЕНАРИЙ MUAR A",
        "name": "MUAR A Interior",
        "role": "ЖК Evolution · Стальной и шоколадный кант, коррекция геометрии"
    },
    10: {
        "badge": "АВТОРСКИЙ СЦЕНАРИЙ MUAR A",
        "name": "MUAR A Family",
        "role": "ЖК «Атлант» / Дос · Гипоаллергенный текстиль & Авторские помпоны"
    }
}

BA_SCENES = {
    1: {
        "num": "01",
        "title": "Проект 01: Драматургия Red & White (Частная резиденция)",
        "desc": "Черновой интерьер vs законченный кутюрный шик: портьеры на светозащитной подкладке, авторская вставка с птицами и стёганое покрывало.",
        "before": "assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp",
        "after": "assets/muar/portfolio/garden-14.webp",
        "labelBefore": "Интерьер до текстиля",
        "labelAfter": "Драматургия Red & White"
    },
    2: {
        "num": "02",
        "title": "Проект 02: ЖК Vivaldi (Совместно с IDesign)",
        "desc": "Панорамные окна в пол, электрокарнизы Somfy, портьеры на подкладке Dimout от выгорания, римские шторы и покрывало со специальной подкладкой.",
        "before": "assets/muar/living-luxe-before.webp",
        "after": "assets/muar/portfolio/1.webp",
        "labelBefore": "Слепящее южное солнце",
        "labelAfter": "Мягкий свет Dimout"
    },
    3: {
        "num": "03",
        "title": "Проект 03: Загородный дом (Дизайнер Зарина Секен)",
        "desc": "Текстильный размах резиденции «под ключ»: басонные декоративные канты, прозрачный римский тюль, авторские формы валиков.",
        "before": "assets/muar/portfolio/_MG_9217-2.webp",
        "after": "assets/muar/portfolio/kzlst-13.webp",
        "labelBefore": "Пустое витражное окно",
        "labelAfter": "Римский тюль & Басонный кант"
    },
    7: {
        "num": "07",
        "title": "Проект 07: Виллы «Темный Рыцарь» (Архитектор Габиден)",
        "desc": "Высота потолков 10 метров: проектирование специальной лифт-системы с трубчатыми моторами и стальными тросами, плотный сатин на подкладке.",
        "before": "assets/muar/portfolio/IMG_4198.webp",
        "after": "assets/muar/portfolio/IMG_6721.webp",
        "labelBefore": "Черновой холл высотой 10 метров",
        "labelAfter": "Лифт-система «Темный Рыцарь»"
    },
    9: {
        "num": "09",
        "title": "Проект 09: Спальня — Коррекция асимметрии окна",
        "desc": "Живое преображение для компактных спален: вместо тяжелой портьеры — невесомая римская штора и льняной тюль бирюзовый омбре, исправившие геометрию пространства.",
        "before": "assets/muar/portfolio/project_09_before.webp",
        "after": "assets/muar/portfolio/project_09_after.webp",
        "labelBefore": "Асимметрия и темная портьера",
        "labelAfter": "Римская штора & Льняной тюль омбре"
    }
}

def build_solid_luxury_site():
    projects_json = json.dumps(PROJECTS, ensure_ascii=False)
    ba_scenes_json = json.dumps(BA_SCENES, ensure_ascii=False)
    
    # Read supporting CSS and JS files from scratch
    with open('scratch/luxury_tokens.css', 'r', encoding='utf-8') as f:
        luxury_tokens_css = f.read()

    with open('scratch/interactive_engine.css', 'r', encoding='utf-8') as f:
        interactive_engine_css = f.read()

    with open('scratch/interactive_engine.js', 'r', encoding='utf-8') as f:
        interactive_engine_js = f.read()

    # Read calculator CSS, HTML and JS with robust dynamic slicing
    with open('scratch/calculator_engine.html', 'r', encoding='utf-8') as f:
        calc_content = f.read()
    
    style_start = calc_content.find('<style>') + len('<style>')
    style_end = calc_content.find('</style>')
    calc_css = calc_content[style_start:style_end]

    html_start = calc_content.find('<div class="calc-container">')
    idx_main = calc_content.find('</main>')
    html_end = calc_content.find('</div>', idx_main) + len('</div>')
    calc_html = calc_content[html_start:html_end]

    scripts = calc_content.split('<script>')
    if len(scripts) >= 3:
        calc_controller_js = scripts[2].split('</script>')[0]
    else:
        calc_controller_js = "" 

    with open('scratch/calculator_engine.js', 'r', encoding='utf-8') as f:
        calculator_engine_js = f.read()

    # Pre-render the 10 project monograph cards
    monograph_cards_html = []
    folio_jump_links = []

    for p in PROJECTS:
        p_id = p["id"]
        p_num = p["num"]
        p_cat = p["cat"]
        p_cat_name = p["cat_name"]
        p_title = p["title"]
        p_collab = p["collaborator"]
        p_loc = p["location"]
        p_desc = p["desc"]
        p_specs = p["specs"]
        p_photos = p["photos"]
        p_has_ba = p.get("has_ba", False)
        
        wa_text = f"Здравствуйте, Асенгуль! Меня заинтересовал Проект №{p_num} «{p_title}» ({p_loc}). Хочу получить консультацию и рассчитать текстильный сценарий."
        wa_url = f"https://wa.me/77710551515?text={urllib.parse.quote(wa_text)}"

        folio_jump_links.append(f'''
          <a href="#folio-{p_num}" class="folio-jump-btn" data-folio="{p_num}">
            <span class="folio-jump-num">{p_num}</span>
            <span class="folio-jump-title">{p_cat_name}</span>
          </a>
        ''')

        # Collaboration plaque resolution
        collab_entry = COLLAB_DATA.get(p_id, {
            "badge": "АРХИТЕКТУРНАЯ КОЛЛАБОРАЦИЯ",
            "name": p_collab,
            "role": "Текстильный сценарий и кутюрный пошив MUAR A"
        })
        collab_badge = collab_entry["badge"]
        collab_name = collab_entry["name"]
        collab_role = collab_entry["role"]

        # Specs list items
        specs_html = "".join([f'<li class="spec-item"><span class="spec-bullet">✦</span> {s}</li>' for s in p_specs])

        # Photo gallery items (first 4 photos in primary grid, remaining accessible via Lightbox)
        gallery_items_html = []
        for idx, photo in enumerate(p_photos):
            p_src = photo["src"]
            p_alt = photo["alt"]
            is_extra = "extra-photo" if idx >= 4 else ""
            gallery_items_html.append(f'''
              <div class="project-photo-wrap {is_extra}" 
                   data-project-id="{p_id}" 
                   data-photo-index="{idx}"
                   onclick="openProjectLightbox({p_id}, {idx})">
                <img src="{p_src}" alt="{p_alt}" class="project-photo-img" loading="lazy">
                <div class="photo-overlay">
                  <span class="photo-zoom-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                      <circle cx="11" cy="11" r="7"/>
                      <line x1="21" y1="21" x2="16.65" y2="16.65"/>
                      <line x1="11" y1="8" x2="11" y2="14"/>
                      <line x1="8" y1="11" x2="14" y2="11"/>
                    </svg>
                  </span>
                  <span class="photo-caption-tag">{p_alt}</span>
                </div>
              </div>
            ''')

        gallery_html = "".join(gallery_items_html)
        photos_count = len(p_photos)

        # Before / After button if project has BA
        ba_badge_html = ""
        if p_has_ba:
            ba_badge_html = f'''
              <a href="#beforeAfter" onclick="switchBaScene({p_id});" class="collab-tag ba-tag" style="text-decoration:none;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M16 3h5v5M4 20L21 3M21 16v5h-5M9 21H4v-5"/>
                </svg>
                Интерактивное До / После
              </a>
            '''

        card_html = f'''
        <article class="monograph-card" id="folio-{p_num}" data-cat="{p_cat}" data-project-id="{p_id}">
          <div class="monograph-card-header">
            <div class="monograph-meta-left">
              <span class="folio-badge">FOLIO № {p_num} / 10</span>
              <span class="category-badge">{p_cat_name}</span>
              {ba_badge_html}
            </div>
            <div class="monograph-meta-right">
              <span class="location-badge">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 2a8 8 0 0 0-8 8c0 5.25 8 12 8 12s8-6.75 8-12a8 8 0 0 0-8-8z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                {p_loc}
              </span>
            </div>
          </div>

          <div class="monograph-grid">
            <div class="monograph-content-col">
              <div class="collab-plaque-couture">
                <div class="collab-seal-icon">✦</div>
                <div class="collab-plaque-content">
                  <span class="collab-plaque-kicker">{collab_badge}</span>
                  <strong class="collab-plaque-name">{collab_name}</strong>
                  <span class="collab-plaque-role">{collab_role}</span>
                </div>
              </div>

              <h3 class="monograph-title">{p_title}</h3>
              
              <div class="monograph-narrative">
                <p>{p_desc}</p>
              </div>

              <div class="monograph-specs-block">
                <h4 class="specs-title">Кутюрные решения & ТТХ:</h4>
                <ul class="specs-list">
                  {specs_html}
                </ul>
              </div>

              <div class="monograph-actions">
                <a href="{wa_url}" target="_blank" rel="noopener" class="btn-noir-gold">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
                  </svg>
                  Обсудить проект {p_num} в WhatsApp
                </a>
                <button type="button" class="btn-outline-gold" onclick="openProjectLightbox({p_id}, 0)">
                  Галерея ({photos_count} фото)
                </button>
              </div>
            </div>

            <div class="monograph-gallery-col">
              <div class="project-gallery-grid count-{min(photos_count, 4)}">
                {gallery_html}
              </div>
            </div>
          </div>
        </article>
        '''
        monograph_cards_html.append(card_html)

    all_cards_str = "\n".join(monograph_cards_html)
    jump_links_str = "\n".join(folio_jump_links)

    # Master HTML Template
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>MUAR A · Салон интерьерного текстиля и архитектурной солнцезащиты · Астана</title>
  <meta name="description" content="MUAR A — салон интерьерного текстиля в Астане с 2014 года. 2 этажа коллекций со всего мира, собственное швейное производство без надомниц, лифт-системы до 10 метров. Топ-30 декораторов СНГ (Golden O).">
  <meta name="theme-color" content="#131211">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="MUAR A · Текстильная архитектура и оформление знаковых резиденций">
  <meta property="og:description" content="10 реализованных проектов текстильного дома MUAR A. Виллы с высотой потолков 10м, пентхаусы, кабинеты первых лиц. Подлинные истории создания и расчет сметы.">
  <meta property="og:image" content="assets/muar/portfolio/garden-14.webp">
  <meta property="og:url" content="https://muar-a.pages.dev/">

  <!-- Canonical Fonts: Cormorant Garamond (Editorial Serif) + Manrope + JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=JetBrains+Mono:wght@400;500;600&family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
{luxury_tokens_css}

{interactive_engine_css}

{calc_css}

    /* ==========================================================================
       ADDITIONAL MONOGRAPH & ATELIER PRESENTATION STYLES (QUIET LUXURY)
       ========================================================================== */
    /* Header Bar */
    .master-header {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 80px;
      z-index: 1000;
      background: rgba(250, 248, 245, 0.94);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(197, 160, 105, 0.25);
      transition: var(--transition-couture);
    }}
    .master-header.scrolled {{
      height: 70px;
      box-shadow: 0 10px 30px rgba(19, 18, 17, 0.06);
    }}
    .header-inner {{
      max-width: 1440px;
      height: 100%;
      margin: 0 auto;
      padding: 0 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
    }}
    .brand-block {{
      display: flex;
      flex-direction: column;
      text-decoration: none;
    }}
    .brand-logo-text {{
      font-family: var(--font-serif);
      font-size: 1.75rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      color: var(--text-noir);
      line-height: 1.1;
      text-transform: uppercase;
    }}
    .brand-subline {{
      font-family: var(--font-sans);
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.22em;
      color: var(--gold-deep);
      text-transform: uppercase;
      margin-top: 2px;
    }}

    .header-nav {{
      display: flex;
      align-items: center;
      gap: 28px;
    }}
    .nav-link {{
      font-family: var(--font-sans);
      font-size: 0.88rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      color: var(--text-secondary);
      text-decoration: none;
      position: relative;
      padding: 6px 0;
      transition: color 0.25s ease;
    }}
    .nav-link:hover {{
      color: var(--text-noir);
    }}
    .nav-link::after {{
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0%;
      height: 1.5px;
      background: var(--gold-primary);
      transition: width 0.28s ease;
    }}
    .nav-link:hover::after {{
      width: 100%;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    /* Hero Section (Daylit Editorial Atmosphere) */
    .hero-editorial {{
      position: relative;
      padding-top: 130px;
      padding-bottom: 90px;
      background: linear-gradient(180deg, #F5F1EB 0%, #FAF8F5 100%);
      border-bottom: 1px solid rgba(197, 160, 105, 0.22);
      overflow: hidden;
    }}
    .hero-editorial::before {{
      content: "";
      position: absolute;
      top: -20%;
      right: -10%;
      width: 600px;
      height: 600px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(197, 160, 105, 0.08) 0%, transparent 70%);
      pointer-events: none;
    }}
    .hero-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 32px;
    }}
    .hero-layout {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 64px;
      align-items: center;
    }}
    .hero-kicker-wrap {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
    }}
    .kicker-line {{
      width: 36px;
      height: 1.5px;
      background: var(--gold-primary);
    }}
    .hero-kicker {{
      font-family: var(--font-sans);
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--gold-deep);
    }}
    .hero-title {{
      font-family: var(--font-serif);
      font-size: clamp(2.6rem, 4.5vw, 4.2rem);
      font-weight: 600;
      line-height: 1.15;
      letter-spacing: -0.02em;
      color: var(--text-noir);
      margin-bottom: 24px;
    }}
    .hero-title em {{
      font-style: italic;
      font-weight: 400;
      color: var(--gold-deep);
    }}
    .hero-lead {{
      font-family: var(--font-sans);
      font-size: clamp(1.05rem, 1.25vw, 1.22rem);
      font-weight: 400;
      line-height: 1.7;
      color: var(--text-secondary);
      margin-bottom: 36px;
      max-width: 620px;
    }}
    .hero-metrics-row {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-bottom: 40px;
      padding: 22px 24px;
      background: #FFFFFF;
      border: 1px solid rgba(197, 160, 105, 0.28);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-subtle);
    }}
    .metric-cell {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .metric-val {{
      font-family: var(--font-serif);
      font-size: 1.85rem;
      font-weight: 700;
      color: var(--text-noir);
      line-height: 1;
    }}
    .metric-lbl {{
      font-family: var(--font-sans);
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      line-height: 1.35;
    }}
    .hero-buttons {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .hero-stage-card {{
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 30px 70px rgba(19, 18, 17, 0.14);
      border: 1px solid rgba(197, 160, 105, 0.35);
      background: #FFFFFF;
    }}
    .hero-stage-img {{
      width: 100%;
      height: 540px;
      object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .hero-stage-card:hover .hero-stage-img {{
      transform: scale(1.025);
    }}
    .hero-stage-caption {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 24px 28px;
      background: linear-gradient(180deg, transparent 0%, rgba(19, 18, 17, 0.88) 100%);
      color: #FFFFFF;
    }}
    .stage-tag {{
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--gold-light);
      margin-bottom: 6px;
    }}
    .stage-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 600;
    }}

    /* Monograph Section */
    .section-monograph {{
      padding: 100px 0;
      background: var(--bg-canvas);
    }}
    .monograph-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 32px;
    }}
    .section-head-center {{
      text-align: center;
      max-width: 820px;
      margin: 0 auto 54px;
    }}
    .section-kicker-center {{
      display: inline-block;
      font-family: var(--font-sans);
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--gold-deep);
      margin-bottom: 12px;
    }}
    .section-title-monograph {{
      font-family: var(--font-serif);
      font-size: clamp(2.2rem, 3.8vw, 3.4rem);
      font-weight: 600;
      line-height: 1.2;
      color: var(--text-noir);
      margin-bottom: 18px;
    }}
    .section-title-monograph em {{
      font-style: italic;
      color: var(--gold-deep);
    }}
    .section-subtitle {{
      font-family: var(--font-sans);
      font-size: 1.08rem;
      font-weight: 400;
      line-height: 1.7;
      color: var(--text-secondary);
    }}

    /* Category Filter Tabs */
    .filter-tabs-bar {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 40px;
    }}
    .filter-tab-btn {{
      font-family: var(--font-sans);
      font-size: 0.86rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      padding: 11px 22px;
      background: #FFFFFF;
      border: 1px solid rgba(197, 160, 105, 0.28);
      border-radius: var(--radius-pill);
      color: var(--text-secondary);
      cursor: pointer;
      transition: var(--transition-couture);
    }}
    .filter-tab-btn:hover {{
      border-color: var(--gold-primary);
      color: var(--text-noir);
      transform: translateY(-1px);
    }}
    .filter-tab-btn.active {{
      background: var(--noir-deep);
      border-color: var(--gold-primary);
      color: #FFFFFF;
      box-shadow: 0 6px 20px rgba(19, 18, 17, 0.15);
    }}

    /* Folio Jump Bar */
    .folio-jump-nav {{
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 60px;
      padding: 14px 20px;
      background: #FFFFFF;
      border: 1px solid rgba(197, 160, 105, 0.22);
      border-radius: var(--radius-pill);
      box-shadow: var(--shadow-subtle);
      width: fit-content;
      margin-left: auto;
      margin-right: auto;
    }}
    .folio-jump-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-secondary);
      text-decoration: none;
      transition: var(--transition-couture);
    }}
    .folio-jump-btn:hover {{
      background: rgba(197, 160, 105, 0.12);
      color: var(--text-noir);
    }}
    .folio-jump-num {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--gold-deep);
    }}

    /* Monograph Card */
    .monograph-cards-list {{
      display: flex;
      flex-direction: column;
      gap: 64px;
    }}
    .monograph-card {{
      background: #FFFFFF;
      border: 1px solid rgba(197, 160, 105, 0.28);
      border-radius: var(--radius-xl);
      padding: 48px;
      box-shadow: var(--shadow-card);
      transition: var(--transition-couture);
      scroll-margin-top: 100px;
    }}
    .monograph-card:hover {{
      box-shadow: var(--shadow-hover);
      border-color: rgba(197, 160, 105, 0.5);
    }}
    .monograph-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      padding-bottom: 24px;
      margin-bottom: 32px;
      border-bottom: 1px solid rgba(19, 18, 17, 0.08);
    }}
    .monograph-meta-left {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .folio-badge {{
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      color: var(--gold-deep);
      background: rgba(197, 160, 105, 0.12);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(197, 160, 105, 0.35);
    }}
    .category-badge {{
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-secondary);
      background: var(--bg-canvas-subtle);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
    }}
    .ba-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-sans);
      font-size: 0.78rem;
      font-weight: 600;
      color: #9E7B42;
      background: rgba(197, 160, 105, 0.14);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(197, 160, 105, 0.35);
      transition: var(--transition-couture);
    }}
    .ba-tag:hover {{
      background: rgba(197, 160, 105, 0.22);
      color: var(--text-noir);
    }}
    .location-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
    }}

    .monograph-grid {{
      display: grid;
      grid-template-columns: 1.05fr 1.15fr;
      gap: 48px;
      align-items: start;
    }}
    .collaborator-box {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-bottom: 16px;
      padding: 12px 18px;
      background: var(--bg-canvas);
      border-left: 3px solid var(--gold-primary);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    }}
    .collab-label {{
      font-family: var(--font-sans);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--text-muted);
    }}
    .collab-name {{
      font-family: var(--font-sans);
      font-size: 0.94rem;
      font-weight: 700;
      color: var(--text-noir);
    }}
    .monograph-title {{
      font-family: var(--font-serif);
      font-size: clamp(1.85rem, 2.5vw, 2.35rem);
      font-weight: 600;
      line-height: 1.25;
      color: var(--text-noir);
      margin-bottom: 20px;
    }}
    .monograph-narrative {{
      font-family: var(--font-sans);
      font-size: 0.98rem;
      line-height: 1.75;
      color: var(--text-secondary);
      margin-bottom: 28px;
    }}
    .monograph-specs-block {{
      margin-bottom: 36px;
      padding: 20px 24px;
      background: #FAF8F5;
      border: 1px solid rgba(197, 160, 105, 0.22);
      border-radius: var(--radius-md);
    }}
    .specs-title {{
      font-family: var(--font-serif);
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text-noir);
      margin-bottom: 14px;
    }}
    .specs-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px 16px;
    }}
    .spec-item {{
      font-family: var(--font-sans);
      font-size: 0.84rem;
      font-weight: 500;
      color: var(--text-secondary);
      display: flex;
      align-items: baseline;
      gap: 8px;
    }}
    .spec-bullet {{
      color: var(--gold-deep);
      font-size: 0.75rem;
    }}
    .monograph-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
    }}

    /* Gallery Grid in Card */
    .project-gallery-grid {{
      display: grid;
      gap: 14px;
    }}
    .project-gallery-grid.count-1 {{ grid-template-columns: 1fr; }}
    .project-gallery-grid.count-2 {{ grid-template-columns: repeat(2, 1fr); }}
    .project-gallery-grid.count-3 {{
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: repeat(2, 220px);
    }}
    .project-gallery-grid.count-3 .project-photo-wrap:first-child {{
      grid-column: span 2;
    }}
    .project-gallery-grid.count-4 {{
      grid-template-columns: repeat(2, 1fr);
      grid-template-rows: repeat(2, 240px);
    }}
    .project-photo-wrap {{
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
      border: 1px solid rgba(197, 160, 105, 0.2);
      background: #131211;
      min-height: 200px;
    }}
    .project-photo-wrap.extra-photo {{
      display: none;
    }}
    .project-photo-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .project-photo-wrap:hover .project-photo-img {{
      transform: scale(1.05);
    }}
    .photo-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 40%, rgba(19, 18, 17, 0.75) 100%);
      display: flex;
      align-items: flex-end;
      padding: 14px 16px;
      opacity: 0;
      transition: opacity 0.3s ease;
    }}
    .project-photo-wrap:hover .photo-overlay {{
      opacity: 1;
    }}
    .photo-zoom-icon {{
      position: absolute;
      top: 14px;
      right: 14px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(19, 18, 17, 0.75);
      border: 1px solid rgba(197, 160, 105, 0.45);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(8px);
    }}
    .photo-caption-tag {{
      font-family: var(--font-sans);
      font-size: 0.75rem;
      font-weight: 500;
      color: #FFFFFF;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Before / After Dedicated Section Styles */
    .section-ba-master {{
      padding: 100px 0;
      background: #F4EFEB;
      border-top: 1px solid rgba(197, 160, 105, 0.25);
      border-bottom: 1px solid rgba(197, 160, 105, 0.25);
    }}
    .ba-tabs-nav {{
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      margin: 36px 0 40px;
    }}
    .ba-tab-btn {{
      padding: 11px 22px;
      border-radius: var(--radius-pill);
      background: #FFFFFF;
      border: 1px solid rgba(197, 160, 105, 0.3);
      font-family: var(--font-sans);
      font-size: 0.86rem;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
      transition: var(--transition-couture);
    }}
    .ba-tab-btn:hover {{
      border-color: var(--gold-primary);
      color: var(--text-noir);
      transform: translateY(-1px);
    }}
    .ba-tab-btn.active {{
      background: var(--noir-deep);
      border-color: var(--gold-primary);
      color: #FFFFFF;
      box-shadow: 0 6px 20px rgba(19, 18, 17, 0.15);
    }}
    .ba-stage-card {{
      background: #FFFFFF;
      border-radius: var(--radius-xl);
      border: 1px solid rgba(197, 160, 105, 0.35);
      box-shadow: var(--shadow-luxury);
      overflow: hidden;
      max-width: 1240px;
      margin: 0 auto;
    }}
    .ba-slider-hero {{
      width: 100%;
      height: 600px;
      position: relative;
    }}
    @media (max-width: 768px) {{
      .ba-slider-hero {{
        height: 380px;
      }}
    }}
    .ba-card-caption {{
      padding: 28px 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      flex-wrap: wrap;
      border-top: 1px solid rgba(197, 160, 105, 0.2);
      background: #FAF8F5;
    }}
    .ba-caption-text h4 {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-weight: 600;
      color: var(--text-noir);
      margin-bottom: 6px;
    }}
    .ba-caption-text p {{
      font-family: var(--font-sans);
      font-size: 0.92rem;
      color: var(--text-secondary);
      line-height: 1.6;
    }}

    /* Atelier Section (Nocturne Haute Luxury) */
    .section-atelier-nocturne {{
      padding: 110px 0;
      background: radial-gradient(circle at 50% 5%, #190E22 0%, #131211 65%, #0B0A09 100%);
      color: var(--text-light-primary);
      position: relative;
      border-top: 1px solid rgba(197, 160, 105, 0.35);
      border-bottom: 1px solid rgba(197, 160, 105, 0.35);
    }}
    .atelier-head {{
      text-align: center;
      max-width: 860px;
      margin: 0 auto 60px;
    }}
    .atelier-kicker {{
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--gold-light);
      margin-bottom: 14px;
    }}
    .atelier-title {{
      font-family: var(--font-serif);
      font-size: clamp(2.3rem, 4vw, 3.5rem);
      font-weight: 600;
      line-height: 1.18;
      color: #FAF8F5;
      margin-bottom: 20px;
    }}
    .atelier-title em {{
      font-style: italic;
      color: var(--gold-light);
    }}
    .atelier-desc {{
      font-family: var(--font-sans);
      font-size: 1.05rem;
      line-height: 1.75;
      color: rgba(250, 248, 245, 0.75);
    }}

    /* Video Exhibits Theater */
    .videos-grid-theater {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      margin-bottom: 80px;
    }}
    .video-exhibit-card {{
      background: var(--noir-surface);
      border: 1px solid rgba(197, 160, 105, 0.28);
      border-radius: var(--radius-lg);
      overflow: hidden;
      transition: var(--transition-couture);
      display: flex;
      flex-direction: column;
    }}
    .video-exhibit-card:hover {{
      border-color: var(--gold-primary);
      transform: translateY(-4px);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    }}
    .video-thumb-container {{
      position: relative;
      height: 260px;
      overflow: hidden;
      cursor: pointer;
    }}
    .video-thumb-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }}
    .video-thumb-container:hover .video-thumb-img {{
      transform: scale(1.04);
    }}
    .video-play-halo {{
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(19, 18, 17, 0.4);
      transition: background 0.3s ease;
    }}
    .video-thumb-container:hover .video-play-halo {{
      background: rgba(19, 18, 17, 0.2);
    }}
    .play-btn-gold {{
      width: 68px;
      height: 68px;
      border-radius: 50%;
      background: rgba(19, 18, 17, 0.85);
      border: 2px solid var(--gold-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--gold-light);
      box-shadow: 0 0 30px rgba(197, 160, 105, 0.35);
      transition: transform 0.3s ease, border-color 0.3s ease;
    }}
    .video-thumb-container:hover .play-btn-gold {{
      transform: scale(1.08);
      border-color: #FFFFFF;
    }}
    .video-duration-chip {{
      position: absolute;
      bottom: 12px;
      right: 14px;
      background: rgba(0, 0, 0, 0.8);
      font-family: var(--font-mono);
      font-size: 0.72rem;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }}
    .video-card-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}
    .video-card-kicker {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--gold-light);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}
    .video-card-title {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-weight: 600;
      color: #FAF8F5;
      margin-bottom: 12px;
      line-height: 1.3;
    }}
    .video-card-text {{
      font-family: var(--font-sans);
      font-size: 0.88rem;
      color: rgba(250, 248, 245, 0.7);
      line-height: 1.6;
      margin-bottom: 20px;
      flex: 1;
    }}

    /* 6 Pillars of Quality */
    .pillars-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-bottom: 80px;
    }}
    .pillar-card {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(197, 160, 105, 0.22);
      border-radius: var(--radius-md);
      padding: 30px 26px;
      transition: var(--transition-couture);
    }}
    .pillar-card:hover {{
      border-color: var(--gold-primary);
      background: rgba(255, 255, 255, 0.05);
      transform: translateY(-2px);
    }}
    .pillar-num {{
      font-family: var(--font-serif);
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 14px;
      line-height: 1;
    }}
    .pillar-title {{
      font-family: var(--font-serif);
      font-size: 1.22rem;
      font-weight: 600;
      color: #FAF8F5;
      margin-bottom: 10px;
    }}
    .pillar-text {{
      font-family: var(--font-sans);
      font-size: 0.86rem;
      color: rgba(250, 248, 245, 0.68);
      line-height: 1.65;
    }}

    /* Duo Profiles */
    .profiles-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 36px;
    }}
    .profile-card {{
      background: var(--noir-surface);
      border: 1px solid rgba(197, 160, 105, 0.35);
      border-radius: var(--radius-lg);
      padding: 36px;
      display: grid;
      grid-template-columns: 140px 1fr;
      gap: 28px;
      align-items: center;
    }}
    .profile-photo {{
      width: 140px;
      height: 140px;
      border-radius: 50%;
      object-fit: cover;
      border: 2px solid var(--gold-primary);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
    }}
    .profile-role {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--gold-light);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    .profile-name {{
      font-family: var(--font-serif);
      font-size: 1.7rem;
      font-weight: 600;
      color: #FAF8F5;
      margin-bottom: 10px;
    }}
    .profile-bio {{
      font-family: var(--font-sans);
      font-size: 0.88rem;
      color: rgba(250, 248, 245, 0.75);
      line-height: 1.6;
      margin-bottom: 16px;
    }}

    /* Calculator Master Section */
    .section-calc-master {{
      padding: 100px 0;
      background: var(--bg-canvas);
    }}

    /* Footer */
    .master-footer {{
      background: var(--noir-deep);
      color: rgba(250, 248, 245, 0.75);
      padding: 80px 0 40px;
      border-top: 1px solid rgba(197, 160, 105, 0.3);
    }}
    .footer-container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 32px;
    }}
    .footer-top-grid {{
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      gap: 60px;
      margin-bottom: 60px;
    }}
    .footer-brand-title {{
      font-family: var(--font-serif);
      font-size: 2rem;
      font-weight: 700;
      color: #FAF8F5;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      margin-bottom: 12px;
    }}
    .footer-brand-desc {{
      font-family: var(--font-sans);
      font-size: 0.94rem;
      line-height: 1.7;
      color: rgba(250, 248, 245, 0.65);
      max-width: 440px;
      margin-bottom: 24px;
    }}
    .footer-col-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 600;
      color: #FAF8F5;
      margin-bottom: 20px;
    }}
    .footer-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .footer-list a {{
      color: rgba(250, 248, 245, 0.7);
      font-size: 0.92rem;
      text-decoration: none;
      transition: color 0.2s ease;
    }}
    .footer-list a:hover {{
      color: var(--gold-light);
    }}
    .footer-bottom {{
      padding-top: 30px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.82rem;
      color: rgba(250, 248, 245, 0.45);
    }}

    /* Cinema Modal for Video */
    .cinema-modal {{
      position: fixed;
      inset: 0;
      z-index: 3000;
      background: rgba(10, 9, 8, 0.95);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 32px;
    }}
    .cinema-modal.active {{
      display: flex;
    }}
    .cinema-modal-box {{
      width: 100%;
      max-width: 1000px;
      background: var(--noir-surface);
      border: 1px solid var(--gold-primary);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 40px 90px rgba(0, 0, 0, 0.9);
      position: relative;
    }}
    .cinema-modal-header {{
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(197, 160, 105, 0.25);
    }}
    .cinema-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      color: #FAF8F5;
    }}
    .cinema-close-btn {{
      background: transparent;
      border: none;
      color: var(--gold-light);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 6px;
      transition: transform 0.2s ease;
    }}
    .cinema-close-btn:hover {{
      transform: scale(1.15);
      color: #FFFFFF;
    }}
    .cinema-video-wrap {{
      width: 100%;
      height: 560px;
      background: #000;
    }}
    .cinema-video-player {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    /* Responsive Queries */
    @media (max-width: 1100px) {{
      .hero-layout {{
        grid-template-columns: 1fr;
        gap: 40px;
      }}
      .hero-stage-img {{
        height: 420px;
      }}
      .monograph-grid {{
        grid-template-columns: 1fr;
      }}
      .videos-grid-theater {{
        grid-template-columns: 1fr;
      }}
      .pillars-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .profiles-grid {{
        grid-template-columns: 1fr;
      }}
      .footer-top-grid {{
        grid-template-columns: 1fr;
        gap: 40px;
      }}
    }}
    @media (max-width: 768px) {{
      .master-header {{
        height: 70px;
      }}
      .header-nav {{
        display: none;
      }}
      .hero-editorial {{
        padding-top: 100px;
        padding-bottom: 60px;
      }}
      .hero-metrics-row {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .monograph-card {{
        padding: 24px;
        border-radius: var(--radius-lg);
      }}
      .specs-list {{
        grid-template-columns: 1fr;
      }}
      .project-gallery-grid.count-3,
      .project-gallery-grid.count-4 {{
        grid-template-columns: 1fr;
        grid-template-rows: auto;
      }}
      .project-gallery-grid.count-3 .project-photo-wrap:first-child {{
        grid-column: span 1;
      }}
      .pillars-grid {{
        grid-template-columns: 1fr;
      }}
      .profile-card {{
        grid-template-columns: 1fr;
        text-align: center;
      }}
      .profile-photo {{
        margin: 0 auto;
      }}
    }}
  </style>
</head>
<body>

  <!-- ========================================================================
       1. MASTER FLOATING HEADER (ALABASTER & ANTIQUE GOLD)
       ======================================================================== -->
  <header class="master-header" id="masterHeader">
    <div class="header-inner">
      <a href="#top" class="brand-block">
        <span class="brand-logo-text">MUAR A</span>
        <span class="brand-subline">ATELIER D'ART TEXTILE · EST. 2014</span>
      </a>

      <nav class="header-nav">
        <a href="#monograph" class="nav-link">10 Проектов</a>
        <a href="#beforeAfter" class="nav-link">До / После</a>
        <a href="#qualityMarks" class="nav-link">Знаки Качества</a>
        <a href="#atelier" class="nav-link">Ателье & Высота 10м</a>
        <a href="#calculator" class="nav-link">Точный Расчет</a>
        <a href="#contacts" class="nav-link">Контакты</a>
      </nav>

      <div class="header-actions">
        <!-- Ambient Soundscape Toggle Button -->
        <button type="button" class="btn-soundscape" id="soundscapeBtn" onclick="window.muarSoundscape && window.muarSoundscape.toggleSound()" title="Атмосфера салона">
          <span class="sound-wave-bars">
            <span class="sound-bar"></span>
            <span class="sound-bar"></span>
            <span class="sound-bar"></span>
            <span class="sound-bar"></span>
          </span>
          <span class="sound-label">Атмосфера</span>
        </button>

        <a href="https://wa.me/77710551515?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C%20MUAR%20A!%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C%D1%81%D1%8F%20%D0%BD%D0%B0%20%D0%B2%D0%B8%D0%B7%D0%B8%D1%82%20%D0%B2%20%D1%81%D0%B0%D0%BB%D0%BE%D0%BD." 
           target="_blank" rel="noopener" class="btn-noir-gold" style="padding: 10px 20px; font-size: 0.84rem;">
          Запись в салон
        </a>
      </div>
    </div>
  </header>

  <!-- ========================================================================
       2. HERO SECTION: SUNLIT ARCHITECTURAL EDITORIAL
       ======================================================================== -->
  <section class="hero-editorial" id="top">
    <div class="hero-container">
      <div class="hero-layout">
        <div class="hero-text-col">
          <div class="hero-kicker-wrap">
            <span class="kicker-line"></span>
            <span class="hero-kicker">Ведущий текстильный дом Астаны · с 2014 года</span>
          </div>

          <h1 class="hero-title">
            Текстильная архитектура и <em>кутюрный шик</em> знаковых пространств
          </h1>

          <p class="hero-lead">
            Собственное швейное ателье полного цикла без надомниц. Проектирование лифт-систем для окон высотой до 10 метров. Топ-30 текстильных декораторов СНГ, премия Golden O. Прямые контрактные поставки тканей из Италии, Испании, Бельгии и Франции.
          </p>

          <div class="hero-metrics-row">
            <div class="metric-cell">
              <span class="metric-val">12</span>
              <span class="metric-lbl">Лет опыта в Астане (EST. 2014)</span>
            </div>
            <div class="metric-cell">
              <span class="metric-val">10м</span>
              <span class="metric-lbl">Высота потолков и лифт-системы</span>
            </div>
            <div class="metric-cell">
              <span class="metric-val">56</span>
              <span class="metric-lbl">Архивных фото 10 шедевров</span>
            </div>
            <div class="metric-cell">
              <span class="metric-val">100%</span>
              <span class="metric-lbl">Собственный цех по ГОСТу РК</span>
            </div>
          </div>

          <!-- Hero Quality Trust Bar -->
          <div class="hero-trust-bar">
            <div class="trust-badge-item">
              <span class="trust-badge-icon">✦</span>
              <span><strong>Сертификат ЕАЭС:</strong> ГОСТ РК &amp; безопасность</span>
            </div>
            <div class="trust-divider"></div>
            <div class="trust-badge-item">
              <span class="trust-badge-icon">✦</span>
              <span><strong>Топ-30 СНГ:</strong> Международная премия Golden O</span>
            </div>
            <div class="trust-divider"></div>
            <div class="trust-badge-item">
              <span class="trust-badge-icon">✦</span>
              <span><strong>Архитектурная гильдия:</strong> IDesign, Зарина Секен, Габиден</span>
            </div>
          </div>

          <div class="hero-buttons" style="margin-top: 32px;">
            <a href="#monograph" class="btn-noir-gold">
              Смотреть 10 Реальных Проектов ↓
            </a>
            <a href="#calculator" class="btn-gold-satin">
              Точный Расчет Сметы (508 800 ₸)
            </a>
          </div>
        </div>

        <div class="hero-visual-col">
          <div class="hero-stage-card">
            <img src="assets/muar/hero-interior.webp" alt="Интерьерное текстильное оформление MUAR A Астана" class="hero-stage-img">
            <div class="hero-stage-caption">
              <span class="stage-tag">АСТАНА · ЧАСТНАЯ РЕЗИДЕНЦИЯ</span>
              <h3 class="stage-title">Драматургия светозащиты и архитектурная драпировка</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       3. ARCHITECTURAL MONOGRAPH: 10 REAL PROJECTS & 56 WEBP PHOTOGRAPHS
       ======================================================================== -->
  <section class="section-monograph" id="monograph">
    <div class="monograph-container">
      <div class="section-head-center">
        <span class="section-kicker-center">АРХИВ РЕАЛИЗОВАННЫХ ОБЪЕКТОВ · 2014–2026</span>
        <h2 class="section-title-monograph">
          Монография <em>10 знаковых проектов</em> MUAR A
        </h2>
        <p class="section-subtitle">
          Подлинные истории текстильного проектирования от основателя ателье Асенгуль и ведущих архитекторов Казахстана: Зарины Секен, IDesign, Габидена (Виллы «Темный Рыцарь»), Динары Усмановой, Лауры Жакиной и Руслана.
        </p>
      </div>

      <!-- Category Filter Tabs -->
      <div class="filter-tabs-bar">
        <button type="button" class="filter-tab-btn active" data-filter="all" onclick="filterProjects('all')">
          Все 10 проектов (10)
        </button>
        <button type="button" class="filter-tab-btn" data-filter="b2c" onclick="filterProjects('b2c')">
          Частные резиденции и пентхаусы (5)
        </button>
        <button type="button" class="filter-tab-btn" data-filter="villa" onclick="filterProjects('villa')">
          Загородные виллы и высота до 10м (3)
        </button>
        <button type="button" class="filter-tab-btn" data-filter="b2b" onclick="filterProjects('b2b')">
          Контрактные пространства и B2B (2)
        </button>
      </div>

      <!-- Folio Jump Nav -->
      <nav class="folio-jump-nav" aria-label="Быстрый переход по проектам">
        {jump_links_str}
      </nav>

      <!-- Monograph Cards Container -->
      <div class="monograph-cards-list" id="monographCardsList">
        {all_cards_str}
      </div>
    </div>
  </section>

  <!-- ========================================================================
       4. BEFORE / AFTER DEDICATED ARCHITECTURAL COMPARISON (TACTILE SLIDER)
       ======================================================================== -->
  <section class="section-ba-master" id="beforeAfter">
    <div class="monograph-container">
      <div class="section-head-center">
        <span class="section-kicker-center">ВИЗУАЛЬНАЯ ТРАНСФОРМАЦИЯ</span>
        <h2 class="section-title-monograph">
          Преображение пространства · <em>До и После</em>
        </h2>
        <p class="section-subtitle">
          Перемещайте бегунок, чтобы увидеть, как текстильная архитектура MUAR A меняет акустику, геометрию окон и световой сценарий помещения.
        </p>
      </div>

      <!-- Scene Switcher Tabs (5 Key Projects) -->
      <div class="ba-tabs-nav">
        <button type="button" class="ba-tab-btn active" onclick="switchBaScene(1, this)">01. Red &amp; White (Резиденция)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(2, this)">02. ЖК Vivaldi (Панорамный Dimout)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(3, this)">03. Загородный дом (Римский тюль)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(7, this)">07. Вилла «Темный Рыцарь» (10-метровый холл)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(9, this)">09. Спальня (Коррекция асимметрии окна)</button>
      </div>

      <div class="ba-stage-card">
        <div class="ba-slider-hero" id="baHeroSlider">
          <div class="ba-slider-container muar-ba-container" id="baDedicatedSlider" role="slider" tabindex="0" aria-label="Интерактивное сравнение До и После" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">
            <div class="ba-after-layer muar-ba-layer muar-ba-after">
              <img id="baHeroImgAfter" src="assets/muar/portfolio/garden-14.webp" alt="После текстильного оформления" draggable="false">
            </div>
            <div class="ba-before-layer muar-ba-layer muar-ba-before" id="baHeroBeforeLayer">
              <img id="baHeroImgBefore" src="assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp" alt="До текстильного оформления" draggable="false">
            </div>
            <div class="ba-handle-line muar-ba-divider" id="baHeroHandleLine">
              <div class="ba-handle-grip muar-ba-grip" tabindex="0" role="slider" aria-label="Разделитель До и После">
                <svg class="muar-ba-arrows-svg" viewBox="0 0 24 24" width="22" height="22">
                  <path d="M8.5 7.5L4 12l4.5 4.5M15.5 7.5L20 12l-4.5 4.5" stroke="#1A150B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                </svg>
              </div>
            </div>
            <div class="ba-tag ba-tag-before muar-ba-badge muar-ba-badge-before" id="baHeroLabelBefore">
              <span class="muar-ba-badge-dot"></span>
              <span id="baHeroLabelBeforeText">Интерьер до текстиля</span>
            </div>
            <div class="ba-tag ba-tag-after muar-ba-badge muar-ba-badge-after" id="baHeroLabelAfter">
              <span class="muar-ba-badge-dot"></span>
              <span id="baHeroLabelAfterText">Кутюрное преображение MUAR A</span>
            </div>
          </div>
        </div>
        <div class="ba-card-caption">
          <div class="ba-caption-text">
            <h4 id="baHeroCaptionTitle">Проект 01: Драматургия Red &amp; White (Частная резиденция)</h4>
            <p id="baHeroCaptionDesc">Черновой интерьер vs законченный кутюрный шик: портьеры на светозащитной подкладке, авторская вставка с птицами и стёганое покрывало.</p>
          </div>
          <a href="https://wa.me/77710551515?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C%20MUAR%20A!%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%20%D0%BF%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%8C%D0%B5%D1%80%D0%B0." 
             target="_blank" rel="noopener" class="btn-noir-gold" style="padding: 10px 22px; font-size: 0.84rem;">
            Заказать выезд декоратора
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       5. QUALITY SEALS & ARCHITECTURAL GUILD (ЕАЭС, ТОП-30 СНГ, 6 КОЛЛАБОРАЦИЙ)
       ======================================================================== -->
  <section class="section-quality-marks" id="qualityMarks">
    <div class="monograph-container">
      <div class="section-head-center">
        <span class="section-kicker-center">ГОСУДАРСТВЕННЫЙ СТАНДАРТ И МЕЖДУНАРОДНЫЙ СТАТУС</span>
        <h2 class="section-title-monograph">
          Знаки качества &amp; <em>Архитектурная гильдия</em>
        </h2>
        <p class="section-subtitle">
          Официальная сертификация соответствия нормам ЕАЭС и ГОСТ РК, признание в Топ-30 текстильных декораторов СНГ и почетный реестр золотых плакеток коллабораций с ведущими архитекторами столицы.
        </p>
      </div>

      <!-- Two Monumental Honor Cards: EAEU & Top-30 CIS -->
      <div class="quality-showcase-grid">
        <!-- 1. EAEU Certificate -->
        <article class="quality-honor-card">
          <div class="honor-media-frame" onclick="openCertModal('assets/muar/certificate_eaeu.webp', 'Государственный сертификат соответствия нормам ЕАЭС и ГОСТ РК — ТОО «KazTextileА» / MUAR A')">
            <img src="assets/muar/certificate_eaeu.webp" alt="Сертификат соответствия ЕАЭС MUAR A" class="honor-media-img" loading="lazy">
            <span class="honor-zoom-hint">Клик для зума</span>
          </div>
          <div class="honor-body">
            <span class="honor-badge-pill">ГОСТ РК · ЕАЭС СЕРТИФИКАЦИЯ</span>
            <h3 class="honor-card-title">Золотая печать соответствия ЕАЭС</h3>
            <p class="honor-card-desc">
              Официальное государственное свидетельство безопасности и соответствия нормам Евразийского Экономического Союза (ТР ТС 017/2011). Собственный цех в Астане без надомниц, 12 точек контроля качества ОТК.
            </p>
            <ul class="honor-meta-list">
              <li><span class="gold-bullet">✦</span> <strong>Регламент ЕАЭС:</strong> Полное отсутствие вредных химических испарений и формальдегидов</li>
              <li><span class="gold-bullet">✦</span> <strong>Класс негорючести:</strong> Контрактный европейский текстиль Trevira CS (класс КМ1)</li>
              <li><span class="gold-bullet">✦</span> <strong>Детская безопасность:</strong> Гипоаллергенные натуральные волокна для детских комнат</li>
              <li><span class="gold-bullet">✦</span> <strong>B2B документация:</strong> ЭСФ, накладные, сертификаты и паспорта объектов с НДС 12%</li>
            </ul>
          </div>
        </article>

        <!-- 2. Golden O CIS Top-30 Award -->
        <article class="quality-honor-card">
          <div class="honor-media-frame" onclick="openCertModal('assets/muar/golden_o_award.webp', 'Официальный диплом международной премии Golden O: Топ-30 текстильных декораторов СНГ')">
            <img src="assets/muar/golden_o_award.webp" alt="Диплом Топ-30 текстильных декораторов СНГ Golden O" class="honor-media-img" loading="lazy">
            <span class="honor-zoom-hint">Клик для зума</span>
          </div>
          <div class="honor-body">
            <span class="honor-badge-pill">ПРЕМИЯ GOLDEN O · СНГ СТАТУС</span>
            <h3 class="honor-card-title">Топ-30 текстильных декораторов СНГ</h3>
            <p class="honor-card-desc">
              Международное признание авторского почерка основателя дома MUAR A Асенгуль. Включение в элитный закрытый рейтинг 30 лучших текстильных декораторов Содружества Независимых Государств.
            </p>
            <ul class="honor-meta-list">
              <li><span class="gold-bullet">✦</span> <strong>12 лет опыта:</strong> Свыше 1 200 оформленных приватных резиденций и вилл</li>
              <li><span class="gold-bullet">✦</span> <strong>Европейские фабрики:</strong> Прямые поставки шелков, бархата и жаккардов из Италии и Франции</li>
              <li><span class="gold-bullet">✦</span> <strong>Сложная инженерия:</strong> Проектирование лифт-систем для окон высотой до 10 метров</li>
              <li><span class="gold-bullet">✦</span> <strong>Кутюрный цех:</strong> Французская ручная складка и нити Gütermann Mara 120</li>
            </ul>
          </div>
        </article>
      </div>

      <!-- 6 Golden Collaboration Plaques Grid -->
      <div style="margin-top: 60px; margin-bottom: 24px; text-align: center;">
        <span class="section-kicker-center">АРХИТЕКТУРНЫЙ СОЮЗ СТОЛИЦЫ</span>
        <h3 style="font-family: var(--font-serif); font-size: 2rem; color: var(--text-noir); font-weight: 600;">
          Почетный реестр <em>6 золотых плакеток</em> коллабораций
        </h3>
      </div>

      <div class="guild-plaques-grid">
        <!-- 1. IDesign -->
        <div class="guild-plaque-item">
          <div class="guild-plaque-header">
            <div class="guild-crest-mini">ID</div>
            <div>
              <h4 class="guild-arch-name">IDesign Studio</h4>
              <span class="guild-arch-role">Архитектура &amp; Дизайн интерьера</span>
            </div>
          </div>
          <div class="guild-project-title">ЖК Vivaldi (Пентхаус с панорамными окнами)</div>
          <p class="guild-project-desc">
            Совместное проектирование светозащитного сценария Dimout для южных витражей, скрытые моторизованные карнизы Somfy и покрывала со спецподкладкой.
          </p>
          <a href="#folio-02" class="guild-project-link">
            Смотреть Folio № 02 <span>→</span>
          </a>
        </div>

        <!-- 2. Зарина Секен -->
        <div class="guild-plaque-item">
          <div class="guild-plaque-header">
            <div class="guild-crest-mini">ЗС</div>
            <div>
              <h4 class="guild-arch-name">Зарина Секен</h4>
              <span class="guild-arch-role">Дизайнер премиальных интерьеров</span>
            </div>
          </div>
          <div class="guild-project-title">Загородная резиденция (Колористика &amp; Орнаменты)</div>
          <p class="guild-project-desc">
            Текстильный размах резиденции «под ключ»: басонные декоративные канты, прозрачный римский тюль и авторские геометрические валики.
          </p>
          <a href="#folio-03" class="guild-project-link">
            Смотреть Folio № 03 <span>→</span>
          </a>
        </div>

        <!-- 3. Габиден -->
        <div class="guild-plaque-item">
          <div class="guild-plaque-header">
            <div class="guild-crest-mini">ГБ</div>
            <div>
              <h4 class="guild-arch-name">Архитектор Габиден</h4>
              <span class="guild-arch-role">Архитектор элитных вилл</span>
            </div>
          </div>
          <div class="guild-project-title">Виллы «Темный Рыцарь» (Потолки 10 метров)</div>
          <p class="guild-project-desc">
            Проектирование и монтаж высотной лифт-системы на стальных тросах с трубчатыми моторами. Портьеры из плотного сатина на светозащитной подкладке.
          </p>
          <a href="#folio-07" class="guild-project-link">
            Смотреть Folio № 07 <span>→</span>
          </a>
        </div>

        <!-- 4. Динара Усманова -->
        <div class="guild-plaque-item">
          <div class="guild-plaque-header">
            <div class="guild-crest-mini">ДУ</div>
            <div>
              <h4 class="guild-arch-name">Динара Усманова</h4>
              <span class="guild-arch-role">Дизайнер интерьера</span>
            </div>
          </div>
          <div class="guild-project-title">Загородный дом (Стиль модерн 60-х)</div>
          <p class="guild-project-desc">
            Создание штучного крафтового изделия: ручная роспись геометрического орнамента, шелковый кант и акценты нитями мулине.
          </p>
          <a href="#folio-06" class="guild-project-link">
            Смотреть Folio № 06 <span>→</span>
          </a>
        </div>

        <!-- 5. Лаура Жакина -->
        <div class="guild-plaque-item">
          <div class="guild-plaque-header">
            <div class="guild-crest-mini">ЛЖ</div>
            <div>
              <h4 class="guild-arch-name">Лаура Жакина</h4>
              <span class="guild-arch-role">Дизайнер интерьера</span>
            </div>
          </div>
          <div class="guild-project-title">VIP-Апартаменты (Бордо &amp; Пайетки)</div>
          <p class="guild-project-desc">
            Драматургия глубокого бордо: барельефный подхват-роза ручной работы, стеганое покрывало с изножьем в пайетках и подушки из шерсти и сатина.
          </p>
          <a href="#folio-08" class="guild-project-link">
            Смотреть Folio № 08 <span>→</span>
          </a>
        </div>

        <!-- 6. Руслан -->
        <div class="guild-plaque-item">
          <div class="guild-plaque-header">
            <div class="guild-crest-mini">РС</div>
            <div>
              <h4 class="guild-arch-name">Дизайнер Руслан</h4>
              <span class="guild-arch-role">Архитектура общественных пространств</span>
            </div>
          </div>
          <div class="guild-project-title">Премиальный ресторан (Потолочные паруса)</div>
          <p class="guild-project-desc">
            Монтаж профилей длиной свыше 4 метров, ювелирный расчет естественного растяжения ткани, игра света и неповторимая асимметрия волн.
          </p>
          <a href="#folio-05" class="guild-project-link">
            Смотреть Folio № 05 <span>→</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       5. ATELIER & ENGINEERING SHOWCASE (NOCTURNE CINEMA THEATER & 10M SYSTEMS)
       ======================================================================== -->
  <section class="section-atelier-nocturne" id="atelier">
    <div class="monograph-container">
      <div class="atelier-head">
        <span class="atelier-kicker">СОБСТВЕННОЕ ПРОИЗВОДСТВО В АСТАНЕ · EST. 2014</span>
        <h2 class="atelier-title">
          Ателье высшей категории & <em>Инженерия высоких потолков</em>
        </h2>
        <p class="atelier-desc">
          Полный отказ от надомниц и субподряда. Собственный швейный цех с профессиональным оборудованием Juki и Dürkopp Adler. Проектирование лифт-систем на стальных тросах для высоты до 10 метров в виллах и резиденциях столицы.
        </p>
      </div>

      <!-- Video Exhibits Theater -->
      <div class="videos-grid-theater">
        <!-- Exhibit 01: Master Maral -->
        <article class="video-exhibit-card">
          <div class="video-thumb-container" onclick="openCinemaModal('assets/muar/craft-maral.mp4', 'Экспонат 01: Мастер Марал — ручная кутюрная складка и нити Gütermann')">
            <img src="assets/muar/craft-maral-poster.jpg" alt="Мастер Марал швейный цех MUAR A" class="video-thumb-img" onerror="this.src='assets/muar/craft-maral.webp'">
            <div class="video-play-halo">
              <div class="play-btn-gold">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="5 3 19 12 5 21 5 3"/>
                </svg>
              </div>
            </div>
            <span class="video-duration-chip">01:10</span>
          </div>
          <div class="video-card-body">
            <span class="video-card-kicker">ЭКСПОНАТ 01 · МАСТЕРСТВО</span>
            <h3 class="video-card-title">Мастер Марал: 25 лет стажа</h3>
            <p class="video-card-text">
              Французская тройная ручная складка 1:2.0. Потайной нижний подгиб 10 см с закрытым стежком Blindstitch и армированными немецкими нитями Gütermann Mara 120.
            </p>
            <button type="button" class="btn-outline-gold" onclick="openCinemaModal('assets/muar/craft-maral.mp4', 'Мастер Марал — ручная кутюрная складка')">
              Смотреть фильм (01:10)
            </button>
          </div>
        </article>

        <!-- Exhibit 02: 10m Villa Lift System -->
        <article class="video-exhibit-card">
          <div class="video-thumb-container" onclick="openCinemaModal('assets/muar/villa-lift-system.mp4', 'Экспонат 02: Лифт-система 10 метров — Виллы «Темный Рыцарь»')">
            <img src="assets/muar/villa-lift-poster.jpg" alt="Монтаж лифт-системы 10 метров виллы Темный Рыцарь" class="video-thumb-img" onerror="this.src='assets/muar/portfolio/IMG_6721.webp'">
            <div class="video-play-halo">
              <div class="play-btn-gold">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="5 3 19 12 5 21 5 3"/>
                </svg>
              </div>
            </div>
            <span class="video-duration-chip">00:10</span>
          </div>
          <div class="video-card-body">
            <span class="video-card-kicker">ЭКСПОНАТ 02 · ИНЖЕНЕРИЯ</span>
            <h3 class="video-card-title">Лифт-системы для окон 10 метров</h3>
            <p class="video-card-text">
              Монтаж специальной моторизованной лифт-системы со стальными тросами и трубчатыми моторами в виллах «Темный Рыцарь» для легкого обслуживания без лесов.
            </p>
            <button type="button" class="btn-outline-gold" onclick="openCinemaModal('assets/muar/villa-lift-system.mp4', 'Лифт-система 10 метров — Виллы Темный Рыцарь')">
              Смотреть фильм (00:10)
            </button>
          </div>
        </article>

        <!-- Exhibit 03: Order Journey -->
        <article class="video-exhibit-card">
          <div class="video-thumb-container" onclick="openCinemaModal('assets/muar/order-journey.mp4', 'Экспонат 03: Путь заказа под ключ — от замера до отпаривания')">
            <img src="assets/muar/order-journey-poster.jpg" alt="Путь заказа штор под ключ MUAR A" class="video-thumb-img" onerror="this.src='assets/muar/portfolio/garden-14.webp'">
            <div class="video-play-halo">
              <div class="play-btn-gold">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="5 3 19 12 5 21 5 3"/>
                </svg>
              </div>
            </div>
            <span class="video-duration-chip">01:31</span>
          </div>
          <div class="video-card-body">
            <span class="video-card-kicker">ЭКСПОНАТ 03 · РЕГЛАМЕНТ</span>
            <h3 class="video-card-title">Путь заказа под ключ</h3>
            <p class="video-card-text">
              Лазерный замер, текстильный сценарий декоратора, паровая декатировка полотен при 140°C ДО раскроя, навеска и вертикальное отпаривание парогенератором 4.5 Bar.
            </p>
            <button type="button" class="btn-outline-gold" onclick="openCinemaModal('assets/muar/order-journey.mp4', 'Путь заказа текстиля под ключ')">
              Смотреть фильм (01:31)
            </button>
          </div>
        </article>
      </div>

      <!-- 6 Pillars of Quality -->
      <div class="pillars-grid">
        <div class="pillar-card">
          <div class="pillar-num">I</div>
          <h4 class="pillar-title">Собственный цех без надомниц</h4>
          <p class="pillar-text">
            100% контроль каждого сантиметра. 12 контрольных точек ОТК, пошив строго по ГОСТам РК.
          </p>
        </div>
        <div class="pillar-card">
          <div class="pillar-num">II</div>
          <h4 class="pillar-title">Немецкие нити Gütermann</h4>
          <p class="pillar-text">
            Армированные полиэфирные нити Mara 120. Потайной шов с глубиной подгибки 10 см держит безупречную геометрию.
          </p>
        </div>
        <div class="pillar-card">
          <div class="pillar-num">III</div>
          <h4 class="pillar-title">Декатировка паром до пошива</h4>
          <p class="pillar-text">
            Глубокая термоусадка итальянским парогенератором 140°C при 4.5 Bar ДО раскроя. Изделия гарантированно не сядут.
          </p>
        </div>
        <div class="pillar-card">
          <div class="pillar-num">IV</div>
          <h4 class="pillar-title">Высотные лифт-системы до 10м</h4>
          <p class="pillar-text">
            Усиленные электрокарнизы Somfy / Dooya, проектирование систем на стальных тросах для загородных резиденций.
          </p>
        </div>
        <div class="pillar-card">
          <div class="pillar-num">V</div>
          <h4 class="pillar-title">2 этажа коллекций со всего мира</h4>
          <p class="pillar-text">
            7 000+ образцов тканей из Италии, Испании, Бельгии и Франции по прямым фабричным контрактам в салоне Астаны.
          </p>
        </div>
        <div class="pillar-card">
          <div class="pillar-num">VI</div>
          <h4 class="pillar-title">B2B отдел с НДС 12%</h4>
          <p class="pillar-text">
            Официальный контрактный текстиль Trevira CS (класс КМ1), полный пакет ЭСФ, акты выполненных работ, паспорта объектов.
          </p>
        </div>
      </div>

      <!-- Duo Profiles -->
      <div class="profiles-grid">
        <div class="profile-card">
          <img src="assets/muar/strength-2-award.webp" alt="Асенгуль — основатель MUAR A" class="profile-photo">
          <div>
            <span class="profile-role">Основатель & Ведущий Декоратор</span>
            <h3 class="profile-name">Асенгуль</h3>
            <p class="profile-bio">
              Топ-30 текстильных декораторов СНГ. Лауреат профессиональной премии Golden O. 12+ лет оформления резиденций и дипломатических объектов столицы.
            </p>
            <a href="https://wa.me/77710551515?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C%20%D0%90%D1%81%D0%B5%D0%BD%D0%B3%D1%83%D0%BB%D1%8C!%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%BE%D0%B1%D1%81%D1%83%D0%B4%D0%B8%D1%82%D1%8C%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82." 
               target="_blank" rel="noopener" class="btn-gold-satin" style="padding: 10px 18px; font-size: 0.82rem;">
              Написать Асенгуль в WhatsApp
            </a>
          </div>
        </div>

        <div class="profile-card">
          <img src="assets/muar/craft-maral.webp" alt="Мастер Марал — главный технолог цеха MUAR A" class="profile-photo">
          <div>
            <span class="profile-role">Главный Технолог Производства</span>
            <h3 class="profile-name">Мастер Марал</h3>
            <p class="profile-bio">
              25 лет непрерывного стажа в швейном искусстве высшей категории. Более 14 000 безупречно сшитых портьер, филигранная подгонка раппорта жаккардов с точностью до 1 мм.
            </p>
            <button type="button" class="btn-outline-gold" onclick="openCinemaModal('assets/muar/craft-maral.mp4', 'Мастер Марал в цехе MUAR A')" style="padding: 10px 18px; font-size: 0.82rem;">
              Смотреть работу мастера
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       6. EXACT ASENGUL CALCULATION SECTION (ALABASTER & BRASS QUIET LUXURY)
       ======================================================================== -->
  <section class="section-calc-master" id="calculator">
    {calc_html}
  </section>

  <!-- ========================================================================
       7. CONTACTS & VIP SALON APPOINTMENT
       ======================================================================== -->
  <section class="section-monograph" id="contacts" style="background: #F4EFEB; border-top: 1px solid rgba(197, 160, 105, 0.25);">
    <div class="monograph-container">
      <div class="monograph-card" style="padding: 56px; border-color: rgba(197, 160, 105, 0.45);">
        <div class="monograph-grid" style="align-items: center;">
          <div>
            <span class="folio-badge" style="margin-bottom: 16px; display: inline-block;">ФЛАГМАНСКИЙ САЛОН MUAR A В АСТАНЕ</span>
            <h2 class="monograph-title" style="font-size: 2.6rem;">
              Приглашаем в мир <em>высокого текстиля</em>
            </h2>
            <p class="monograph-narrative">
              2 этажа экспозиции европейского текстиля, образцы карнизов с электроприводами Somfy, живые выкрасы и фактуры. За чашкой кофе ведущий декоратор Асенгуль сформирует персональный текстильный сценарий для вашего дома.
            </p>
            <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 28px;">
              <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--text-noir);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C5A069" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                г. Астана, ул. Керей, Жәнибек хандар, 50/1, ВП 18
              </div>
              <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--text-noir);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C5A069" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/>
                  <polyline points="12 6 12 12 16 14"/>
                </svg>
                Понедельник — Суббота: 10:00 – 19:00 (по предварительной записи)
              </div>
              <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--text-noir);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C5A069" stroke-width="2">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                </svg>
                +7 771 055 15 15 (Прямой контакт декоратора)
              </div>
            </div>
            <div class="monograph-actions">
              <a href="https://wa.me/77710551515?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C%20%D1%85%D0%BE%D1%87%D1%83%20%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C%D1%81%D1%8F%20%D0%BD%D0%B0%20%D0%BA%D0%BE%D0%BD%D1%81%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%86%D0%B8%D1%8E%20%D0%B2%20%D1%81%D0%B0%D0%BB%D0%BE%D0%BD%20MUAR%20A." 
                 target="_blank" rel="noopener" class="btn-noir-gold">
                Написать в WhatsApp
              </a>
              <a href="https://2gis.kz/astana/search/%D0%9A%D0%B5%D1%80%D0%B5%D0%B9%2C%20%D0%96%D3%99%D0%BD%D1%96%D0%B1%D0%B5%D0%BA%20%D1%85%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%2C%2050%2F1" 
                 target="_blank" rel="noopener" class="btn-outline-gold">
                Маршрут в 2GIS
              </a>
            </div>
          </div>
          <div>
            <div style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-card); border: 1px solid rgba(197, 160, 105, 0.35);">
              <img src="assets/muar/strength-1-floors.webp" alt="Салон текстиля MUAR A Астана" style="width: 100%; height: 380px; object-fit: cover;" onerror="this.src='assets/muar/hero-interior.webp'">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       8. MASTER FOOTER
       ======================================================================== -->
  <footer class="master-footer">
    <div class="footer-container">
      <div class="footer-top-grid">
        <div>
          <div class="footer-brand-title">MUAR A</div>
          <p class="footer-brand-desc">
            Флагманский салон интерьерного текстиля, моторизованных карнизов и архитектурной солнцезащиты в Астане с 2014 года. Собственный швейный цех по ГОСТам РК.
          </p>
          <div style="font-family: var(--font-mono); font-size: 0.78rem; color: var(--gold-light);">
            ТОО «KazTextileА» · БИН / НДС 12% · Астана
          </div>
        </div>

        <div>
          <h4 class="footer-col-title">Навигация</h4>
          <ul class="footer-list">
            <li><a href="#monograph">10 Архитектурных проектов</a></li>
            <li><a href="#beforeAfter">Интерактивное До / После</a></li>
            <li><a href="#atelier">Швейный цех и Мастер Марал</a></li>
            <li><a href="#atelier">Лифт-системы 10 метров</a></li>
            <li><a href="#calculator">Калькулятор Асенгуль (508 800 ₸)</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer-col-title">Контакты</h4>
          <ul class="footer-list">
            <li>Астана, ул. Керей, Жәнибек хандар, 50/1</li>
            <li><a href="tel:+77710551515">+7 771 055 15 15</a></li>
            <li><a href="https://wa.me/77710551515" target="_blank" rel="noopener">WhatsApp Декоратора</a></li>
            <li><a href="https://instagram.com/muar.a" target="_blank" rel="noopener">Instagram: @muar.a</a></li>
            <li>Пн–Сб 10:00–19:00</li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>© 2014–2026 MUAR A · Салон интерьерного текстиля. Все права защищены.</div>
        <div>Астана · Алматы · Проекты по всему Казахстану</div>
      </div>
    </div>
  </footer>

  <!-- ========================================================================
       9. MASTER CINEMA MODAL (SOUND-SAFE ATELIER VIDEO THEATER)
       ======================================================================== -->
  <!-- ========================================================================
       CERTIFICATE & AWARD FULLSCREEN LIGHTBOX MODAL
       ======================================================================== -->
  <div class="cert-modal" id="certModal" onclick="closeCertModal(event)">
    <div class="cert-modal-box" onclick="event.stopPropagation()">
      <div class="cert-modal-header">
        <h3 class="cert-modal-title" id="certModalTitle">Официальный знак качества MUAR A</h3>
        <button type="button" class="cert-close-btn" onclick="closeCertModal()" title="Закрыть">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>
      <div class="cert-image-wrap">
        <img id="certModalImg" src="" alt="Официальный документ MUAR A" class="cert-modal-img">
      </div>
    </div>
  </div>

  <div class="cinema-modal" id="cinemaModal" onclick="closeCinemaModal(event)">
    <div class="cinema-modal-box" onclick="event.stopPropagation()">
      <div class="cinema-modal-header">
        <h3 class="cinema-title" id="cinemaTitle">Экспонат ателье MUAR A</h3>
        <button type="button" class="cinema-close-btn" onclick="closeCinemaModal()" title="Закрыть">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>
      <div class="cinema-video-wrap">
        <video class="cinema-video-player" id="cinemaVideo" controls playsinline preload="auto"></video>
      </div>
    </div>
  </div>

  <!-- Audio Element for Ambient Lounge -->
  <audio id="ambientAudio" loop preload="none">
    <source src="assets/muar/ambient-lounge.mp3" type="audio/mpeg">
  </audio>

  <!-- ========================================================================
       10. SCRIPTS & LOGIC
       ======================================================================== -->
  <script>
    // Global Projects Dataset from Asengul
    window.MUAR_PROJECTS = {projects_json};
    window.BA_SCENES = {ba_scenes_json};
  </script>

  <!-- Core Interactive Engine (Before/After Slider, Lightbox, Audio) -->
  <script>
{interactive_engine_js}
  </script>

  <!-- Precision Calculator Engine (100% Asengul Math & Alabaster UI) -->
  <script>
{calculator_engine_js}
  </script>

  <script>
{calc_controller_js}
  </script>

  <!-- Master Page Orchestration Script -->
  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      // 1. Initialize Ambient Soundscape
      window.muarSoundscape = new window.MuarInteractive.MuarAmbientSoundscape({{
        audioSrc: 'assets/muar/ambient-lounge.mp3'
      }});

      // 2. Initialize Master Lightbox
      window.muarLightbox = new window.MuarInteractive.MuarLightbox({{
        projectsData: window.MUAR_PROJECTS
      }});

      // 3. Initialize Before/After Slider
      const baContainer = document.getElementById('baDedicatedSlider');
      if (baContainer) {{
        window.muarBeforeAfter = new window.MuarInteractive.MuarBeforeAfterSlider(baContainer, {{
          initialPosition: 50,
          soundEngine: window.muarSoundscape
        }});
      }}

      // 4. Scroll Header styling
      const header = document.getElementById('masterHeader');
      window.addEventListener('scroll', function () {{
        if (window.scrollY > 40) {{
          header.classList.add('scrolled');
        }} else {{
          header.classList.remove('scrolled');
        }}
      }}, {{ passive: true }});
    }});

    // Category Filtering for Monograph Cards
    function filterProjects(cat) {{
      const buttons = document.querySelectorAll('.filter-tab-btn');
      buttons.forEach(btn => {{
        if (btn.getAttribute('data-filter') === cat) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});

      const cards = document.querySelectorAll('.monograph-card');
      cards.forEach(card => {{
        const cardCat = card.getAttribute('data-cat');
        if (cat === 'all' || cardCat === cat) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});

      if (window.muarSoundscape) {{
        window.muarSoundscape.playTactile('brass-click');
      }}
    }}

    // Before/After Scene Switcher
    function switchBaScene(sceneId, btn) {{
      document.querySelectorAll('.ba-tab-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) {{
        btn.classList.add('active');
      }} else {{
        const targetBtn = document.querySelector('.ba-tab-btn[onclick*="switchBaScene(' + sceneId + '"]');
        if (targetBtn) targetBtn.classList.add('active');
      }}

      const sc = window.BA_SCENES[sceneId] || window.BA_SCENES[1];
      const imgBefore = document.getElementById('baHeroImgBefore');
      const imgAfter = document.getElementById('baHeroImgAfter');
      if (imgBefore) imgBefore.src = sc.before;
      if (imgAfter) imgAfter.src = sc.after;

      const lblB = document.getElementById('baHeroLabelBeforeText');
      const lblA = document.getElementById('baHeroLabelAfterText');
      if (lblB) lblB.textContent = sc.labelBefore;
      if (lblA) lblA.textContent = sc.labelAfter;

      const capTitle = document.getElementById('baHeroCaptionTitle');
      const capDesc = document.getElementById('baHeroCaptionDesc');
      if (capTitle) capTitle.textContent = sc.title;
      if (capDesc) capDesc.textContent = sc.desc;

      if (window.muarBeforeAfter) {{
        window.muarBeforeAfter.setPercentage(50, false);
      }}

      if (window.muarSoundscape) {{
        window.muarSoundscape.playTactile('brass-click');
      }}
    }}

    // Lightbox Helper
    function openProjectLightbox(projectId, photoIndex) {{
      if (window.muarLightbox) {{
        window.muarLightbox.open(projectId, photoIndex);
      }}
    }}

    // Certificate Lightbox Modal Logic
    function openCertModal(imageSrc, title) {{
      const modal = document.getElementById('certModal');
      const img = document.getElementById('certModalImg');
      const titleEl = document.getElementById('certModalTitle');

      if (titleEl) titleEl.textContent = title || 'Официальный знак качества MUAR A';
      if (img) img.src = imageSrc;
      if (modal) modal.classList.add('active');

      if (window.muarSoundscape) {{
        window.muarSoundscape.playTactile('brass-click');
      }}
    }}

    function closeCertModal(e) {{
      if (e && e.target !== e.currentTarget && !e.target.closest('.cert-close-btn')) return;
      const modal = document.getElementById('certModal');
      if (modal) modal.classList.remove('active');
    }}

    // Cinema Video Modal Logic
    function openCinemaModal(videoSrc, title) {{
      const modal = document.getElementById('cinemaModal');
      const video = document.getElementById('cinemaVideo');
      const titleEl = document.getElementById('cinemaTitle');

      if (titleEl) titleEl.textContent = title || 'Экспонат ателье MUAR A';
      if (video) {{
        video.src = videoSrc;
        video.play().catch(() => {{}});
      }}
      if (modal) modal.classList.add('active');

      // Pause ambient sound while watching video
      if (window.muarSoundscape && window.muarSoundscape.isPlaying) {{
        window.muarSoundscape.fadeOut();
      }}
    }}

    function closeCinemaModal(e) {{
      if (e && e.target !== e.currentTarget && !e.target.closest('.cinema-close-btn')) return;
      const modal = document.getElementById('cinemaModal');
      const video = document.getElementById('cinemaVideo');

      if (video) {{
        video.pause();
        video.removeAttribute('src');
        video.load();
      }}
      if (modal) modal.classList.remove('active');
    }}

    // Keyboard ESC to close Cinema Modal
    document.addEventListener('keydown', function (e) {{
      if (e.key === 'Escape') {{
        const modal = document.getElementById('cinemaModal');
        if (modal && modal.classList.contains('active')) {{
          closeCinemaModal();
        }}
        const certModal = document.getElementById('certModal');
        if (certModal && certModal.classList.contains('active')) {{
          closeCertModal();
        }}
      }}
    }});
  </script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    content = build_solid_luxury_site()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    with open('dist/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Solid luxury index.html & dist/index.html generated successfully!")
