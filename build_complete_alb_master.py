#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Synthesis Builder (Subagent 10)
Merges all 9 delivered subagent modules into a single, cohesive, production-ready
master index.html in the Anthony Lawrence-Belfair NYC Workroom aesthetic.
"""

import os
import re
import json
import urllib.parse

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
        "badge": "АВТОРСКИЙ ПРОЕКТ СПАЛЬНИ",
        "name": "MUAR A Interior Team",
        "role": "Яркая спальня · Глубокий винный бархат, тесьма с пайетками"
    },
    9: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Дизайнер Лаура Жакина",
        "role": "Мастер-спальня · Коррекция асимметрии окна, Римская штора & Тюль омбре"
    },
    10: {
        "badge": "ЗОЛОТАЯ ПЛАКЕТКА КОЛЛАБОРАЦИИ",
        "name": "Архитектор Динара",
        "role": "Спальня-ансамбль · Римские шторы с помпонами, гардеробные портьеры"
    }
}

BA_SCENES = {
    1: {
        "title": "Проект 01: Драматургия Red & White (Частная резиденция)",
        "desc": "Черновой интерьер vs законченный кутюрный шик: портьеры на светозащитной подкладке, авторская вставка с птицами и стёганое покрывало.",
        "before": "assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp",
        "after": "assets/muar/portfolio/garden-14.webp",
        "labelBefore": "Интерьер до текстиля",
        "labelAfter": "Кутюрное преображение MUAR A"
    },
    2: {
        "title": "Проект 02: ЖК Vivaldi (Панорамные окна & Somfy)",
        "desc": "Голые стекла и эхо в пентхаусе vs мягкий рассеивающий Dimout, акустический комфорт и скрытый монтаж моторизованных карнизов.",
        "before": "assets/muar/portfolio/photo_11@29-09-2026_17-02-56.webp",
        "after": "assets/muar/portfolio/garden-20.webp",
        "labelBefore": "Бетонное эхо и блики",
        "labelAfter": "Рассеивающий Dimout & Somfy"
    },
    3: {
        "title": "Проект 03: Загородная резиденция (Римский тюль Зарины Секен)",
        "desc": "Строгая геометрия эркеров vs легкий прозрачный римский тюль с басонным кантом ручной работы и тяжелыми портьерами в пол.",
        "before": "assets/muar/portfolio/photo_14@29-09-2026_17-02-56.webp",
        "after": "assets/muar/portfolio/garden-22.webp",
        "labelBefore": "Окна до текстильного решения",
        "labelAfter": "Римский тюль и басонный кант"
    },
    7: {
        "title": "Проект 07: Виллы «Темный Рыцарь» (10-метровый второй свет)",
        "desc": "Пустой 10-метровый витраж vs моторизованная лифт-система на стальных тросах с блэкаутом для виллы в стиле Бэтмена.",
        "before": "assets/muar/portfolio/IMG_6721.webp",
        "after": "assets/muar/portfolio/IMG_6722.webp",
        "labelBefore": "Пустой витраж высотой 10 метров",
        "labelAfter": "Лифт-система & Моторизованный блэкаут"
    },
    9: {
        "title": "Проект 09: Спальня — Коррекция асимметрии окна (Лаура Жакина)",
        "desc": "Смещенный оконный проем и визуальный диссонанс vs изящная римская штора с льняным тюлем омбре, визуально выровнявшие стену спальни.",
        "before": "assets/muar/portfolio/project_09_before.webp",
        "after": "assets/muar/portfolio/project_09_after.webp",
        "labelBefore": "Асимметрия и темная портьера",
        "labelAfter": "Римская штора & Льняной тюль омбре"
    }
}

def extract_module(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    styles = re.findall(r'<style[^>]*>(.*?)</style>', c, re.DOTALL)
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', c, re.DOTALL)
    if '<body>' in c and '</body>' in c:
        m = re.search(r'<body>(.*?)</body>', c, re.DOTALL)
        body = m.group(1) if m else c
    else:
        body = c.split('</head>')[-1] if '</head>' in c else c
    body_clean = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)
    body_clean = re.sub(r'</?(?:html|body)[^>]*>', '', body_clean)
    return {
        'styles': "\n\n".join(s.strip() for s in styles),
        'scripts': "\n\n".join(s.strip() for s in scripts),
        'body': body_clean.strip()
    }

def build_monograph_cards():
    cards = []
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
        
        wa_text = f"Здравствуйте, Асенгуль! Меня заинтересовал Проект №{p_num} «{p_title}» ({p_loc}). Хочу получить консультацию и рассчитать текстильный сценарий."
        wa_url = f"https://wa.me/77710551515?text={urllib.parse.quote(wa_text)}"

        collab_entry = COLLAB_DATA.get(p_id, {
            "badge": "АРХИТЕКТУРНАЯ КОЛЛАБОРАЦИЯ",
            "name": p_collab,
            "role": "Текстильный сценарий и кутюрный пошив MUAR A"
        })
        collab_badge = collab_entry["badge"]
        collab_name = collab_entry["name"]
        collab_role = collab_entry["role"]

        specs_html = "".join([f'<li class="spec-item"><span class="spec-bullet">✦</span> {s}</li>' for s in p_specs])

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

        card_html = f'''
        <article class="monograph-card" id="folio-{p_num}" data-category="{p_cat}">
          <div class="monograph-grid">
            <div class="monograph-narrative-col">
              <div class="folio-header-meta">
                <span class="folio-num">№ {p_num}</span>
                <span class="folio-cat-badge">{p_cat_name}</span>
                <span class="folio-loc">📍 {p_loc}</span>
              </div>

              <h3 class="monograph-title">{p_title}</h3>

              <div class="architect-guild-plaque">
                <div class="guild-seal">
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                  </svg>
                </div>
                <div>
                  <span class="guild-badge">{collab_badge}</span>
                  <div class="guild-name">{collab_name}</div>
                  <div class="guild-role">{collab_role}</div>
                </div>
              </div>

              <div class="monograph-narrative">
                <p>{p_desc}</p>
              </div>

              <div class="audio-commentary-wrap">
                <div class="audio-wave-anim">
                  <span class="wave-bar"></span>
                  <span class="wave-bar"></span>
                  <span class="wave-bar"></span>
                  <span class="wave-bar"></span>
                </div>
                <div class="audio-commentary-text">
                  <span class="audio-kicker">ГОЛОСОВОЙ АРХИВ АСЕНГУЛЬ (TELEGRAM 2026)</span>
                  <p class="audio-quote">«Мы создаем не просто шторы, а архитектурное завершение ремонта. В этом проекте мы учли падение естественного света и создали идеальный объем складок». — Асенгуль Омарова</p>
                </div>
              </div>

              <div class="monograph-specs">
                <h4 class="specs-title">КУТЮРНЫЕ УЗЛЫ И СПЕЦИФИКАЦИЯ:</h4>
                <ul class="specs-list">
                  {specs_html}
                </ul>
              </div>

              <div class="monograph-actions">
                <a href="{wa_url}" target="_blank" rel="noopener" class="btn-noir-gold">
                  Заказать проект в этом стиле
                </a>
                <button type="button" class="btn-outline-gold" onclick="openProjectLightbox({p_id}, 0)">
                  Смотреть все {photos_count} фото
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
        cards.append(card_html)
    return "\n".join(cards)

def main():
    print("Building Anthony Lawrence-Belfair Master Index...")
    
    with open('alb_design_system.css', 'r', encoding='utf-8') as f:
        alb_css = f.read()
    with open('tactile_interactions.css', 'r', encoding='utf-8') as f:
        tactile_css = f.read()
    with open('scratch/luxury_tokens.css', 'r', encoding='utf-8') as f:
        luxury_tokens_css = f.read()
    with open('scratch/interactive_engine.css', 'r', encoding='utf-8') as f:
        interactive_engine_css = f.read()

    workroom = extract_module('workroom_section.html')
    pathways = extract_module('pathways_section.html')
    credentials = extract_module('credentials_section.html')
    calculator = extract_module('calculator_module.html')

    with open('tactile_interactions.js', 'r', encoding='utf-8') as f:
        tactile_js = f.read()
    with open('scratch/interactive_engine.js', 'r', encoding='utf-8') as f:
        interactive_engine_js = f.read()

    monograph_cards_html = build_monograph_cards()
    projects_json = json.dumps(PROJECTS, ensure_ascii=False)
    ba_scenes_json = json.dumps(BA_SCENES, ensure_ascii=False)

    master_html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>MUAR A · Салон интерьерного текстиля и архитектурной солнцезащиты · Астана</title>
  <meta name="description" content="MUAR A — салон интерьерного текстиля в Астане с 2014 года. 2 этажа коллекций со всего мира, собственное швейное производство без надомниц, лифт-системы до 10 метров. Топ-30 декораторов СНГ (Golden O).">
  <meta name="theme-color" content="#212121">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="MUAR A · Текстильная архитектура и оформление знаковых резиденций">
  <meta property="og:description" content="10 реализованных проектов текстильного дома MUAR A. Виллы с высотой потолков 10м, пентхаусы, кабинеты первых лиц. Подлинные истории создания и расчет сметы.">
  <meta property="og:image" content="assets/muar/portfolio/garden-14.webp">
  <meta property="og:url" content="https://muar-a.pages.dev/">

  <!-- Google Fonts: Cormorant Garamond, Playfair Display, Montserrat, Cinzel, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@300;400;500;600&display=swap" rel="stylesheet">

  <style>
/* 1. ALB NYC DESIGN SYSTEM TOKENS & FOUNDATION */
{alb_css}

/* 2. TACTILE INTERACTIONS STYLES */
{tactile_css}

/* 3. LUXURY BASE TOKENS */
{luxury_tokens_css}

/* 4. INTERACTIVE ENGINE CSS */
{interactive_engine_css}

/* 5. WORKROOM SECTION CSS */
{workroom['styles']}

/* 6. PATHWAYS SECTION CSS */
{pathways['styles']}

/* 7. CREDENTIALS SECTION CSS */
{credentials['styles']}

/* 8. CALCULATOR MODULE CSS */
{calculator['styles']}

/* ==========================================================================
   MASTER INTEGRATOR OVERRIDES & GLUE STYLES (ANTHONY LAWRENCE-BELFAIR NYC)
   ========================================================================== */
:root {{
  --font-serif: var(--alb-font-serif);
  --font-sans: var(--alb-font-sans);
  --font-mono: var(--alb-font-mono);
  --gold-primary: var(--alb-color-brass);
  --noir-deep: var(--alb-color-charcoal);
}}

html {{
  scroll-behavior: smooth;
  scroll-padding-top: 90px;
  background-color: var(--alb-color-linen);
  color: var(--alb-color-charcoal);
  font-family: var(--alb-font-sans);
}}

body {{
  background-color: var(--alb-color-linen);
  color: var(--alb-color-charcoal);
  overflow-x: hidden;
  margin: 0;
}}

/* Monograph & Gallery Styles */
.section-monograph {{
  padding: clamp(70px, 7vw, 110px) 0;
  background: var(--alb-color-linen);
  border-top: 1px solid var(--alb-color-border-taupe);
}}

.monograph-container {{
  max-width: 1360px;
  margin: 0 auto;
  padding: 0 24px;
}}

.section-head-center {{
  text-align: center;
  max-width: 860px;
  margin: 0 auto 50px;
}}

.section-kicker-center {{
  font-family: var(--alb-font-mono);
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--alb-color-brass-deep);
  display: inline-block;
  margin-bottom: 12px;
}}

.section-title-monograph {{
  font-family: var(--alb-font-serif);
  font-size: clamp(2rem, 3.5vw, 3.2rem);
  font-weight: 400;
  line-height: 1.18;
  color: var(--alb-color-charcoal);
  margin-bottom: 16px;
}}

.section-title-monograph em {{
  font-style: italic;
  color: var(--alb-color-brass-deep);
}}

.section-subtitle {{
  font-family: var(--alb-font-sans);
  font-size: 1.02rem;
  line-height: 1.7;
  color: var(--alb-color-secondary);
}}

.monograph-filter-bar {{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 50px;
}}

.filter-tab-btn {{
  background: var(--alb-color-surface);
  border: 1px solid var(--alb-color-border-taupe);
  padding: 10px 22px;
  border-radius: 9999px;
  font-family: var(--alb-font-sans);
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--alb-color-secondary);
  cursor: pointer;
  transition: all 0.25s ease;
}}

.filter-tab-btn:hover,
.filter-tab-btn.active {{
  background: var(--alb-color-charcoal);
  color: #FFFFFF;
  border-color: var(--alb-color-charcoal);
}}

.monograph-cards-stack {{
  display: flex;
  flex-direction: column;
  gap: 60px;
}}

.monograph-card {{
  background: var(--alb-color-surface);
  border: 1px solid var(--alb-color-border-taupe);
  border-radius: var(--alb-radius-lg);
  padding: 44px;
  box-shadow: var(--alb-shadow-subtle);
  transition: transform 0.35s ease, box-shadow 0.35s ease;
}}

.monograph-card:hover {{
  box-shadow: var(--alb-shadow-elevated);
}}

.monograph-grid {{
  display: grid;
  grid-template-columns: 1.05fr 1.15fr;
  gap: 44px;
  align-items: start;
}}

@media (max-width: 1024px) {{
  .monograph-grid {{
    grid-template-columns: 1fr;
  }}
  .monograph-card {{
    padding: 28px 20px;
  }}
}}

.folio-header-meta {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 14px;
  font-family: var(--alb-font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
}}

.folio-num {{
  color: var(--alb-color-brass-deep);
  font-weight: 700;
}}

.folio-cat-badge {{
  background: var(--alb-color-canvas);
  color: var(--alb-color-charcoal);
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 0.72rem;
  text-transform: uppercase;
}}

.folio-loc {{
  color: var(--alb-color-muted);
}}

.monograph-title {{
  font-family: var(--alb-font-serif);
  font-size: 2.1rem;
  font-weight: 500;
  line-height: 1.22;
  color: var(--alb-color-charcoal);
  margin-bottom: 18px;
}}

.architect-guild-plaque {{
  background: var(--alb-color-canvas);
  border: 1px solid var(--alb-color-border-taupe);
  border-radius: var(--alb-radius-sm);
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 22px;
}}

.guild-seal {{
  color: var(--alb-color-brass-deep);
}}

.guild-badge {{
  font-family: var(--alb-font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--alb-color-brass-deep);
  display: block;
}}

.guild-name {{
  font-family: var(--alb-font-sans);
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--alb-color-charcoal);
}}

.guild-role {{
  font-family: var(--alb-font-sans);
  font-size: 0.82rem;
  color: var(--alb-color-secondary);
}}

.monograph-narrative {{
  font-family: var(--alb-font-sans);
  font-size: 0.96rem;
  line-height: 1.7;
  color: var(--alb-color-secondary);
  margin-bottom: 22px;
}}

.audio-commentary-wrap {{
  background: var(--alb-color-canvas);
  border-left: 3px solid var(--alb-color-brass);
  padding: 14px 18px;
  border-radius: 0 var(--alb-radius-sm) var(--alb-radius-sm) 0;
  margin-bottom: 24px;
}}

.audio-kicker {{
  font-family: var(--alb-font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  color: var(--alb-color-brass-deep);
  display: block;
  margin-bottom: 6px;
}}

.audio-quote {{
  font-family: var(--alb-font-serif);
  font-style: italic;
  font-size: 1.05rem;
  color: var(--alb-color-charcoal);
  margin: 0;
  line-height: 1.45;
}}

.monograph-specs {{
  margin-bottom: 28px;
}}

.specs-title {{
  font-family: var(--alb-font-mono);
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  color: var(--alb-color-charcoal);
  margin-bottom: 10px;
}}

.specs-list {{
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}

.spec-item {{
  font-family: var(--alb-font-sans);
  font-size: 0.88rem;
  color: var(--alb-color-secondary);
  display: flex;
  align-items: flex-start;
  gap: 8px;
}}

.spec-bullet {{
  color: var(--alb-color-brass-deep);
}}

.monograph-actions {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}}

.btn-noir-gold {{
  background: var(--alb-color-charcoal);
  color: #FFFFFF;
  border: 1px solid var(--alb-color-charcoal);
  padding: 12px 24px;
  border-radius: 9999px;
  font-family: var(--alb-font-sans);
  font-size: 0.86rem;
  font-weight: 500;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
}}

.btn-noir-gold:hover {{
  background: var(--alb-color-brass-deep);
  border-color: var(--alb-color-brass-deep);
  color: #FFFFFF;
}}

.btn-outline-gold {{
  background: transparent;
  color: var(--alb-color-charcoal);
  border: 1px solid var(--alb-color-border-taupe);
  padding: 12px 24px;
  border-radius: 9999px;
  font-family: var(--alb-font-sans);
  font-size: 0.86rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.25s ease;
}}

.btn-outline-gold:hover {{
  border-color: var(--alb-color-brass);
  color: var(--alb-color-brass-deep);
}}

.project-gallery-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}}

.project-photo-wrap {{
  position: relative;
  border-radius: var(--alb-radius-md);
  overflow: hidden;
  height: 220px;
  cursor: pointer;
  background: var(--alb-color-canvas);
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
  background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, transparent 60%);
  opacity: 0;
  transition: opacity 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 14px;
  color: #FFFFFF;
}}

.project-photo-wrap:hover .photo-overlay {{
  opacity: 1;
}}

.photo-caption-tag {{
  font-family: var(--alb-font-sans);
  font-size: 0.78rem;
}}

/* Before / After Master Styles */
.section-ba-master {{
  padding: clamp(70px, 7vw, 110px) 0;
  background: var(--alb-color-canvas);
  border-top: 1px solid var(--alb-color-border-taupe);
}}

.ba-tabs-nav {{
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 36px;
}}

.ba-tab-btn {{
  background: var(--alb-color-surface);
  border: 1px solid var(--alb-color-border-taupe);
  padding: 9px 18px;
  border-radius: 9999px;
  font-family: var(--alb-font-sans);
  font-size: 0.82rem;
  color: var(--alb-color-secondary);
  cursor: pointer;
  transition: all 0.25s ease;
}}

.ba-tab-btn.active {{
  background: var(--alb-color-charcoal);
  color: #FFFFFF;
  border-color: var(--alb-color-charcoal);
}}

.ba-stage-card {{
  max-width: 1080px;
  margin: 0 auto;
  background: var(--alb-color-surface);
  border: 1px solid var(--alb-color-border-taupe);
  border-radius: var(--alb-radius-lg);
  overflow: hidden;
  box-shadow: var(--alb-shadow-subtle);
}}

.ba-slider-container {{
  position: relative;
  width: 100%;
  height: clamp(380px, 55vw, 620px);
  overflow: hidden;
  user-select: none;
}}

.ba-after-layer, .ba-before-layer {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}}

.ba-after-layer img, .ba-before-layer img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}}

.ba-before-layer {{
  width: 50%;
  overflow: hidden;
  z-index: 2;
  border-right: 2px solid #FFFFFF;
}}

.ba-before-layer img {{
  width: 100%;
  max-width: none;
}}

.ba-handle-line {{
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 2px;
  background: #FFFFFF;
  z-index: 3;
  transform: translateX(-50%);
  cursor: ew-resize;
}}

.ba-handle-grip {{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #FFFFFF;
  box-shadow: 0 4px 16px rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
}}

.ba-tag {{
  position: absolute;
  bottom: 20px;
  z-index: 4;
  background: rgba(33, 33, 33, 0.75);
  backdrop-filter: blur(8px);
  color: #FFFFFF;
  padding: 6px 14px;
  border-radius: 9999px;
  font-family: var(--alb-font-mono);
  font-size: 0.75rem;
  letter-spacing: 0.06em;
}}

.ba-tag-before {{ left: 20px; }}
.ba-tag-after {{ right: 20px; }}

.ba-card-caption {{
  padding: 24px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  background: var(--alb-color-surface);
  border-top: 1px solid var(--alb-color-border-taupe);
}}

@media (max-width: 768px) {{
  .ba-card-caption {{
    flex-direction: column;
    align-items: flex-start;
  }}
}}

.ba-card-caption h4 {{
  font-family: var(--alb-font-serif);
  font-size: 1.35rem;
  color: var(--alb-color-charcoal);
  margin-bottom: 4px;
}}

.ba-card-caption p {{
  font-family: var(--alb-font-sans);
  font-size: 0.9rem;
  color: var(--alb-color-secondary);
  margin: 0;
}}
</style>
</head>
<body>

  <!-- ========================================================================
       1. MASTER HEADER NAVIGATION (ANTHONY LAWRENCE-BELFAIR STYLE)
       ======================================================================== -->
  <header class="alb-header" id="masterHeader">
    <div class="wrap">
      <div class="alb-title-area">
        <a href="#top" class="alb-logo-link">
          <span style="font-family: var(--alb-font-serif); font-size: 24px; font-weight: 700; letter-spacing: 0.15em; color: var(--alb-color-charcoal);">MUAR A</span>
        </a>
        <div class="alb-brand-meta">
          <span class="alb-site-title" style="color: var(--alb-color-charcoal);">BESPOKE ATELIER</span>
          <span class="alb-site-description">ASTANA · EST. 2014</span>
        </div>
      </div>

      <nav class="alb-nav" id="mainNavigation" style="display: flex; gap: 20px; align-items: center;">
        <a href="#monograph" style="font-family: var(--alb-font-sans); font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--alb-color-charcoal); text-decoration: none;">10 Проектов</a>
        <a href="#beforeAfter" style="font-family: var(--alb-font-sans); font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--alb-color-charcoal); text-decoration: none;">До / После</a>
        <a href="#customer-pathways" style="font-family: var(--alb-font-sans); font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--alb-color-charcoal); text-decoration: none;">Маршрут B2C / B2B</a>
        <a href="#the-workroom" style="font-family: var(--alb-font-sans); font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--alb-color-charcoal); text-decoration: none;">Швейный Цех</a>
        <a href="#credentialsSection" style="font-family: var(--alb-font-sans); font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--alb-color-charcoal); text-decoration: none;">Знаки Качества</a>
        <a href="#calculatorApp" style="font-family: var(--alb-font-sans); font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--alb-color-charcoal); text-decoration: none;">Калькулятор</a>
      </nav>

      <div style="display: flex; align-items: center; gap: 14px;">
        <button type="button" class="btn-soundscape" id="soundscapeBtn" onclick="window.muarSoundscape && window.muarSoundscape.toggleSound()" style="background: var(--alb-color-surface); border: 1px solid var(--alb-color-border-taupe); border-radius: 9999px; padding: 8px 16px; font-family: var(--alb-font-mono); font-size: 0.75rem; cursor: pointer; color: var(--alb-color-charcoal);">
          Атмосфера ♪
        </button>
        <a href="https://wa.me/77710551515?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%2C%20MUAR%20A!%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C%D1%81%D1%8F%20%D0%BD%D0%B0%20%D0%B2%D0%B8%D0%B7%D0%B8%D1%82%20%D0%B2%20%D1%81%D0%B0%D0%BB%D0%BE%D0%BD." 
           target="_blank" rel="noopener" class="btn-noir-gold" style="padding: 10px 20px; font-size: 0.82rem;">
          Запись в салон
        </a>
      </div>
    </div>
  </header>

  <!-- ========================================================================
       2. HERO SECTION: ANTHONY LAWRENCE-BELFAIR NYC WORKROOM ATMOSPHERE
       ======================================================================== -->
  <section class="alb-hero" id="top" style="padding-top: 140px; padding-bottom: 80px; background: var(--alb-color-linen);">
    <div class="monograph-container">
      <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 50px; align-items: center;">
        <div>
          <span style="font-family: var(--alb-font-mono); font-size: 0.8rem; letter-spacing: 0.16em; text-transform: uppercase; color: var(--alb-color-brass-deep); display: block; margin-bottom: 16px;">
            ТОО «KAZTEXTILEА» · САЛОН ИНТЕРЬЕРНОГО ТЕКСТИЛЯ С 2014 ГОДА · АСТАНА
          </span>
          <h1 style="font-family: var(--alb-font-serif); font-size: clamp(2.5rem, 4.8vw, 4.2rem); font-weight: 400; line-height: 1.12; color: var(--alb-color-charcoal); margin-bottom: 22px;">
            Текстильная архитектура <em>знаковых резиденций</em> и контрактных объектов
          </h1>
          <p style="font-family: var(--alb-font-sans); font-size: 1.1rem; line-height: 1.75; color: var(--alb-color-secondary); margin-bottom: 32px;">
            Кутюрный пошив штор, моторизованные лифт-системы до 10 метров и оформление частных вилл, пентхаусов и представительских офисов. Собственный цех без надомниц, официальная декларация ЕАЭС и статус Топ-30 декораторов СНГ.
          </p>

          <div style="display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 36px;">
            <a href="#monograph" class="btn-noir-gold" style="padding: 14px 28px; font-size: 0.9rem;">
              Смотреть 10 Реальных Проектов ↓
            </a>
            <a href="#customer-pathways" class="btn-outline-gold" style="padding: 14px 28px; font-size: 0.9rem;" onclick="switchPathwayTab && switchPathwayTab('b2b')">
              Корпоративный портал (НДС 12%)
            </a>
            <a href="#calculatorApp" class="btn-noir-gold" style="background: var(--alb-color-brass-deep); border-color: var(--alb-color-brass-deep); padding: 14px 28px; font-size: 0.9rem;">
              Точный Расчет (508 800 ₸)
            </a>
          </div>

          <div style="display: flex; gap: 28px; border-top: 1px solid var(--alb-color-border-taupe); padding-top: 24px;">
            <div>
              <span style="font-family: var(--alb-font-mono); font-size: 1.6rem; font-weight: 700; color: var(--alb-color-charcoal);">12</span>
              <span style="display: block; font-family: var(--alb-font-sans); font-size: 0.75rem; color: var(--alb-color-muted); text-transform: uppercase;">Лет опыта</span>
            </div>
            <div>
              <span style="font-family: var(--alb-font-mono); font-size: 1.6rem; font-weight: 700; color: var(--alb-color-charcoal);">10м</span>
              <span style="display: block; font-family: var(--alb-font-sans); font-size: 0.75rem; color: var(--alb-color-muted); text-transform: uppercase;">Лифт-системы</span>
            </div>
            <div>
              <span style="font-family: var(--alb-font-mono); font-size: 1.6rem; font-weight: 700; color: var(--alb-color-charcoal);">65</span>
              <span style="display: block; font-family: var(--alb-font-sans); font-size: 0.75rem; color: var(--alb-color-muted); text-transform: uppercase;">Реальных фото</span>
            </div>
            <div>
              <span style="font-family: var(--alb-font-mono); font-size: 1.6rem; font-weight: 700; color: var(--alb-color-charcoal);">100%</span>
              <span style="display: block; font-family: var(--alb-font-sans); font-size: 0.75rem; color: var(--alb-color-muted); text-transform: uppercase;">Цех по ГОСТу</span>
            </div>
          </div>
        </div>

        <div style="border-radius: var(--alb-radius-lg); overflow: hidden; box-shadow: var(--alb-shadow-elevated); border: 1px solid var(--alb-color-border-taupe);">
          <img src="assets/muar/hero-interior.webp" alt="Интерьерное текстильное оформление MUAR A Астана" style="width: 100%; height: 500px; object-fit: cover; display: block;">
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       3. MONOGRAPH OF 10 AUTHENTIC PROJECTS (#monograph)
       ======================================================================== -->
  <section class="section-monograph" id="monograph">
    <div class="monograph-container">
      <div class="section-head-center">
        <span class="section-kicker-center">АРХИВ РЕАЛИЗОВАННЫХ ОБЪЕКТОВ · 2014–2026</span>
        <h2 class="section-title-monograph">
          10 Знаковых проектов · <em>Музейная монография</em>
        </h2>
        <p class="section-subtitle">
          Подлинные истории текстильного оформления резиденций, загородных вилл с высотой потолков до 10 метров, пентхаусов и представительских пространств Астаны. Все 65 архивных фотографий.
        </p>
      </div>

      <div class="monograph-filter-bar">
        <button type="button" class="filter-tab-btn active" data-filter="all" onclick="filterProjects('all')">Все объекты (10)</button>
        <button type="button" class="filter-tab-btn" data-filter="villas" onclick="filterProjects('villas')">Резиденции &amp; Виллы (4)</button>
        <button type="button" class="filter-tab-btn" data-filter="bedrooms" onclick="filterProjects('bedrooms')">Мастер-спальни (4)</button>
        <button type="button" class="filter-tab-btn" data-filter="b2b" onclick="filterProjects('b2b')">B2B &amp; Контракт (2)</button>
      </div>

      <div class="monograph-cards-stack">
        {monograph_cards_html}
      </div>
    </div>
  </section>

  <!-- ========================================================================
       4. INTERACTIVE BEFORE / AFTER TRANSFORMATION (#beforeAfter)
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

      <div class="ba-tabs-nav">
        <button type="button" class="ba-tab-btn active" onclick="switchBaScene(1, this)">01. Red &amp; White (Резиденция)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(2, this)">02. ЖК Vivaldi (Панорамный Dimout)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(3, this)">03. Загородный дом (Римский тюль)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(7, this)">07. Вилла «Темный Рыцарь» (10-метровый холл)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(9, this)">09. Спальня (Коррекция асимметрии окна)</button>
      </div>

      <div class="ba-stage-card">
        <div class="ba-slider-container muar-ba-container" id="baDedicatedSlider" role="slider" tabindex="0" aria-label="Интерактивное сравнение До и После">
          <div class="ba-after-layer muar-ba-layer muar-ba-after">
            <img id="baHeroImgAfter" src="assets/muar/portfolio/garden-14.webp" alt="После текстильного оформления" draggable="false">
          </div>
          <div class="ba-before-layer muar-ba-layer muar-ba-before" id="baHeroBeforeLayer">
            <img id="baHeroImgBefore" src="assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp" alt="До текстильного оформления" draggable="false">
          </div>
          <div class="ba-handle-line muar-ba-divider" id="baHeroHandleLine">
            <div class="ba-handle-grip muar-ba-grip">
              <svg viewBox="0 0 24 24" width="22" height="22">
                <path d="M8.5 7.5L4 12l4.5 4.5M15.5 7.5L20 12l-4.5 4.5" stroke="#1A150B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
              </svg>
            </div>
          </div>
          <div class="ba-tag ba-tag-before" id="baHeroLabelBefore">
            <span id="baHeroLabelBeforeText">Интерьер до текстиля</span>
          </div>
          <div class="ba-tag ba-tag-after" id="baHeroLabelAfter">
            <span id="baHeroLabelAfterText">Кутюрное преображение MUAR A</span>
          </div>
        </div>
        <div class="ba-card-caption">
          <div>
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
       5. CUSTOMER PATHWAYS (6-STEP B2C ROADMAP & B2B CONTRACT PORTAL 12% VAT)
       Delivered by Subagent 6
       ======================================================================== -->
  <div id="roadmap"></div>
  <div id="b2b"></div>
  {pathways['body']}

  <!-- ========================================================================
       6. THE WORKROOM · СОБСТВЕННЫЙ ШВЕЙНЫЙ ЦЕХ И МАСТЕРА КУТЮРА
       Featuring Master Zhanar singing while sewing (04:09 video)
       Delivered by Subagent 5
       ======================================================================== -->
  <div id="atelier"></div>
  {workroom['body']}

  <!-- ========================================================================
       7. OFFICIAL CREDENTIALS & QUALITY MARKS (EAEU, GOLDEN O, TOP-30 CIS)
       Delivered by Subagent 7
       ======================================================================== -->
  <div id="qualityMarks"></div>
  {credentials['body']}

  <!-- ========================================================================
       8. EXACT ASENGUL CALCULATOR (508 800 ₸ PRESET & WHATSAPP DISPATCHER)
       Delivered by Subagent 8
       ======================================================================== -->
  <div id="calculator"></div>
  <section class="section-monograph" id="calculatorApp" style="background: var(--alb-color-linen); padding: clamp(60px, 6vw, 100px) 0;">
    <div class="monograph-container">
      <div class="section-head-center">
        <span class="section-kicker-center">МАТЕМАТИЧЕСКАЯ МОДЕЛЬ ЦЕНООБРАЗОВАНИЯ</span>
        <h2 class="section-title-monograph">
          Интерактивный калькулятор · <em>Смета по ГОСТам РК</em>
        </h2>
        <p class="section-subtitle">
          Прозрачный расчет себестоимости по авторскому регламенту основателя MUAR A Асенгуль: карниз 3.2 м, ткань Испанский сатин (55 000 ₸/м), сборка 1:2.0, цеховой пошив и навеска = <strong>508 800 ₸ ровно</strong>.
        </p>
      </div>
      {calculator['body']}
    </div>
  </section>

  <!-- ========================================================================
       9. CONTACTS & VIP FLAGSHIP SALON APPOINTMENT
       ======================================================================== -->
  <section class="section-monograph" id="contacts" style="background: var(--alb-color-canvas); border-top: 1px solid var(--alb-color-border-taupe);">
    <div class="monograph-container">
      <div class="contacts-card" style="background: var(--alb-color-surface); border: 1px solid var(--alb-color-border-taupe); border-radius: var(--alb-radius-lg); padding: 56px; box-shadow: var(--alb-shadow-subtle);">
        <div class="monograph-grid" style="align-items: center;">
          <div>
            <span class="folio-cat-badge" style="margin-bottom: 16px; display: inline-block;">ФЛАГМАНСКИЙ САЛОН MUAR A В АСТАНЕ</span>
            <h2 class="monograph-title" style="font-size: 2.5rem;">
              Приглашаем в мир <em>высокого текстиля</em>
            </h2>
            <p class="monograph-narrative">
              2 этажа экспозиции европейского текстиля, образцы карнизов с электроприводами Somfy, живые выкрасы и фактуры. За чашкой кофе ведущий декоратор Асенгуль сформирует персональный текстильный сценарий для вашего дома.
            </p>
            <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 28px;">
              <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--alb-color-charcoal);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                г. Астана, ул. Керей, Жәнибек хандар, 50/1, ВП 18
              </div>
              <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--alb-color-charcoal);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="12" cy="12" r="10"/>
                  <polyline points="12 6 12 12 16 14"/>
                </svg>
                Понедельник — Суббота: 10:00 – 19:00 (по предварительной записи)
              </div>
              <div style="display: flex; align-items: center; gap: 12px; font-weight: 600; color: var(--alb-color-charcoal);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
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
            <div style="border-radius: var(--alb-radius-lg); overflow: hidden; box-shadow: var(--alb-shadow-subtle); border: 1px solid var(--alb-color-border-taupe);">
              <img src="assets/muar/strength-1-floors.webp" alt="Салон текстиля MUAR A Астана" style="width: 100%; height: 380px; object-fit: cover;" onerror="this.src='assets/muar/hero-interior.webp'">
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       10. MASTER FOOTER (ANTHONY LAWRENCE-BELFAIR NYC SIGNATURE STYLE)
       ======================================================================== -->
  <footer class="alb-footer" style="background: var(--alb-color-stone); padding: 60px 0 40px; border-top: 1px solid var(--alb-color-stone-dark);">
    <div class="monograph-container">
      <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 40px; margin-bottom: 40px;">
        <div>
          <div style="font-family: var(--alb-font-serif); font-size: 28px; font-weight: 700; letter-spacing: 0.15em; color: var(--alb-color-charcoal); margin-bottom: 12px;">MUAR A</div>
          <p style="font-family: var(--alb-font-sans); font-size: 0.92rem; line-height: 1.6; color: var(--alb-color-secondary); max-width: 480px; margin-bottom: 16px;">
            Флагманский салон интерьерного текстиля, моторизованных карнизов и архитектурной солнцезащиты в Астане с 2014 года. Собственный швейный цех по ГОСТам РК.
          </p>
          <div style="font-family: var(--alb-font-mono); font-size: 0.78rem; color: var(--alb-color-brass-deep);">
            ТОО «KazTextileА» · БИН 140940019744 · НДС 12% · Астана
          </div>
        </div>

        <div>
          <h4 style="font-family: var(--alb-font-mono); font-size: 0.8rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--alb-color-charcoal); margin-bottom: 16px;">Навигация</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; font-family: var(--alb-font-sans); font-size: 0.88rem;">
            <li><a href="#monograph" style="color: var(--alb-color-secondary); text-decoration: none;">10 Архитектурных проектов</a></li>
            <li><a href="#beforeAfter" style="color: var(--alb-color-secondary); text-decoration: none;">Интерактивное До / После</a></li>
            <li><a href="#customer-pathways" style="color: var(--alb-color-secondary); text-decoration: none;">6 шагов маршрута B2C</a></li>
            <li><a href="#customer-pathways" style="color: var(--alb-color-secondary); text-decoration: none;">B2B Контрактный портал (НДС 12%)</a></li>
            <li><a href="#the-workroom" style="color: var(--alb-color-secondary); text-decoration: none;">Швейный цех и Мастер Жанар</a></li>
            <li><a href="#credentialsSection" style="color: var(--alb-color-secondary); text-decoration: none;">Декларация ЕАЭС и Golden O</a></li>
            <li><a href="#calculatorApp" style="color: var(--alb-color-secondary); text-decoration: none;">Калькулятор Асенгуль (508 800 ₸)</a></li>
          </ul>
        </div>

        <div>
          <h4 style="font-family: var(--alb-font-mono); font-size: 0.8rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--alb-color-charcoal); margin-bottom: 16px;">Контакты</h4>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; font-family: var(--alb-font-sans); font-size: 0.88rem; color: var(--alb-color-secondary);">
            <li>Астана, ул. Керей, Жәнибек хандар, 50/1</li>
            <li>Пн–Сб: 10:00 – 19:00</li>
            <li><a href="tel:+77710551515" style="color: var(--alb-color-charcoal); font-weight: 600; text-decoration: none;">+7 771 055 15 15</a></li>
            <li><a href="https://wa.me/77710551515" target="_blank" rel="noopener" style="color: var(--alb-color-brass-deep); text-decoration: none;">WhatsApp Декоратора</a></li>
          </ul>
        </div>
      </div>

      <div style="border-top: 1px solid var(--alb-color-stone-dark); padding-top: 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; font-family: var(--alb-font-sans); font-size: 0.78rem; color: var(--alb-color-muted);">
        <div>© 2014–2026 MUAR A (ТОО «KazTextileА»). Все права защищены.</div>
        <div>Астана · Алматы · Проекты по всему Казахстану</div>
      </div>
    </div>
  </footer>

  <!-- ========================================================================
       11. MASTER CINEMA & LIGHTBOX MODALS
       ======================================================================== -->
  <div class="cinema-modal" id="cinemaModal" onclick="closeCinemaModal(event)" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.92); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="max-width:960px; width:100%; background:#131211; border:1px solid rgba(197,160,105,0.4); border-radius:16px; overflow:hidden;" onclick="event.stopPropagation()">
      <div style="padding:16px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); color:#FFFFFF;">
        <h3 id="cinemaTitle" style="font-family:var(--alb-font-serif); font-size:1.4rem; margin:0;">Экспонат ателье MUAR A</h3>
        <button type="button" onclick="closeCinemaModal()" style="background:none; border:none; color:#FFFFFF; font-size:24px; cursor:pointer;">✕</button>
      </div>
      <div style="position:relative; padding-top:56.25%;">
        <video id="cinemaVideo" controls playsinline style="position:absolute; inset:0; width:100%; height:100%; object-fit:contain;"></video>
      </div>
    </div>
  </div>

  <div class="lightbox-modal" id="projectLightbox" onclick="closeProjectLightbox(event)" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.94); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="max-width:1100px; width:100%; background:#131211; border:1px solid rgba(197,160,105,0.4); border-radius:16px; overflow:hidden;" onclick="event.stopPropagation()">
      <div style="padding:16px 24px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,255,255,0.1); color:#FFFFFF;">
        <h3 id="lightboxTitle" style="font-family:var(--alb-font-serif); font-size:1.4rem; margin:0;">Архив проекта</h3>
        <button type="button" onclick="closeProjectLightbox()" style="background:none; border:none; color:#FFFFFF; font-size:24px; cursor:pointer;">✕</button>
      </div>
      <div style="padding:20px; text-align:center;">
        <img id="lightboxImg" src="" alt="Фотография проекта" style="max-height:75vh; max-width:100%; object-fit:contain; border-radius:8px;">
        <p id="lightboxCaption" style="font-family:var(--alb-font-sans); color:rgba(255,255,255,0.7); margin-top:12px; font-size:0.9rem;"></p>
      </div>
    </div>
  </div>

  <!-- Audio Element for Ambient Lounge -->
  <audio id="ambientAudio" loop preload="none">
    <source src="assets/muar/ambient-lounge.mp3" type="audio/mpeg">
  </audio>

  <!-- ========================================================================
       12. SCRIPTS & LOGIC
       ======================================================================== -->
  <script>
    // Global Projects Dataset from Asengul
    window.MUAR_PROJECTS = {projects_json};
    window.BA_SCENES = {ba_scenes_json};

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
      if (modal) modal.style.display = 'flex';
      
      if (window.muarSoundscape && window.muarSoundscape.isPlaying) {{
        window.muarSoundscape.fadeOut();
      }}
    }}

    function closeCinemaModal(e) {{
      if (e && e.target !== e.currentTarget && !e.target.closest('button')) return;
      const modal = document.getElementById('cinemaModal');
      const video = document.getElementById('cinemaVideo');

      if (video) {{
        video.pause();
        video.removeAttribute('src');
        video.load();
      }}
      if (modal) modal.style.display = 'none';
    }}

    // Project Gallery Lightbox Logic
    let currentLightboxProject = null;
    let currentLightboxIdx = 0;

    function openProjectLightbox(projId, photoIdx) {{
      const proj = window.MUAR_PROJECTS.find(p => p.id === projId);
      if (!proj || !proj.photos || !proj.photos[photoIdx]) return;

      currentLightboxProject = proj;
      currentLightboxIdx = photoIdx;

      const modal = document.getElementById('projectLightbox');
      const img = document.getElementById('lightboxImg');
      const titleEl = document.getElementById('lightboxTitle');
      const captionEl = document.getElementById('lightboxCaption');

      const photo = proj.photos[photoIdx];
      if (titleEl) titleEl.textContent = `Проект №${{proj.num}} · ${{proj.title}} (${{photoIdx + 1}} из ${{proj.photos.length}})`;
      if (img) img.src = photo.src;
      if (captionEl) captionEl.textContent = photo.alt;

      if (modal) modal.style.display = 'flex';
    }}

    function closeProjectLightbox(e) {{
      if (e && e.target !== e.currentTarget && !e.target.closest('button')) return;
      const modal = document.getElementById('projectLightbox');
      if (modal) modal.style.display = 'none';
    }}

    // Before/After Switcher
    function switchBaScene(sceneId, btn) {{
      const scene = window.BA_SCENES[sceneId];
      if (!scene) return;

      document.querySelectorAll('.ba-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      const imgBefore = document.getElementById('baHeroImgBefore');
      const imgAfter = document.getElementById('baHeroImgAfter');
      const titleEl = document.getElementById('baHeroCaptionTitle');
      const descEl = document.getElementById('baHeroCaptionDesc');
      const lblBefore = document.getElementById('baHeroLabelBeforeText');
      const lblAfter = document.getElementById('baHeroLabelAfterText');

      if (imgBefore) imgBefore.src = scene.before;
      if (imgAfter) imgAfter.src = scene.after;
      if (titleEl) titleEl.textContent = scene.title;
      if (descEl) descEl.textContent = scene.desc;
      if (lblBefore) lblBefore.textContent = scene.labelBefore;
      if (lblAfter) lblAfter.textContent = scene.labelAfter;
    }}

    // Projects Filter
    function filterProjects(cat) {{
      document.querySelectorAll('.filter-tab-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.querySelector(`.filter-tab-btn[data-filter="${{cat}}"]`);
      if (activeBtn) activeBtn.classList.add('active');

      const cards = document.querySelectorAll('.monograph-card');
      cards.forEach(c => {{
        if (cat === 'all' || c.getAttribute('data-category') === cat) {{
          c.style.display = 'block';
        }} else {{
          c.style.display = 'none';
        }}
      }});
    }}

    // Keyboard ESC listener
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') {{
        closeCinemaModal();
        closeProjectLightbox();
      }}
    }});
  </script>

  <!-- Subagent Modules JavaScript -->
  <script>
{tactile_js}
  </script>

  <script>
{interactive_engine_js}
  </script>

  <script>
{workroom['scripts']}
  </script>

  <script>
{pathways['scripts']}
  </script>

  <script>
{credentials['scripts']}
  </script>

  <script>
{calculator['scripts']}
  </script>

</body>
</html>
'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(master_html)
    with open('dist/index.html', 'w', encoding='utf-8') as f:
        f.write(master_html)
        
    print(f"SUCCESS: Generated master index.html ({len(master_html)} bytes)")

if __name__ == '__main__':
    main()
