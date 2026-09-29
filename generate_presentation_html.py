#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the complete, high-fidelity, production-grade index.html for MUAR A.
Strictly executes the user's requirement:
"сохрани что есть / дальше давай вот тут все смотрисноси ис уть вытащи убираем этот стиль дедлаем новый полностью по тем 10 проектам которые есть и берем описание"
"""

import json
from build_new_index import PROJECTS

def generate_html():
    projects_json = json.dumps(PROJECTS, ensure_ascii=False)
    
    html = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>MUAR A · 10 Знаковых Проектов и Ателье Текстиля в Астане</title>
  <meta name="description" content="10 реализованных проектов интерьерного текстиля в Астане: от частных пентхаусов и загородных вилл до представительских кабинетов. Собственный швейный цех, точный расчет стоимости и авторский надзор.">
  <meta name="theme-color" content="#0B0B0E">
  
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="MUAR A · 10 Знаковых Проектов и Ателье Текстиля в Астане">
  <meta property="og:description" content="Подлинные истории создания текстиля от основателя ателье Асемгуль и ведущих архитекторов Казахстана: Зарины Секен, IDesign, Габидена, Динары Усмановой, Лауры Жакиной и Руслана.">
  <meta property="og:image" content="assets/muar/portfolio/garden-14.webp">
  <meta property="og:url" content="https://muar-a.pages.dev/">

  <!-- Google Fonts: Playfair Display + Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">

  <!-- MUAR A Tactile Motion & Interactive Engine Styles -->
  <link rel="stylesheet" href="scratch/interactive_engine.css">

  <style>
    /* ============================================================ */
    /* 1. ARCHITECTURAL LUXURY DESIGN SYSTEM (ANTI-AI SLOP)         */
    /* Clean obsidian/charcoal palette + Couture Coral Accents      */
    /* ============================================================ */
    :root {{
      --bg-base: #0B0B0E;
      --bg-surface: #121217;
      --bg-surface-elevated: #181820;
      --bg-card: #14141A;
      --bg-card-hover: #1A1A24;
      
      /* Asengul explicit wish: Couture Coral for project accents */
      --coral: #E25A3D;
      --coral-light: #FF7052;
      --coral-soft: #FFA08A;
      --coral-bg: rgba(226, 90, 61, 0.12);
      --coral-border: rgba(226, 90, 61, 0.4);
      --coral-glow: rgba(226, 90, 61, 0.25);
      
      --gold: #C5A059;
      --gold-soft: #D8BA7A;
      --gold-bg: rgba(197, 160, 89, 0.1);
      
      --text-primary: #FFFFFF;
      --text-secondary: rgba(255, 255, 255, 0.78);
      --text-muted: rgba(255, 255, 255, 0.48);
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(255, 255, 255, 0.2);
      
      --font-serif: "Playfair Display", Georgia, "Times New Roman", serif;
      --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-xl: 28px;
      --radius-pill: 9999px;
      --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      background-color: var(--bg-base);
      color: var(--text-primary);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.6;
    }}

    body {{
      background-color: var(--bg-base);
      color: var(--text-primary);
      overflow-x: hidden;
      min-height: 100vh;
      position: relative;
    }}

    a {{
      color: inherit;
      text-decoration: none;
      transition: var(--transition);
    }}

    button, input, select, textarea {{
      font: inherit;
      color: inherit;
    }}

    img, video {{
      max-width: 100%;
      height: auto;
      display: block;
    }}

    .wrap {{
      width: 100%;
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    @media (max-width: 768px) {{
      .wrap {{ padding: 0 16px; }}
    }}

    /* Typography */
    .font-serif {{ font-family: var(--font-serif); }}
    .coral-text {{ color: var(--coral); }}
    .gold-text {{ color: var(--gold); }}

    .section-kicker {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--coral);
      margin-bottom: 12px;
    }}
    .section-kicker::before {{
      content: "";
      display: inline-block;
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--coral);
      box-shadow: 0 0 8px var(--coral);
    }}

    .section-title {{
      font-family: var(--font-serif);
      font-size: clamp(2rem, 3.8vw, 3.2rem);
      font-weight: 600;
      line-height: 1.18;
      letter-spacing: -0.02em;
      color: var(--text-primary);
      margin-bottom: 16px;
    }}

    .section-subtitle {{
      font-size: clamp(1rem, 1.3vw, 1.15rem);
      color: var(--text-secondary);
      max-width: 780px;
      line-height: 1.65;
    }}

    .center {{ text-align: center; }}
    .center .section-subtitle {{ margin-left: auto; margin-right: auto; }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 14px 28px;
      border-radius: var(--radius-pill);
      font-size: 0.92rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      transition: var(--transition);
      white-space: nowrap;
      text-decoration: none;
    }}
    .btn-coral {{
      background: var(--coral);
      color: #FFFFFF;
      box-shadow: 0 4px 20px var(--coral-glow);
    }}
    .btn-coral:hover {{
      background: var(--coral-light);
      transform: translateY(-2px);
      box-shadow: 0 8px 28px rgba(226, 90, 61, 0.4);
    }}
    .btn-ghost {{
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--border-subtle);
      color: var(--text-primary);
    }}
    .btn-ghost:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: var(--border-hover);
      transform: translateY(-2px);
    }}
    .btn-sm {{
      padding: 9px 18px;
      font-size: 0.82rem;
    }}

    /* ============================================================ */
    /* 2. STICKY LUXURY HEADER                                      */
    /* ============================================================ */
    .header {{
      position: sticky;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 100;
      background: rgba(11, 11, 14, 0.88);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-subtle);
      transition: var(--transition);
    }}
    .header-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 74px;
    }}
    .logo-wrap {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .brand-logo {{
      font-family: var(--font-serif);
      font-size: 1.65rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .brand-logo span {{
      color: var(--coral);
    }}
    .brand-tagline {{
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-muted);
      border-left: 1px solid var(--border-subtle);
      padding-left: 12px;
      display: none;
    }}
    @media (min-width: 900px) {{
      .brand-tagline {{ display: block; }}
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 28px;
      list-style: none;
    }}
    @media (max-width: 1024px) {{
      .nav-links {{ display: none; }}
    }}
    .nav-link {{
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-secondary);
      position: relative;
      padding: 6px 0;
    }}
    .nav-link:hover, .nav-link.active {{
      color: #FFFFFF;
    }}
    .nav-link.active::after {{
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 2px;
      background: var(--coral);
      border-radius: 2px;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .audio-toggle-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 14px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      font-size: 0.78rem;
      font-weight: 500;
      color: var(--text-secondary);
      cursor: pointer;
      transition: var(--transition);
    }}
    .audio-toggle-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--border-hover);
      color: #FFFFFF;
    }}
    .audio-toggle-btn.active {{
      border-color: var(--coral);
      color: var(--coral-light);
      background: var(--coral-bg);
    }}
    .sound-wave {{
      display: flex;
      align-items: center;
      gap: 2px;
      height: 12px;
    }}
    .sound-bar {{
      width: 2px;
      background: currentColor;
      border-radius: 1px;
      height: 4px;
      transition: height 0.2s ease;
    }}
    .audio-toggle-btn.active .sound-bar:nth-child(1) {{ animation: eq 0.6s infinite ease-in-out alternate; }}
    .audio-toggle-btn.active .sound-bar:nth-child(2) {{ animation: eq 0.8s infinite 0.2s ease-in-out alternate; }}
    .audio-toggle-btn.active .sound-bar:nth-child(3) {{ animation: eq 0.5s infinite 0.4s ease-in-out alternate; }}
    @keyframes eq {{ 0% {{ height: 3px; }} 100% {{ height: 12px; }} }}

    @media (max-width: 640px) {{
      .header-inner {{ height: 62px; }}
      .audio-btn-text {{ display: none; }}
      .header-actions .btn-sm {{ padding: 7px 12px; font-size: 0.75rem; }}
      .brand-logo {{ font-size: 1.35rem; }}
    }}

    /* ============================================================ */
    /* 3. EDITORIAL HERO SECTION                                    */
    /* ============================================================ */
    .hero-section {{
      position: relative;
      min-height: 82vh;
      display: flex;
      align-items: center;
      padding: 70px 0 60px;
      background: radial-gradient(ellipse 80% 50% at 50% -10%, rgba(226, 90, 61, 0.15) 0%, transparent 70%);
      border-bottom: 1px solid var(--border-subtle);
      overflow: hidden;
    }}
    .hero-content {{
      max-width: 920px;
      margin: 0 auto;
      text-align: center;
      width: 100%;
    }}
    .hero-kicker-pill {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      background: var(--coral-bg);
      border: 1px solid var(--coral-border);
      color: var(--coral-light);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 24px;
    }}
    .hero-title {{
      font-family: var(--font-serif);
      font-size: clamp(2.2rem, 5.2vw, 4.2rem);
      font-weight: 600;
      line-height: 1.12;
      letter-spacing: -0.025em;
      color: #FFFFFF;
      margin-bottom: 24px;
    }}
    .hero-title em {{
      font-style: italic;
      color: var(--coral-light);
    }}
    .hero-lead {{
      font-size: clamp(1rem, 1.6vw, 1.25rem);
      line-height: 1.65;
      color: var(--text-secondary);
      max-width: 780px;
      margin: 0 auto 36px;
    }}
    .hero-actions {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 50px;
    }}
    .hero-metrics-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      max-width: 900px;
      margin: 0 auto;
      padding-top: 36px;
      border-top: 1px solid var(--border-subtle);
    }}
    @media (max-width: 768px) {{
      .hero-metrics-grid {{ grid-template-columns: repeat(2, 1fr); gap: 20px; }}
    }}
    .metric-card {{
      text-align: center;
    }}
    .metric-val {{
      font-family: var(--font-serif);
      font-size: 2.2rem;
      font-weight: 700;
      color: #FFFFFF;
      line-height: 1;
      margin-bottom: 6px;
    }}
    .metric-val span {{ color: var(--coral); }}
    .metric-label {{
      font-size: 0.78rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    /* ============================================================ */
    /* 4. THE 10 REAL PROJECTS SECTION (THE STAR OF THE SHOW)       */
    /* ============================================================ */
    .section-projects {{
      padding: 90px 0;
      position: relative;
      overflow: hidden;
    }}
    .projects-filter-bar {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
      margin: 36px 0 44px;
    }}
    .filter-btn {{
      padding: 9px 20px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text-secondary);
      cursor: pointer;
      transition: var(--transition);
    }}
    .filter-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--border-hover);
      color: #FFFFFF;
    }}
    .filter-btn.active {{
      background: var(--coral);
      border-color: var(--coral);
      color: #FFFFFF;
      box-shadow: 0 4px 16px var(--coral-glow);
    }}

    /* Interactive Showcase Stage */
    .showcase-stage {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      display: grid;
      grid-template-columns: 340px 1fr;
      box-shadow: 0 30px 80px -20px rgba(0, 0, 0, 0.7);
      margin-bottom: 50px;
      width: 100%;
      max-width: 100%;
      box-sizing: border-box;
    }}
    @media (max-width: 1080px) {{
      .showcase-stage {{
        grid-template-columns: 100%;
        width: 100%;
      }}
    }}

    /* Left: Project Selector List */
    .stage-nav {{
      border-right: 1px solid var(--border-subtle);
      background: rgba(0, 0, 0, 0.25);
      max-height: 820px;
      overflow-y: auto;
      overflow-x: hidden;
      scrollbar-width: thin;
      scrollbar-color: rgba(255, 255, 255, 0.15) transparent;
      width: 100%;
      box-sizing: border-box;
    }}
    @media (max-width: 1080px) {{
      .stage-nav {{
        border-right: none;
        border-bottom: 1px solid var(--border-subtle);
        max-height: 280px;
      }}
    }}
    .stage-nav-header {{
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-subtle);
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-sizing: border-box;
      width: 100%;
    }}
    .nav-item-btn {{
      width: 100%;
      text-align: left;
      padding: 16px 20px;
      background: transparent;
      border: none;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      transition: var(--transition);
      position: relative;
      box-sizing: border-box;
    }}
    .nav-item-btn:hover {{
      background: rgba(255, 255, 255, 0.03);
    }}
    .nav-item-btn.active {{
      background: rgba(226, 90, 61, 0.08);
      border-left: 3px solid var(--coral);
    }}
    .nav-num-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: var(--radius-sm);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--text-secondary);
      flex-shrink: 0;
    }}
    .nav-item-btn.active .nav-num-badge {{
      background: var(--coral);
      border-color: var(--coral);
      color: #FFFFFF;
      box-shadow: 0 2px 10px var(--coral-glow);
    }}
    .nav-meta {{ flex: 1; min-width: 0; }}
    .nav-project-title {{
      font-size: 0.95rem;
      font-weight: 600;
      color: #FFFFFF;
      line-height: 1.35;
      margin-bottom: 4px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .nav-item-btn.active .nav-project-title {{
      color: var(--coral-light);
    }}
    .nav-project-collab {{
      font-size: 0.78rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Right: Active Project Stage Details */
    .stage-view {{
      padding: 36px 40px;
      display: flex;
      flex-direction: column;
      gap: 28px;
      background: var(--bg-card);
    }}
    @media (max-width: 768px) {{
      .stage-view {{ padding: 24px 18px; }}
    }}

    /* Main Visual / Slider Container */
    .stage-media-wrap {{
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      background: #000000;
      border: 1px solid var(--border-subtle);
      aspect-ratio: 16/10;
      width: 100%;
      box-shadow: 0 16px 40px -10px rgba(0, 0, 0, 0.6);
    }}
    @media (max-width: 768px) {{
      .stage-media-wrap {{ aspect-ratio: 4/3; }}
    }}
    .stage-primary-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }}

    /* Split Before/After Slider inside Viewer */
    .ba-slider-container {{
      position: relative;
      width: 100%;
      height: 100%;
      overflow: hidden;
      user-select: none;
      touch-action: pan-y;
      cursor: ew-resize;
    }}
    .ba-after-layer, .ba-before-layer {{
      position: absolute;
      top: 0;
      left: 0;
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
      clip-path: inset(0 50% 0 0);
      z-index: 2;
    }}
    .ba-handle-line {{
      position: absolute;
      top: 0;
      bottom: 0;
      left: 50%;
      width: 2px;
      background: #FFFFFF;
      box-shadow: 0 0 12px rgba(0, 0, 0, 0.8);
      z-index: 5;
      transform: translateX(-50%);
      pointer-events: none;
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
      color: #000000;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
      font-size: 16px;
      cursor: grab;
      border: 2px solid var(--coral);
    }}
    .ba-tag {{
      position: absolute;
      bottom: 16px;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.15);
      z-index: 6;
      pointer-events: none;
    }}
    .ba-tag-before {{ left: 16px; }}
    .ba-tag-after {{ right: 16px; border-color: var(--coral); color: var(--coral-light); }}

    /* Project Information */
    .stage-info-header {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .project-header-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .stage-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--coral);
    }}
    .stage-collab-pill {{
      font-size: 0.82rem;
      font-weight: 500;
      color: var(--gold-soft);
      background: var(--gold-bg);
      border: 1px solid rgba(197, 160, 89, 0.3);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
    }}
    .stage-title {{
      font-family: var(--font-serif);
      font-size: clamp(1.6rem, 2.5vw, 2.4rem);
      font-weight: 600;
      line-height: 1.25;
      color: #FFFFFF;
    }}
    .stage-desc {{
      font-size: 1.02rem;
      line-height: 1.7;
      color: var(--text-secondary);
      background: rgba(255, 255, 255, 0.02);
      border-left: 3px solid var(--coral);
      padding: 16px 20px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
    }}

    /* Material Specs Chips */
    .stage-specs {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .spec-chip {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      font-size: 0.8rem;
      font-weight: 500;
      color: var(--text-secondary);
    }}
    .spec-chip::before {{
      content: "";
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: var(--coral);
    }}

    /* Gallery Strip */
    .stage-gallery-wrap {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding-top: 16px;
      border-top: 1px solid var(--border-subtle);
    }}
    .gallery-label-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .gallery-label {{
      font-size: 0.82rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }}
    .gallery-lightbox-trigger {{
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--coral-light);
      background: none;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
    }}
    .gallery-lightbox-trigger:hover {{
      color: #FFFFFF;
      text-decoration: underline;
    }}
    .gallery-strip {{
      display: flex;
      gap: 10px;
      overflow-x: auto;
      padding-bottom: 6px;
      scrollbar-width: thin;
      scrollbar-color: rgba(255, 255, 255, 0.15) transparent;
    }}
    .gallery-thumb-btn {{
      position: relative;
      width: 88px;
      height: 64px;
      flex-shrink: 0;
      border-radius: var(--radius-sm);
      overflow: hidden;
      border: 2px solid transparent;
      background: #000000;
      cursor: pointer;
      transition: var(--transition);
      padding: 0;
    }}
    .gallery-thumb-btn img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.7;
      transition: var(--transition);
    }}
    .gallery-thumb-btn:hover img {{
      opacity: 1;
      transform: scale(1.05);
    }}
    .gallery-thumb-btn.active {{
      border-color: var(--coral);
      box-shadow: 0 0 12px var(--coral-glow);
    }}
    .gallery-thumb-btn.active img {{
      opacity: 1;
    }}

    /* 10 Projects Visual Grid (Scanning all 10) */
    .projects-grid-section {{
      margin-top: 40px;
    }}
    .projects-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }}
    @media (max-width: 1024px) {{
      .projects-grid {{ grid-template-columns: repeat(2, 1fr); gap: 18px; }}
    }}
    @media (max-width: 640px) {{
      .projects-grid {{ grid-template-columns: 1fr; gap: 16px; }}
    }}
    .project-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: var(--transition);
      cursor: pointer;
    }}
    .project-card:hover {{
      transform: translateY(-4px);
      border-color: var(--border-hover);
      box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.5);
    }}
    .project-card-media {{
      position: relative;
      aspect-ratio: 16/10;
      overflow: hidden;
      background: #000000;
    }}
    .project-card-media img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }}
    .project-card:hover .project-card-media img {{
      transform: scale(1.04);
    }}
    .card-badge {{
      position: absolute;
      top: 14px;
      left: 14px;
      padding: 5px 12px;
      border-radius: var(--radius-pill);
      background: rgba(11, 11, 14, 0.85);
      backdrop-filter: blur(8px);
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--coral-light);
      border: 1px solid var(--coral-border);
    }}
    .project-card-body {{
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      flex: 1;
    }}
    .card-collab {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}
    .card-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 600;
      line-height: 1.3;
      color: #FFFFFF;
      margin-bottom: 10px;
    }}
    .card-snippet {{
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.55;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-bottom: 16px;
    }}
    .card-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 14px;
      border-top: 1px solid var(--border-subtle);
      font-size: 0.82rem;
    }}
    .card-photos-count {{
      color: var(--text-muted);
    }}
    .card-open-link {{
      color: var(--coral-light);
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}

    /* ============================================================ */
    /* 5. BEFORE & AFTER TRANSFORMATION LAB                         */
    /* ============================================================ */
    .section-ba {{
      padding: 80px 0;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }}
    .ba-tabs-nav {{
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      margin: 36px 0 40px;
    }}
    .ba-tab-btn {{
      padding: 10px 22px;
      border-radius: var(--radius-pill);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text-secondary);
      cursor: pointer;
      transition: var(--transition);
    }}
    .ba-tab-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--border-hover);
      color: #FFFFFF;
    }}
    .ba-tab-btn.active {{
      background: var(--coral);
      border-color: var(--coral);
      color: #FFFFFF;
      box-shadow: 0 4px 16px var(--coral-glow);
    }}
    .ba-stage-card {{
      max-width: 1080px;
      margin: 0 auto;
      border-radius: var(--radius-xl);
      overflow: hidden;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      box-shadow: 0 24px 60px -15px rgba(0, 0, 0, 0.6);
    }}
    .ba-slider-hero {{
      aspect-ratio: 16/10;
      width: 100%;
      position: relative;
      overflow: hidden;
      background: #000000;
    }}
    .ba-card-caption {{
      padding: 24px 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      background: var(--bg-card);
      border-top: 1px solid var(--border-subtle);
    }}
    .ba-caption-text h4 {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      color: #FFFFFF;
      margin-bottom: 4px;
    }}
    .ba-caption-text p {{
      font-size: 0.9rem;
      color: var(--text-secondary);
    }}

    /* ============================================================ */
    /* 6. ATELIER WORKSHOP & CRAFTSMANSHIP (REAL VIDEOS)            */
    /* ============================================================ */
    .section-atelier {{
      padding: 90px 0;
      position: relative;
    }}
    .videos-trio-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      margin-top: 48px;
    }}
    @media (max-width: 992px) {{
      .videos-trio-grid {{ grid-template-columns: 1fr; gap: 20px; }}
    }}
    .video-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: var(--transition);
    }}
    .video-card:hover {{
      border-color: var(--border-hover);
      transform: translateY(-4px);
      box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.6);
    }}
    .video-player-wrap {{
      position: relative;
      aspect-ratio: 16/10;
      background: #000000;
      overflow: hidden;
    }}
    .video-player-wrap video {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .video-card-body {{
      padding: 24px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .video-card-tag {{
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--coral-light);
      margin-bottom: 8px;
    }}
    .video-card-title {{
      font-family: var(--font-serif);
      font-size: 1.3rem;
      color: #FFFFFF;
      line-height: 1.3;
      margin-bottom: 10px;
    }}
    .video-card-desc {{
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.55;
    }}

    /* 6 Quality Pillars */
    .pillars-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 60px;
      padding-top: 40px;
      border-top: 1px solid var(--border-subtle);
    }}
    @media (max-width: 900px) {{
      .pillars-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
      .pillars-grid {{ grid-template-columns: 1fr; }}
    }}
    .pillar-item {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 22px;
      display: flex;
      gap: 16px;
    }}
    .pillar-num {{
      font-family: var(--font-serif);
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--coral);
      line-height: 1;
    }}
    .pillar-content h5 {{
      font-size: 1rem;
      font-weight: 600;
      color: #FFFFFF;
      margin-bottom: 6px;
    }}
    .pillar-content p {{
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* ============================================================ */
    /* 7. EXACT ASENGUL CALCULATION ENGINE (ALABASTER & BRASS HAUTE COUTURE) */
    /* ============================================================ */
    .section-calc {{
      padding: 100px 0;
      background: radial-gradient(circle at 50% 25%, rgba(197, 160, 89, 0.08) 0%, rgba(11, 11, 14, 0.98) 75%);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
      position: relative;
    }}
    .calc-alabaster-card {{
      background: #FFFFFF;
      border: 1px solid rgba(197, 160, 89, 0.42);
      border-radius: var(--radius-xl);
      overflow: hidden;
      margin-top: 48px;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(197, 160, 89, 0.25);
      position: relative;
      color: #1C1917;
    }}
    .calc-alabaster-card::before {{
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 4px;
      background: linear-gradient(90deg, #A78138 0%, #C5A059 50%, #D8BA7A 100%);
      z-index: 2;
    }}

    /* Direction Navigation Tabs */
    .calc-direction-bar {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      background: #F4EFEB;
      border-bottom: 1px solid rgba(197, 160, 89, 0.25);
      padding: 6px;
      gap: 6px;
    }}
    @media (max-width: 900px) {{
      .calc-direction-bar {{ grid-template-columns: 1fr 1fr; }}
    }}
    .dir-tab-btn {{
      padding: 14px 16px;
      background: transparent;
      border: 1px solid transparent;
      border-radius: var(--radius-md);
      font-size: 0.9rem;
      font-weight: 600;
      color: #6E685F;
      cursor: pointer;
      transition: var(--transition);
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }}
    .dir-tab-btn:hover {{
      color: #1C1917;
      background: rgba(255, 255, 255, 0.6);
    }}
    .dir-tab-btn.active {{
      background: #FFFFFF;
      color: #1C1917;
      border-color: rgba(197, 160, 89, 0.35);
      box-shadow: 0 4px 14px rgba(28, 25, 23, 0.06);
    }}
    .badge-exact {{
      font-size: 0.68rem;
      background: #C5A059;
      color: #FFFFFF;
      padding: 2px 7px;
      border-radius: var(--radius-pill);
      font-weight: 700;
    }}

    .calc-body-grid {{
      display: grid;
      grid-template-columns: 1.3fr 1fr;
      background: #FFFFFF;
    }}
    @media (max-width: 992px) {{
      .calc-body-grid {{ grid-template-columns: 1fr; }}
    }}
    .calc-controls-pane {{
      padding: 36px;
      border-right: 1px solid rgba(197, 160, 89, 0.22);
      display: flex;
      flex-direction: column;
      gap: 26px;
      background: #FFFFFF;
    }}
    @media (max-width: 768px) {{
      .calc-controls-pane {{ padding: 24px 18px; border-right: none; border-bottom: 1px solid rgba(197, 160, 89, 0.22); }}
    }}
    .calc-summary-pane {{
      padding: 36px;
      background: #FAF8F5;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    @media (max-width: 768px) {{
      .calc-summary-pane {{ padding: 24px 18px; }}
    }}

    .calc-field-group {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .calc-field-label {{
      font-size: 0.76rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #9E7A32;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .calc-field-label::after {{
      content: "";
      flex: 1;
      height: 1px;
      background: rgba(197, 160, 89, 0.22);
    }}

    /* Fabric Grid (3 rows × 2 cols = 6 noble fabrics) */
    .fabric-grid-3x2 {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }}
    @media (max-width: 580px) {{
      .fabric-grid-3x2 {{ grid-template-columns: 1fr; }}
    }}
    .fabric-select-card {{
      background: #FAF8F5;
      border: 1.5px solid rgba(197, 160, 89, 0.22);
      border-radius: var(--radius-md);
      padding: 12px 14px;
      text-align: left;
      cursor: pointer;
      transition: var(--transition);
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .fabric-select-card:hover {{
      background: #FFFFFF;
      border-color: #D8BA7A;
      transform: translateY(-2px);
    }}
    .fabric-select-card.active {{
      background: #FFFFFF;
      border-color: #C5A059;
      box-shadow: 0 4px 16px rgba(197, 160, 89, 0.18), 0 0 0 1px #C5A059;
    }}
    .fabric-card-row-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 8px;
      margin-bottom: 4px;
    }}
    .fabric-title-text {{
      font-size: 0.92rem;
      font-weight: 600;
      color: #1C1917;
      line-height: 1.25;
    }}
    .fabric-country-sub {{
      font-size: 0.72rem;
      color: #82786F;
    }}
    .fabric-cost-badge {{
      font-size: 0.84rem;
      font-weight: 700;
      color: #9E7A32;
      background: rgba(197, 160, 89, 0.12);
      padding: 2px 7px;
      border-radius: 6px;
      white-space: nowrap;
      border: 1px solid rgba(197, 160, 89, 0.25);
    }}
    .fabric-detail-desc {{
      font-size: 0.74rem;
      color: #6E685F;
      line-height: 1.35;
      margin-top: 3px;
    }}
    .fabric-active-dot {{
      position: absolute;
      top: 8px;
      right: 8px;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: #C5A059;
      color: #FFFFFF;
      font-size: 10px;
      display: none;
      align-items: center;
      justify-content: center;
    }}
    .fabric-select-card.active .fabric-active-dot {{
      display: flex;
    }}

    /* Slider Box */
    .slider-surface-box {{
      background: #F4EFEB;
      border: 1px solid rgba(197, 160, 89, 0.25);
      border-radius: var(--radius-md);
      padding: 16px 20px;
    }}
    .slider-surface-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .slider-surface-title {{
      font-size: 0.88rem;
      font-weight: 600;
      color: #1C1917;
    }}
    .slider-surface-val {{
      font-family: var(--font-serif);
      font-size: 1.3rem;
      font-weight: 700;
      color: #9E7A32;
      background: #FFFFFF;
      padding: 3px 12px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(197, 160, 89, 0.35);
    }}
    .slider-brass-input {{
      width: 100%;
      height: 6px;
      border-radius: 3px;
      background: #ECE5DE;
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
    }}
    .slider-brass-input::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: linear-gradient(135deg, #D8BA7A 0%, #A78138 100%);
      box-shadow: 0 3px 8px rgba(167, 129, 56, 0.35);
      border: 2px solid #FFFFFF;
      cursor: grab;
      transition: transform 0.15s ease;
    }}
    .slider-brass-input::-webkit-slider-thumb:hover {{
      transform: scale(1.15);
    }}
    .slider-surface-sub {{
      display: flex;
      justify-content: space-between;
      font-size: 0.72rem;
      color: #82786F;
      margin-top: 6px;
    }}

    /* Checkbox Rows */
    .calc-check-brass-row {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 11px 16px;
      background: #F4EFEB;
      border: 1px solid rgba(197, 160, 89, 0.22);
      border-radius: var(--radius-md);
      cursor: pointer;
      font-size: 0.86rem;
      color: #4A443E;
      transition: var(--transition);
    }}
    .calc-check-brass-row:hover {{
      background: #FAF8F5;
      border-color: #C5A059;
    }}
    .calc-check-brass-row input[type=checkbox] {{
      width: 18px;
      height: 18px;
      accent-color: #C5A059;
      cursor: pointer;
    }}

    /* Bedspread 5 Tiers */
    .tier-stack-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .tier-choice-btn {{
      background: #FAF8F5;
      border: 1.5px solid rgba(197, 160, 89, 0.22);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      text-align: left;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .tier-choice-btn:hover {{
      background: #FFFFFF;
      border-color: #D8BA7A;
    }}
    .tier-choice-btn.active {{
      background: #FFFFFF;
      border-color: #C5A059;
      box-shadow: 0 4px 14px rgba(197, 160, 89, 0.14);
    }}
    .tier-head-txt {{
      font-size: 0.9rem;
      font-weight: 600;
      color: #1C1917;
      margin-bottom: 2px;
    }}
    .tier-sub-txt {{
      font-size: 0.74rem;
      color: #82786F;
    }}
    .tier-tag-pill {{
      font-size: 0.82rem;
      font-weight: 700;
      color: #9E7A32;
      background: rgba(197, 160, 89, 0.12);
      padding: 3px 8px;
      border-radius: 6px;
      white-space: nowrap;
      border: 1px solid rgba(197, 160, 89, 0.25);
    }}

    /* B2B Packages */
    .b2b-contract-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }}
    @media (max-width: 580px) {{
      .b2b-contract-grid {{ grid-template-columns: 1fr; }}
    }}
    .b2b-contract-card {{
      background: #FAF8F5;
      border: 1.5px solid rgba(197, 160, 89, 0.22);
      border-radius: var(--radius-md);
      padding: 14px;
      text-align: left;
      cursor: pointer;
      transition: var(--transition);
    }}
    .b2b-contract-card:hover {{
      background: #FFFFFF;
      border-color: #D8BA7A;
    }}
    .b2b-contract-card.active {{
      background: #FFFFFF;
      border-color: #C5A059;
      box-shadow: 0 4px 14px rgba(197, 160, 89, 0.14);
    }}

    /* Summary Pane */
    .summary-kicker-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(197, 160, 89, 0.25);
      padding-bottom: 14px;
      margin-bottom: 18px;
    }}
    .summary-atelier-name {{
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #9E7A32;
    }}
    .summary-formula-tag {{
      font-size: 0.72rem;
      color: #6E685F;
      background: #FFFFFF;
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid rgba(197, 160, 89, 0.22);
    }}
    .summary-heading-h4 {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-weight: 600;
      color: #1C1917;
      line-height: 1.25;
      margin-bottom: 4px;
    }}
    .summary-lead-desc {{
      font-size: 0.8rem;
      color: #82786F;
      margin-bottom: 20px;
    }}

    /* Price Output Box */
    .price-alabaster-box {{
      padding: 20px;
      border-radius: var(--radius-md);
      background: #FFFFFF;
      border: 1.5px solid rgba(197, 160, 89, 0.38);
      margin-bottom: 22px;
      box-shadow: 0 4px 18px rgba(197, 160, 89, 0.1);
      text-align: center;
    }}
    .price-box-kicker {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #9E7A32;
      margin-bottom: 4px;
    }}
    .price-num-wrap {{
      display: flex;
      align-items: baseline;
      justify-content: center;
      gap: 8px;
    }}
    .price-sum {{
      font-family: var(--font-serif);
      font-size: clamp(2.3rem, 3.4vw, 3rem);
      font-weight: 700;
      color: #1C1917;
      line-height: 1.1;
      letter-spacing: -0.02em;
    }}
    .price-curr {{
      font-family: var(--font-serif);
      font-size: 1.7rem;
      font-weight: 600;
      color: #A78138;
    }}
    .price-match-pill {{
      display: inline-block;
      margin-top: 6px;
      font-size: 0.72rem;
      color: #1E6B37;
      background: #E8F5E9;
      border: 1px solid #A5D6A7;
      padding: 2px 9px;
      border-radius: var(--radius-pill);
      font-weight: 600;
    }}

    /* Breakdown Lines */
    .breakdown-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 24px;
      border-top: 1px solid rgba(197, 160, 89, 0.2);
      padding-top: 16px;
    }}
    .breakdown-row {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 8px;
      font-size: 0.84rem;
    }}
    .breakdown-lbl {{
      color: #4A443E;
      font-weight: 500;
      white-space: nowrap;
    }}
    .breakdown-dots {{
      flex: 1;
      border-bottom: 1px dotted rgba(197, 160, 89, 0.45);
      margin: 0 4px;
    }}
    .breakdown-val {{
      color: #1C1917;
      font-weight: 700;
      white-space: nowrap;
    }}
    .breakdown-detail-line {{
      font-size: 0.72rem;
      color: #82786F;
      margin-top: -6px;
      margin-bottom: 6px;
      line-height: 1.35;
    }}

    .btn-solid-wa {{
      width: 100%;
      background: linear-gradient(135deg, #1C1917 0%, #2A2520 100%);
      color: #FFFFFF;
      border: 1px solid rgba(197, 160, 89, 0.38);
      border-radius: var(--radius-pill);
      padding: 15px 22px;
      font-size: 0.92rem;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 6px 20px rgba(28, 25, 23, 0.18);
      text-decoration: none;
    }}
    .btn-solid-wa:hover {{
      background: linear-gradient(135deg, #A78138 0%, #C5A059 100%);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(197, 160, 89, 0.3);
    }}
    .btn-solid-wa svg {{
      width: 18px;
      height: 18px;
      fill: currentColor;
    }}

    /* ============================================================ */
    /* 8. CONSULTATION & CONTACTS SECTION                           */
    /* ============================================================ */
    .section-contacts {{
      padding: 90px 0 110px;
      position: relative;
    }}
    .contacts-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      margin-top: 48px;
    }}
    @media (max-width: 860px) {{
      .contacts-grid {{ grid-template-columns: 1fr; gap: 32px; }}
    }}
    .consult-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      padding: 36px;
    }}
    @media (max-width: 600px) {{
      .consult-card {{ padding: 24px 18px; }}
    }}
    .form-group {{
      margin-bottom: 18px;
    }}
    .form-label {{
      display: block;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 6px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .form-input {{
      width: 100%;
      padding: 13px 16px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: #FFFFFF;
      font-size: 0.95rem;
      outline: none;
      transition: var(--transition);
    }}
    .form-input:focus {{
      border-color: var(--coral);
      background: rgba(255, 255, 255, 0.07);
    }}

    .direct-contacts-wrap {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .direct-contact-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 24px;
      display: flex;
      align-items: center;
      gap: 20px;
      transition: var(--transition);
    }}
    .direct-contact-card:hover {{
      border-color: var(--border-hover);
      transform: translateX(4px);
    }}
    .contact-icon {{
      width: 52px;
      height: 52px;
      border-radius: var(--radius-md);
      background: var(--coral-bg);
      border: 1px solid var(--coral-border);
      color: var(--coral-light);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
    }}
    .contact-info-title {{
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin-bottom: 4px;
    }}
    .contact-info-val {{
      font-size: 1.15rem;
      font-weight: 600;
      color: #FFFFFF;
    }}

    /* ============================================================ */
    /* 9. FOOTER                                                    */
    /* ============================================================ */
    .footer {{
      background: #070709;
      border-top: 1px solid var(--border-subtle);
      padding: 48px 0;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .footer-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 20px;
    }}

    /* ============================================================ */
    /* 10. FULLSCREEN LIGHTBOX MODAL                                */
    /* ============================================================ */
    .lightbox-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(12px);
      z-index: 1000;
      display: none;
      flex-direction: column;
      justify-content: space-between;
      padding: 24px;
    }}
    .lightbox-modal.active {{
      display: flex;
    }}
    .lightbox-top-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #FFFFFF;
    }}
    .lightbox-counter {{
      font-size: 0.9rem;
      color: var(--text-muted);
    }}
    .lightbox-close-btn {{
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid var(--border-subtle);
      width: 44px;
      height: 44px;
      border-radius: 50%;
      color: #FFFFFF;
      font-size: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
    }}
    .lightbox-close-btn:hover {{
      background: var(--coral);
    }}
    .lightbox-main-view {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      margin: 16px 0;
    }}
    .lightbox-img {{
      max-width: 90vw;
      max-height: 75vh;
      object-fit: contain;
      border-radius: var(--radius-md);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
    }}
    .lightbox-arrow {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid var(--border-subtle);
      color: #FFFFFF;
      font-size: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
      z-index: 10;
    }}
    .lightbox-arrow:hover {{
      background: var(--coral);
    }}
    .lightbox-prev {{ left: 16px; }}
    .lightbox-next {{ right: 16px; }}
    .lightbox-caption-text {{
      text-align: center;
      color: var(--text-secondary);
      font-size: 0.95rem;
      padding: 10px 0;
    }}

    /* Global Responsive tweaks */
    @media (max-width: 600px) {{
      .btn {{ width: 100%; }}
      .hero-actions {{ flex-direction: column; width: 100%; }}
    }}
  </style>

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "MUAR A · Ателье интерьерного текстиля",
    "description": "Пошив штор, покрывал, римских штор и моторизованных систем для резиденций и представительских объектов в Астане.",
    "telephone": "+77710551515",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Астана",
      "addressCountry": "KZ"
    }},
    "priceRange": "₸₸₸₸"
  }}
  </script>
</head>
<body>

  <!-- ============================================================ -->
  <!-- 1. STICKY HEADER                                             -->
  <!-- ============================================================ -->
  <header class="header">
    <div class="wrap header-inner">
      <div class="logo-wrap">
        <a href="#top" class="brand-logo" onclick="window.playSilkClick(2200)">MUAR<span>·</span>A</a>
        <div class="brand-tagline">10 Знаковых Проектов Столицы</div>
      </div>

      <nav>
        <ul class="nav-links">
          <li><a href="#projects" class="nav-link active" onclick="window.playSilkClick(1800)">10 Проектов</a></li>
          <li><a href="#beforeAfter" class="nav-link" onclick="window.playSilkClick(1800)">До / После</a></li>
          <li><a href="#atelier" class="nav-link" onclick="window.playSilkClick(1800)">Цех и мастера</a></li>
          <li><a href="#calculator" class="nav-link" onclick="window.playSilkClick(1800)">Калькулятор</a></li>
          <li><a href="#contacts" class="nav-link" onclick="window.playSilkClick(1800)">Контакты</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <button type="button" class="audio-toggle-btn muar-sound-btn" id="ambientToggleBtn" onclick="toggleAmbientSound()" title="Включить атмосферную музыку салона">
          <span class="sound-wave muar-sound-wave">
            <span class="sound-bar muar-sound-bar"></span>
            <span class="sound-bar muar-sound-bar"></span>
            <span class="sound-bar muar-sound-bar"></span>
            <span class="sound-bar muar-sound-bar"></span>
          </span>
          <span class="audio-btn-text">Атмосфера салона</span>
        </button>

        <a href="https://wa.me/77710551515?text=Здравствуйте,%20MUAR%20A!%20Хочу%20проконсультироваться%20по%20текстилю%20для%20объекта." target="_blank" class="btn btn-coral btn-sm" onclick="window.playSilkClick(2400)">
          WhatsApp: +7 771 055 1515
        </a>
      </div>
    </div>
  </header>

  <!-- ============================================================ -->
  <!-- 2. EDITORIAL HERO SECTION                                    -->
  <!-- ============================================================ -->
  <section class="hero-section" id="top">
    <div class="wrap">
      <div class="hero-content">
        <div class="hero-kicker-pill">
          КОЛЛЕКЦИЯ 10 РЕАЛИЗОВАННЫХ ОБЪЕКТОВ · АСТАНА 2026
        </div>
        
        <h1 class="hero-title">
          Текстильная драматургия для <em>частных резиденций</em> и представительских пространств
        </h1>
        
        <p class="hero-lead">
          10 реализованных проектов Muar A в Астане с авторскими описаниями основателя ателье Асемгуль, детальной фотосъемкой каждого узла, собственным пошивочным цехом и 100% инженерным расчетом.
        </p>

        <div class="hero-actions">
          <a href="#projects" class="btn btn-coral" onclick="window.playSilkClick(2000)">
            Смотреть 10 проектов ↓
          </a>
          <a href="#calculator" class="btn btn-ghost" onclick="window.playSilkClick(1800)">
            Рассчитать смету онлайн
          </a>
        </div>

        <div class="hero-metrics-grid">
          <div class="metric-card">
            <div class="metric-val">10<span>.</span></div>
            <div class="metric-label">Знаковых проектов в портфолио</div>
          </div>
          <div class="metric-card">
            <div class="metric-val">25 <span>лет</span></div>
            <div class="metric-label">Опыт главного мастера цеха</div>
          </div>
          <div class="metric-card">
            <div class="metric-val">10 <span>м</span></div>
            <div class="metric-label">Высота потолков и лифт-системы</div>
          </div>
          <div class="metric-card">
            <div class="metric-val">12 <span>мес</span></div>
            <div class="metric-label">Официальная гарантия с НДС</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================ -->
  <!-- 3. THE 10 REAL PROJECTS SECTION (INTERACTIVE SHOWCASE)       -->
  <!-- ============================================================ -->
  <section class="section-projects" id="projects">
    <div class="wrap">
      <div class="section-head center">
        <div class="section-kicker">РЕАЛИЗОВАННЫЕ ПРОЕКТЫ В СТОЛИЦЕ</div>
        <h2 class="section-title">10 историй текстильного преображения</h2>
        <p class="section-subtitle">
          Подлинные истории создания текстиля от основателя ателье Асемгуль и ведущих архитекторов Казахстана: Зарины Секен, IDesign, Габидена, Динары Усмановой, Лауры Жакиной и Руслана.
        </p>
      </div>

      <!-- Category Filter -->
      <div class="projects-filter-bar">
        <button type="button" class="filter-btn active" data-filter="all" onclick="filterProjects('all', this)">Все 10 проектов (10)</button>
        <button type="button" class="filter-btn" data-filter="b2c" onclick="filterProjects('b2c', this)">Частные резиденции &amp; Пентхаусы (5)</button>
        <button type="button" class="filter-btn" data-filter="villa" onclick="filterProjects('villa', this)">Загородные виллы (High-Ceiling) (3)</button>
        <button type="button" class="filter-btn" data-filter="b2b" onclick="filterProjects('b2b', this)">Контрактные &amp; B2B объекты (2)</button>
      </div>

      <!-- Master-Detail Interactive Showcase -->
      <div class="showcase-stage" id="showcaseStage">
        
        <!-- Left: Project Selector Rail -->
        <div class="stage-nav">
          <div class="stage-nav-header">
            <span>Выберите проект</span>
            <span class="coral-text">10 ОБЪЕКТОВ</span>
          </div>
          <div id="projectNavItems">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Right: Active Project Detail Stage -->
        <div class="stage-view" id="activeStageView">
          <!-- Rendered via JS -->
        </div>

      </div>

      <!-- 10 Projects Visual Grid -->
      <div class="projects-grid-section">
        <div class="section-kicker" style="margin-bottom: 20px;">КАТАЛОГ ВСЕХ 10 ОБЪЕКТОВ ДЛЯ БЫСТРОГО ОБЗОРА</div>
        <div class="projects-grid" id="projectsGrid">
          <!-- Rendered via JS -->
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================ -->
  <!-- 4. BEFORE & AFTER TRANSFORMATION LAB                         -->
  <!-- ============================================================ -->
  <section class="section-ba" id="beforeAfter">
    <div class="wrap">
      <div class="section-head center">
        <div class="section-kicker">ИНТЕРАКТИВНОЕ СРАВНЕНИЕ</div>
        <h2 class="section-title">Преображение пространства: До и После</h2>
        <p class="section-subtitle">
          Потяните бегунок в центре фотографии, чтобы увидеть, как профессиональный текстиль меняет геометрию, акустику и освещение интерьера.
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
            <h4 id="baHeroCaptionTitle">Проект 01: Драматургия Red &amp; White (Резиденция)</h4>
            <p id="baHeroCaptionDesc">Черновой интерьер vs законченный кутюрный шик: портьеры на светозащитной подкладке, авторская вставка с птицами и стёганое покрывало.</p>
          </div>
          <a href="https://wa.me/77710551515?text=Здравствуйте,%20MUAR%20A!%20Хочу%20получить%20проект%20преображения%20для%20моего%20интерьера." target="_blank" class="btn btn-coral btn-sm">
            Заказать выезд декоратора
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================ -->
  <!-- 5. ATELIER WORKSHOP & CRAFTSMANSHIP (REAL VIDEOS)            -->
  <!-- ============================================================ -->
  <section class="section-atelier" id="atelier">
    <div class="wrap">
      <div class="section-head center">
        <div class="section-kicker">КУТЮРНЫЙ ПОШИВ ПО СТАНДАРТАМ РК</div>
        <h2 class="section-title">Собственный швейный цех и инженерия</h2>
        <p class="section-subtitle">
          Мы не передаем заказы субподрядчикам. Каждый шов, подкладка и узел моторизации создаются нашими штатными мастерами под строгим контролем качества.
        </p>
      </div>

      <!-- Real Video Trio -->
      <div class="videos-trio-grid">
        
        <!-- Video 1: Master Maral -->
        <article class="video-card">
          <div class="video-player-wrap">
            <video src="assets/muar/craft-maral.mp4" controls preload="metadata" poster="assets/muar/portfolio/garden-14.webp" playsinline></video>
          </div>
          <div class="video-card-body">
            <div class="video-card-tag">МАСТЕР ЦЕХА · 25 ЛЕТ ОПЫТА</div>
            <h3 class="video-card-title">Мастер Марал: Искусство ручной складки</h3>
            <p class="video-card-desc">
              Филигранная ручная сборка складок, невидимый нижний подгиб 10 см с утяжелителями и использование немецких армированных нитей Gütermann.
            </p>
          </div>
        </article>

        <!-- Video 2: Villa Lift Systems -->
        <article class="video-card">
          <div class="video-player-wrap">
            <video src="assets/muar/villa-lift-system.mp4" controls preload="metadata" poster="assets/muar/portfolio/IMG_6721.webp" playsinline></video>
          </div>
          <div class="video-card-body">
            <div class="video-card-tag">ИНЖЕНЕРИЯ ВЫСОТЫ · 10 МЕТРОВ</div>
            <h3 class="video-card-title">Лифт-системы для нестандартных вилл</h3>
            <p class="video-card-desc">
              Спроектированные и смонтированные Muar A трубчатые моторы и стальные тросы для подъема и спуска тяжелых портьер на 10-метровой высоте (Виллы «Темный Рыцарь»).
            </p>
          </div>
        </article>

        <!-- Video 3: Order Journey -->
        <article class="video-card">
          <div class="video-player-wrap">
            <video src="assets/muar/order-journey.mp4" controls preload="metadata" poster="assets/muar/portfolio/1.webp" playsinline></video>
          </div>
          <div class="video-card-body">
            <div class="video-card-tag">ПУТЬ ЗАКАЗА «ПОД КЛЮЧ»</div>
            <h3 class="video-card-title">От выезда с образцами до отпаривания</h3>
            <p class="video-card-desc">
              Как создается проект: замер лазерным дальномером, подбор образцов в вашем освещении, пошив в цехе и финальная навеска с отпариванием парогенератором.
            </p>
          </div>
        </article>

      </div>

      <!-- 6 Standards of Atelier Craft -->
      <div class="pillars-grid">
        <div class="pillar-item">
          <div class="pillar-num">01</div>
          <div class="pillar-content">
            <h5>Нити Gütermann (Германия)</h5>
            <p>Высокопрочные армированные нити, которые не рвутся при стирке, химчистке и интенсивной эксплуатации.</p>
          </div>
        </div>
        <div class="pillar-item">
          <div class="pillar-num">02</div>
          <div class="pillar-content">
            <h5>Потайной подгиб 10 см</h5>
            <p>Двойной широкий подгиб низа с потайным швом обеспечивает ровные монументальные фалды без заломов.</p>
          </div>
        </div>
        <div class="pillar-item">
          <div class="pillar-num">03</div>
          <div class="pillar-content">
            <h5>Подкладка Dimout / Blackout</h5>
            <p>Обязательная светозащитная подкладка защищает лицевую ткань от выгорания на солнце и дает красивую полноту складок.</p>
          </div>
        </div>
        <div class="pillar-item">
          <div class="pillar-num">04</div>
          <div class="pillar-content">
            <h5>Ручная складка 1:2.0 / 1:2.5</h5>
            <p>Индивидуальная ручная заложительная складка штор и тюля вместо дешевой китайской шторной ленты.</p>
          </div>
        </div>
        <div class="pillar-item">
          <div class="pillar-num">05</div>
          <div class="pillar-content">
            <h5>Электрокарнизы Somfy (Франция)</h5>
            <p>Бесшумные моторизованные карнизы с управлением от пульта, смартфона и голосовых ассистентов Алиса/Siri.</p>
          </div>
        </div>
        <div class="pillar-item">
          <div class="pillar-num">06</div>
          <div class="pillar-content">
            <h5>Договор и НДС 12%</h5>
            <p>Полный пакет закрывающих документов (ЭСФ, акты выполненных работ, сертификаты негорючести КМ1 для B2B).</p>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================ -->
  <!-- 6. EXACT ASENGUL CALCULATION ENGINE (ALABASTER & BRASS)       -->
  <!-- ============================================================ -->
  <section class="section-calc" id="calculator">
    <div class="wrap">
      <div class="section-head center">
        <div class="section-kicker">ОНЛАЙН-РАСЧЕТ СМЕТЫ · АТЕЛЬЕ АСЕНГУЛЬ</div>
        <h2 class="section-title">Калькулятор текстильного оформления</h2>
        <p class="section-subtitle">
          Строгие производственные регламенты Асенгуль: европейский текстиль, цеховой крой по ГОСТу РК, профильные карнизы и скульптурное отпаривание без скрытых наценок.
        </p>
      </div>

      <div class="calc-alabaster-card">
        
        <!-- Direction Tabs (Curtains / Roman / Bedspread / B2B) -->
        <div class="calc-direction-bar">
          <button type="button" class="dir-tab-btn active" data-product="curtain" onclick="setProduct('curtain', this)">
            <span>Портьеры в пол</span>
            <span class="badge-exact">508 800 ₸ тест</span>
          </button>
          <button type="button" class="dir-tab-btn" data-product="roman" onclick="setProduct('roman', this)">
            <span>Римские шторы</span>
          </button>
          <button type="button" class="dir-tab-btn" data-product="bedspread" onclick="setProduct('bedspread', this)">
            <span>Покрывало стёганое</span>
          </button>
          <button type="button" class="dir-tab-btn" data-product="b2b" onclick="setProduct('b2b', this)">
            <span>B2B Контракт (НДС 12%)</span>
          </button>
        </div>

        <div class="calc-body-grid">
          
          <!-- Left: Controls -->
          <div class="calc-controls-pane">
            
            <!-- Fabric Selector (3x2 Grid = 6 Noble Fabrics) -->
            <div id="fabricChoiceSection">
              <div class="calc-field-label">Коллекция благородных тканей (3×2)</div>
              <div class="fabric-grid-3x2" id="fabricOptionsGrid">
                <!-- 1 -->
                <button type="button" class="fabric-select-card" data-fab="velvet_dedar" onclick="setFabric('velvet_dedar', this)">
                  <div class="fabric-card-row-top">
                    <div>
                      <div class="fabric-title-text">Бархат Dedar Milano</div>
                      <div class="fabric-country-sub">Италия · Haute Couture</div>
                    </div>
                    <div class="fabric-cost-badge">88 000 ₸/м</div>
                  </div>
                  <div class="fabric-detail-desc">520 г/м², глубокий матовый ворс, роскошная драпировка</div>
                  <div class="fabric-active-dot">✓</div>
                </button>

                <!-- 2 -->
                <button type="button" class="fabric-select-card" data-fab="wild_silk" onclick="setFabric('wild_silk', this)">
                  <div class="fabric-card-row-top">
                    <div>
                      <div class="fabric-title-text">Натуральный дикий шелк</div>
                      <div class="fabric-country-sub">Франция · Эксклюзив</div>
                    </div>
                    <div class="fabric-cost-badge">72 000 ₸/м</div>
                  </div>
                  <div class="fabric-detail-desc">Фактурный шантунг ручной выделки с жемчужным отливом</div>
                  <div class="fabric-active-dot">✓</div>
                </button>

                <!-- 3 (Default Satin Spain) -->
                <button type="button" class="fabric-select-card active" data-fab="satin_spain" onclick="setFabric('satin_spain', this)">
                  <div class="fabric-card-row-top">
                    <div>
                      <div class="fabric-title-text">Матовый плотный сатин</div>
                      <div class="fabric-country-sub">Испания · Базовый выбор</div>
                    </div>
                    <div class="fabric-cost-badge">55 000 ₸/м</div>
                  </div>
                  <div class="fabric-detail-desc">Тяжелая пластика складок, устойчивость к УФ-лучам Астаны</div>
                  <div class="fabric-active-dot">✓</div>
                </button>

                <!-- 4 -->
                <button type="button" class="fabric-select-card" data-fab="linen_belgium" onclick="setFabric('linen_belgium', this)">
                  <div class="fabric-card-row-top">
                    <div>
                      <div class="fabric-title-text">Текстурированный лен с мулине</div>
                      <div class="fabric-country-sub">Бельгия · Эко-премиум</div>
                    </div>
                    <div class="fabric-cost-badge">48 000 ₸/м</div>
                  </div>
                  <div class="fabric-detail-desc">Природная выразительная фактура с тонкой нитью мулине</div>
                  <div class="fabric-active-dot">✓</div>
                </button>

                <!-- 5 -->
                <button type="button" class="fabric-select-card" data-fab="dimout_germany" onclick="setFabric('dimout_germany', this)">
                  <div class="fabric-card-row-top">
                    <div>
                      <div class="fabric-title-text">Светозащитный Dimout / Blackout</div>
                      <div class="fabric-country-sub">Германия · 99% затемнение</div>
                    </div>
                    <div class="fabric-cost-badge">42 000 ₸/м</div>
                  </div>
                  <div class="fabric-detail-desc">Трехслойное плетение, термоизоляция и защита мебели</div>
                  <div class="fabric-active-dot">✓</div>
                </button>

                <!-- 6 -->
                <button type="button" class="fabric-select-card" data-fab="tulle_france" onclick="setFabric('tulle_france', this)">
                  <div class="fabric-card-row-top">
                    <div>
                      <div class="fabric-title-text">Французский тюль-вуаль</div>
                      <div class="fabric-country-sub">Турция / Франция · Гардина</div>
                    </div>
                    <div class="fabric-cost-badge">28 000 ₸/м</div>
                  </div>
                  <div class="fabric-detail-desc">Воздушное полотно, мягко рассеивающее яркий свет</div>
                  <div class="fabric-active-dot">✓</div>
                </button>
              </div>
            </div>

            <!-- Curtain Controls (Formula 1) -->
            <div id="curtainSection">
              <div class="calc-field-label">Геометрия окна и карниза (Формула 1)</div>
              <div class="slider-surface-box">
                <div class="slider-surface-top">
                  <span class="slider-surface-title">Ширина карниза (м)</span>
                  <span class="slider-surface-val"><span id="widthOut">3.2</span> м</span>
                </div>
                <input type="range" class="slider-brass-input" id="widthRange" min="1.0" max="8.0" step="0.1" value="3.2" oninput="updateCurtainWidth(this.value)">
                <div class="slider-surface-sub">
                  <span>1.0 м</span>
                  <span>Базовый тест: 3.2 м (расход ткани 6.4 м)</span>
                  <span>8.0 м</span>
                </div>
              </div>

              <!-- Options -->
              <div class="calc-field-group" style="margin-top: 18px;">
                <div class="calc-field-label">Дополнительные опции пошива</div>
                <div style="display: flex; flex-direction: column; gap: 8px;">
                  <label class="calc-check-brass-row">
                    <input type="checkbox" id="checkLining" onchange="recalc()">
                    <span>Сатиновый подклад по ГОСТу РК (+10 900 ₸/м расхода — защита ткани)</span>
                  </label>
                  <label class="calc-check-brass-row">
                    <input type="checkbox" id="checkTulle" onchange="recalc()">
                    <span>Второй ряд: Французская вуаль со сборкой 2.0 (+14 500 ₸/м)</span>
                  </label>
                  <label class="calc-check-brass-row">
                    <input type="checkbox" id="checkSomfy" onchange="recalc()">
                    <span>Электрокарниз Somfy Ultra с бесшумным мотором и пультом (+85 000 ₸)</span>
                  </label>
                </div>
              </div>
            </div>

            <!-- Roman Controls (Formula 2) -->
            <div id="romanSection" style="display: none;">
              <div class="calc-field-label">Параметры римской шторы (Формула 2)</div>
              <div class="slider-surface-box" style="margin-bottom: 12px;">
                <div class="slider-surface-top">
                  <span class="slider-surface-title">Ширина механизма (м)</span>
                  <span class="slider-surface-val"><span id="romanWidthOut">1.6</span> м</span>
                </div>
                <input type="range" class="slider-brass-input" id="romanWidthRange" min="0.8" max="3.0" step="0.1" value="1.6" oninput="updateRomanDims()">
                <div class="slider-surface-sub">
                  <span>0.8 м</span>
                  <span>Цепочный подъемный механизм: 32 000 ₸/м</span>
                  <span>3.0 м</span>
                </div>
              </div>

              <div class="slider-surface-box">
                <div class="slider-surface-top">
                  <span class="slider-surface-title">Высота изделия (м)</span>
                  <span class="slider-surface-val"><span id="romanHeightOut">2.8</span> м</span>
                </div>
                <input type="range" class="slider-brass-input" id="romanHeightRange" min="1.2" max="3.6" step="0.1" value="2.8" oninput="updateRomanDims()">
                <div class="slider-surface-sub">
                  <span>1.2 м</span>
                  <span>Расход: (Высота + 0.3м) × 1.15 = 3.56 пог. м</span>
                  <span>3.6 м</span>
                </div>
              </div>
            </div>

            <!-- Bedspread Controls (Formula 3) -->
            <div id="bedspreadSection" style="display: none;">
              <div class="calc-field-label">5 порогов сложности покрывала (Формула 3)</div>
              <div class="tier-stack-list">
                <button type="button" class="tier-choice-btn" data-tier="0" onclick="setBedspreadTier(0, this)">
                  <div>
                    <div class="tier-head-txt">Порог 1 · Минимализм (Линейная стёжка)</div>
                    <div class="tier-sub-txt">2.2 × 2.4 м, ткань 2.8 м, холлофайбер 150г, хлопок</div>
                  </div>
                  <div class="tier-tag-pill">Пошив 70k ₸</div>
                </button>
                <button type="button" class="tier-choice-btn" data-tier="1" onclick="setBedspreadTier(1, this)">
                  <div>
                    <div class="tier-head-txt">Порог 2 · Классика (Стёжка «Ромбы»)</div>
                    <div class="tier-sub-txt">2.4 × 2.5 м, ткань 3.0 м, синтепон 150г, сатиновый подклад</div>
                  </div>
                  <div class="tier-tag-pill">Пошив 85k ₸</div>
                </button>
                <button type="button" class="tier-choice-btn active" data-tier="2" onclick="setBedspreadTier(2, this)">
                  <div>
                    <div class="tier-head-txt">Порог 3 · Стандарт Асенгуль (Фигурная стёжка + Кант)</div>
                    <div class="tier-sub-txt">2.4 × 2.6 м (кровать 180×200), ткань 3.2 м, синтепон 200 г/м²</div>
                  </div>
                  <div class="tier-tag-pill">Пошив 100k ₸</div>
                </button>
                <button type="button" class="tier-choice-btn" data-tier="3" onclick="setBedspreadTier(3, this)">
                  <div>
                    <div class="tier-head-txt">Порог 4 · Премиум King Size (Вензельная стёжка)</div>
                    <div class="tier-sub-txt">2.6 × 2.7 м, ткань 3.6 м, синтепон 250г, авторский вензель</div>
                  </div>
                  <div class="tier-tag-pill">Пошив 125k ₸</div>
                </button>
                <button type="button" class="tier-choice-btn" data-tier="4" onclick="setBedspreadTier(4, this)">
                  <div>
                    <div class="tier-head-txt">Порог 5 · Haute Couture (Двустороннее + 2 подушки)</div>
                    <div class="tier-sub-txt">2.6 × 2.8 м, ткань 4.0 м, пух + синтепон 250г, компаньон, 2 подушки 50×70</div>
                  </div>
                  <div class="tier-tag-pill">Пошив 160k ₸</div>
                </button>
              </div>
            </div>

            <!-- B2B Controls (Formula 4) -->
            <div id="b2bSection" style="display: none;">
              <div class="calc-field-label">Контрактные пространства B2B (Trevira CS · НДС 12%)</div>
              <div class="b2b-contract-grid">
                <button type="button" class="b2b-contract-card active" data-b2bpkg="b2b_executive" onclick="setB2bPackage('b2b_executive', this)">
                  <div class="tier-head-txt">Кабинет руководителя</div>
                  <div class="tier-sub-txt">Trevira CS Dimout, электрокарниз 3.2 м, КМ1</div>
                  <div class="tier-tag-pill" style="margin-top: 8px;">580k ₸ / кабинет</div>
                </button>
                <button type="button" class="b2b-contract-card" data-b2bpkg="b2b_restaurant" onclick="setB2bPackage('b2b_restaurant', this)">
                  <div class="tier-head-txt">Ресторан / Лаунж</div>
                  <div class="tier-sub-txt">Акустический бархат Trevira CS, износостойкость >60k</div>
                  <div class="tier-tag-pill" style="margin-top: 8px;">720k ₸ / зал</div>
                </button>
                <button type="button" class="b2b-contract-card" data-b2bpkg="b2b_hotel" onclick="setB2bPackage('b2b_hotel', this)">
                  <div class="tier-head-txt">Бутик-отель / Номер</div>
                  <div class="tier-sub-txt">Blackout + негорючая вуаль + стёганое саше</div>
                  <div class="tier-tag-pill" style="margin-top: 8px;">460k ₸ / номер</div>
                </button>
                <button type="button" class="b2b-contract-card" data-b2bpkg="b2b_screens" onclick="setB2bPackage('b2b_screens', this)">
                  <div class="tier-head-txt">Конференц-зал B2B</div>
                  <div class="tier-sub-txt">Моторизованный Screen 3% с защитой от бликов</div>
                  <div class="tier-tag-pill" style="margin-top: 8px;">390k ₸ / зона</div>
                </button>
              </div>

              <div class="slider-surface-box" style="margin-top: 14px;">
                <div class="slider-surface-top">
                  <span class="slider-surface-title">Количество помещений / окон</span>
                  <span class="slider-surface-val"><span id="b2bRoomsOut">1</span> шт.</span>
                </div>
                <input type="range" class="slider-brass-input" id="b2bRoomsRange" min="1" max="20" step="1" value="1" oninput="updateB2BRooms(this.value)">
                <div class="slider-surface-sub">
                  <span>1 помещение</span>
                  <span>От 5 помещений корпоративная скидка 10%</span>
                  <span>20 помещений</span>
                </div>
              </div>
            </div>

          </div>

          <!-- Right: Summary Pane -->
          <div class="calc-summary-pane">
            <div>
              <div class="summary-kicker-bar">
                <span class="summary-atelier-name">MUAR A · Ателье Асенгуль</span>
                <span class="summary-formula-tag" id="calcFormulaTag">Формула 1 · Портьеры в пол</span>
              </div>

              <h4 class="summary-heading-h4" id="calcProductTitle">Портьеры в пол (Комплект)</h4>
              <p class="summary-lead-desc" id="calcProductDesc">Рулонная высота 3.2 м, сборка 2.0, цеховой крой и скульптурное отпаривание</p>

              <!-- Price Box -->
              <div class="price-alabaster-box">
                <div class="price-box-kicker">Итоговая смета «под ключ»</div>
                <div class="price-num-wrap">
                  <div class="price-sum" id="priceOut">508 800</div>
                  <div class="price-curr">₸</div>
                </div>
                <div id="targetPill" class="price-match-pill">✓ Контрольный тест Асенгуль: ровно 508 800 ₸!</div>
              </div>

              <!-- Itemized Breakdown -->
              <div class="breakdown-list" id="breakdownList">
                <!-- Populated via JS -->
              </div>
            </div>

            <div>
              <button type="button" class="btn-solid-wa" id="whatsappCalcBtn" onclick="sendCalcToWhatsApp()">
                <svg viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.694.074-2.122-.519-1.748-.726-2.883-2.508-2.97-2.624-.087-.116-.711-.945-.711-1.804s.449-1.28.608-1.455c.16-.175.348-.218.464-.218.116 0 .232.001.333.006.107.005.25-.041.391.298.145.348.493 1.202.536 1.29.043.087.072.189.014.305-.058.116-.087.189-.174.29-.087.102-.183.228-.261.306-.087.087-.178.182-.077.355.101.174.45 0.742.966 1.202.664.592 1.224.775 1.398.862.174.087.276.073.377-.044.102-.116.435-.508.551-.682.116-.174.232-.145.391-.087s1.014.478 1.188.565c.174.087.29.13.333.203.044.072.044.42-.1 1.025zM12 2C6.477 2 2 6.477 2 12c0 1.891.524 3.662 1.435 5.176L2 22l4.982-1.309A9.957 9.957 0 0012 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg>
                <span id="waBtnLabelText">Зафиксировать расчет 508 800 ₸ в WhatsApp</span>
              </button>
              <div style="font-size: 0.74rem; color: #82786F; text-align: center; margin-top: 10px;">
                ✦ Расчет фиксируется в договоре. Выезд декоратора с образцами тканей в Астане бесплатно.
              </div>
            </div>

          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================ -->
  <!-- 7. CONSULTATION & CONTACTS SECTION                           -->
  <!-- ============================================================ -->
  <section class="section-contacts" id="contacts">
    <div class="wrap">
      <div class="section-head center">
        <div class="section-kicker">СВЯЗЬ С АТЕЛЬЕ И ЗАМЕР</div>
        <h2 class="section-title">Пригласите декоратора на объект в Астане</h2>
        <p class="section-subtitle">
          Декоратор привезет кейс с живыми образцами тканей, выполнит лазерный замер окон и разработает точный текстильный сценарий под ваш интерьер.
        </p>
      </div>

      <div class="contacts-grid">
        
        <!-- Fast Booking Form -->
        <div class="consult-card">
          <form id="consultForm" onsubmit="handleConsultSubmit(event)">
            <div class="form-group">
              <label class="form-label">Ваше имя</label>
              <input type="text" class="form-input" id="clientName" placeholder="Например: Айгерим" required>
            </div>
            <div class="form-group">
              <label class="form-label">Номер телефона / WhatsApp</label>
              <input type="tel" class="form-input" id="clientPhone" placeholder="+7 (771) 000-00-00" required>
            </div>
            <div class="form-group">
              <label class="form-label">Адрес или ЖК в Астане</label>
              <input type="text" class="form-input" id="clientAddress" placeholder="Например: ЖК Vivaldi, пентхаус">
            </div>
            <div class="form-group">
              <label class="form-label">Удобное время для замера</label>
              <input type="text" class="form-input" id="clientTime" placeholder="Например: Завтра после 14:00">
            </div>
            <button type="submit" class="btn btn-coral" style="width: 100%; margin-top: 8px;">
              Записаться на выезд с образцами
            </button>
          </form>
        </div>

        <!-- Direct Contacts -->
        <div class="direct-contacts-wrap">
          
          <a href="https://wa.me/77710551515?text=Здравствуйте,%20MUAR%20A!%20Хочу%20записаться%20на%20консультацию." target="_blank" class="direct-contact-card" onclick="window.playSilkClick(2100)">
            <div class="contact-icon">💬</div>
            <div>
              <div class="contact-info-title">WhatsApp / Telegram Ателье</div>
              <div class="contact-info-val">+7 771 055 1515</div>
              <div style="font-size: 0.8rem; color: var(--coral-light); margin-top: 2px;">Написать напрямую основателю Асемгуль →</div>
            </div>
          </a>

          <a href="tel:+77710551515" class="direct-contact-card" onclick="window.playSilkClick(2100)">
            <div class="contact-icon">📞</div>
            <div>
              <div class="contact-info-title">Прямой телефон в Астане</div>
              <div class="contact-info-val">+7 771 055 1515</div>
              <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 2px;">Ежедневно с 09:00 до 20:00</div>
            </div>
          </a>

          <div class="direct-contact-card">
            <div class="contact-icon">🏛️</div>
            <div>
              <div class="contact-info-title">Шоурум и швейный цех</div>
              <div class="contact-info-val">г. Астана, пр. Мәңгілік Ел</div>
              <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 2px;">Прием по предварительной записи</div>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>

  <!-- ============================================================ -->
  <!-- 8. FOOTER                                                    -->
  <!-- ============================================================ -->
  <footer class="footer">
    <div class="wrap footer-inner">
      <div>
        <div style="font-family: var(--font-serif); font-size: 1.3rem; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">
          MUAR<span class="coral-text">·</span>A
        </div>
        <div>Ателье интерьерного текстиля и контрактных решений · Астана 2026</div>
      </div>
      <div>
        Официальный договор, закрывающие документы с НДС 12%, гарантия 12 месяцев.
      </div>
      <div>
        <a href="#top" style="color: var(--coral-light); font-weight: 600;" onclick="window.playSilkClick(2000)">Наверх ↑</a>
      </div>
    </div>
  </footer>

  <!-- ============================================================ -->
  <!-- 9. FULLSCREEN LIGHTBOX MODAL (PREMIUM ARCHITECTURE)          -->
  <!-- ============================================================ -->
  <div class="muar-lightbox" id="muarLightbox" role="dialog" aria-modal="true" aria-label="Полноэкранный просмотр фото интерьера">
    <div class="muar-lightbox-header">
      <div class="muar-lightbox-counter-pill">
        <span>Кадр</span>
        <span class="muar-lightbox-counter-current" id="muarLightboxCounter">01 / 09</span>
      </div>
      <div class="muar-lightbox-title-center" id="muarLightboxProjectTitle">
        MUAR A · Архитектура Текстиля
      </div>
      <button type="button" class="muar-lightbox-close-btn" id="muarLightboxClose" onclick="closeLightbox()" title="Закрыть (Esc)">
        <svg width="20" height="20" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.2" fill="none">
          <path d="M18 6L6 18M6 6l12 12" stroke-linecap="round"/>
        </svg>
      </button>
    </div>

    <div class="muar-lightbox-stage" id="muarLightboxStage">
      <button type="button" class="muar-lightbox-nav muar-lightbox-prev" id="muarLightboxPrev" onclick="prevLightboxPhoto()" title="Предыдущее фото (←)">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
          <path d="M15 18l-6-6 6-6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <div class="muar-lightbox-img-wrap" id="muarLightboxImgWrap">
        <img id="muarLightboxImg" class="muar-lightbox-img" src="" alt="Деталь интерьера" draggable="false">
      </div>
      <button type="button" class="muar-lightbox-nav muar-lightbox-next" id="muarLightboxNext" onclick="nextLightboxPhoto()" title="Следующее фото (→)">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
          <path d="M9 18l6-6-6-6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
    </div>

    <div class="muar-lightbox-footer">
      <div class="muar-lightbox-caption-card">
        <span class="muar-lightbox-caption-project" id="muarLightboxProjectBadge">ПРОЕКТ 01</span>
        <span class="muar-lightbox-caption-divider"></span>
        <span class="muar-lightbox-caption-location" id="muarLightboxLocation">г. Астана · Частная резиденция</span>
        <span class="muar-lightbox-caption-divider"></span>
        <span class="muar-lightbox-caption-detail" id="muarLightboxDetail">Кутюрное текстильное оформление</span>
      </div>
    </div>
  </div>

  <!-- Audio Asset -->
  <audio id="ambientAudio" loop preload="none">
    <source src="assets/muar/ambient-lounge.mp3" type="audio/mpeg">
  </audio>

  <!-- MUAR A Tactile Motion & Interactive Engine Scripts -->
  <script src="scratch/interactive_engine.js"></script>

  <!-- ============================================================ -->
  <!-- 10. CLIENT ENGINE JAVASCRIPT                                 -->
  <!-- ============================================================ -->
  <script>
    /* ------------------------------------------------------------- */
    /* 1. 10 REAL PROJECTS DATA MODEL                                */
    /* ------------------------------------------------------------- */
    var PROJECTS_DATA = {projects_json};

    var currentProjectId = 1;
    var currentFilter = 'all';
    var activePhotoIndex = 0;

    /* ------------------------------------------------------------- */
    /* 2. SOUND & WEB AUDIO ENGINE                                   */
    /* ------------------------------------------------------------- */
    var audioCtx = null;
    var isAudioPlaying = false;
    var ambientAudioEl = document.getElementById('ambientAudio');

    function getAudioCtx() {{
      if (!audioCtx) {{
        var AC = window.AudioContext || window.webkitAudioContext;
        if (AC) audioCtx = new AC();
      }}
      if (audioCtx && audioCtx.state === 'suspended') {{
        audioCtx.resume();
      }}
      return audioCtx;
    }}

    window.playSilkClick = function(pitch) {{
      try {{
        var ctx = getAudioCtx();
        if (!ctx) return;
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        var f = pitch || 1800;
        osc.type = 'sine';
        osc.frequency.setValueAtTime(f, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(f * 0.35, ctx.currentTime + 0.035);
        gain.gain.setValueAtTime(0.03, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.035);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.04);
      }} catch (e) {{}}
    }};

    function toggleAmbientSound() {{
      getAudioCtx();
      var btn = document.getElementById('ambientToggleBtn');
      if (!ambientAudioEl) return;

      if (isAudioPlaying) {{
        ambientAudioEl.pause();
        isAudioPlaying = false;
        if (btn) btn.classList.remove('active');
      }} else {{
        ambientAudioEl.volume = 0.45;
        var p = ambientAudioEl.play();
        if (p !== undefined) {{
          p.then(function() {{
            isAudioPlaying = true;
            if (btn) btn.classList.add('active');
          }}).catch(function(e) {{
            console.log('Audio requires user gesture:', e);
          }});
        }}
      }}
      window.playSilkClick(2200);
    }}
    window.toggleAmbientSound = toggleAmbientSound;

    /* ------------------------------------------------------------- */
    /* 3. PROJECT SHOWCASE ENGINE                                    */
    /* ------------------------------------------------------------- */
    function renderProjectNav() {{
      var rail = document.getElementById('projectNavItems');
      if (!rail) return;
      rail.innerHTML = '';

      PROJECTS_DATA.forEach(function(p) {{
        if (currentFilter !== 'all' && p.cat !== currentFilter) return;

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'nav-item-btn' + (p.id === currentProjectId ? ' active' : '');
        btn.onclick = function() {{
          selectProject(p.id);
          window.playSilkClick(1900);
        }};

        btn.innerHTML = 
          '<div class="nav-num-badge">' + p.num + '</div>' +
          '<div class="nav-meta">' +
            '<div class="nav-project-title">' + p.title + '</div>' +
            '<div class="nav-project-collab">' + p.collaborator + '</div>' +
          '</div>';

        rail.appendChild(btn);
      }});
    }}

    function renderStageView() {{
      var view = document.getElementById('activeStageView');
      if (!view) return;

      var p = PROJECTS_DATA.find(function(item) {{ return item.id === currentProjectId; }});
      if (!p) p = PROJECTS_DATA[0];

      // Media HTML: Before/After or primary photo
      var mediaHtml = '';
      if (p.has_ba) {{
        mediaHtml = 
          '<div class="stage-media-wrap">' +
            '<div class="ba-slider-container muar-ba-container" id="stageBaSlider" role="slider" tabindex="0" aria-label="Интерактивное сравнение До и После" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">' +
              '<div class="ba-after-layer muar-ba-layer muar-ba-after">' +
                '<img src="' + p.ba_after + '" alt="' + p.title + '" draggable="false">' +
              '</div>' +
              '<div class="ba-before-layer muar-ba-layer muar-ba-before" id="stageBaBeforeLayer">' +
                '<img src="' + p.ba_before + '" alt="Интерьер до оформления" draggable="false">' +
              '</div>' +
              '<div class="ba-handle-line muar-ba-divider" id="stageBaHandleLine">' +
                '<div class="ba-handle-grip muar-ba-grip" tabindex="0" role="slider" aria-label="Разделитель До и После">' +
                  '<svg class="muar-ba-arrows-svg" viewBox="0 0 24 24" width="22" height="22">' +
                    '<path d="M8.5 7.5L4 12l4.5 4.5M15.5 7.5L20 12l-4.5 4.5" stroke="#1A150B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>' +
                  '</svg>' +
                '</div>' +
              '</div>' +
              '<div class="ba-tag ba-tag-before muar-ba-badge muar-ba-badge-before">' +
                '<span class="muar-ba-badge-dot"></span>' +
                '<span>Интерьер до текстиля</span>' +
              '</div>' +
              '<div class="ba-tag ba-tag-after muar-ba-badge muar-ba-badge-after">' +
                '<span class="muar-ba-badge-dot"></span>' +
                '<span>Кутюрное преображение MUAR A</span>' +
              '</div>' +
            '</div>' +
          '</div>';
      }} else {{
        var primaryPhoto = p.photos[activePhotoIndex] || p.photos[0];
        mediaHtml = 
          '<div class="stage-media-wrap" onclick="openLightbox(' + activePhotoIndex + ')" style="cursor: pointer;" title="Нажмите, чтобы развернуть во весь экран">' +
            '<img src="' + primaryPhoto.src + '" alt="' + primaryPhoto.alt + '" class="stage-primary-img" id="stagePrimaryImg">' +
          '</div>';
      }}

      // Specs chips
      var specsHtml = p.specs.map(function(s) {{
        return '<span class="spec-chip">' + s + '</span>';
      }}).join('');

      // Thumbs strip
      var thumbsHtml = p.photos.map(function(ph, idx) {{
        return '<button type="button" class="gallery-thumb-btn' + (idx === activePhotoIndex ? ' active' : '') + '" onclick="selectPhoto(' + idx + ')">' +
          '<img src="' + ph.src + '" alt="' + ph.alt + '" loading="lazy">' +
        '</button>';
      }}).join('');

      view.innerHTML = 
        mediaHtml +
        '<div class="stage-info-header">' +
          '<div class="project-header-top">' +
            '<div class="stage-badge">' + p.badge + '</div>' +
            '<div class="stage-collab-pill">' + p.collaborator + '</div>' +
          '</div>' +
          '<h3 class="stage-title">' + p.title + '</h3>' +
          '<div class="stage-desc">' + p.desc + '</div>' +
          '<div class="stage-specs">' + specsHtml + '</div>' +
        '</div>' +
        '<div class="stage-gallery-wrap">' +
          '<div class="gallery-label-row">' +
            '<span class="gallery-label">Детализация проекта (' + p.photos.length + ' фото)</span>' +
            '<button type="button" class="gallery-lightbox-trigger" onclick="openLightbox(' + activePhotoIndex + ')">' +
              '⤢ Развернуть галерею' +
            '</button>' +
          '</div>' +
          '<div class="gallery-strip">' + thumbsHtml + '</div>' +
        '</div>';

      // Re-bind BA slider if present
      if (p.has_ba) {{
        if (window.MuarInteractive && window.MuarInteractive.MuarBeforeAfterSlider) {{
          window.MuarInteractive.stageSlider = new window.MuarInteractive.MuarBeforeAfterSlider('stageBaSlider', {{
            soundEngine: window.MuarInteractive.soundscape
          }});
        }} else {{
          initBaSlider('stageBaSlider', 'stageBaBeforeLayer', 'stageBaHandleLine');
        }}
      }}
    }}

    function selectProject(id) {{
      currentProjectId = id;
      activePhotoIndex = 0;
      renderProjectNav();
      renderStageView();
    }}

    function selectPhoto(idx) {{
      activePhotoIndex = idx;
      var p = PROJECTS_DATA.find(function(item) {{ return item.id === currentProjectId; }});
      if (!p) return;

      var stageImg = document.getElementById('stagePrimaryImg');
      if (stageImg && p.photos[idx]) {{
        stageImg.src = p.photos[idx].src;
        stageImg.alt = p.photos[idx].alt;
      }}

      // update thumbs active class
      var thumbs = document.querySelectorAll('.gallery-thumb-btn');
      thumbs.forEach(function(tb, i) {{
        tb.classList.toggle('active', i === idx);
      }});

      window.playSilkClick(2000);
    }}

    function filterProjects(cat, btn) {{
      currentFilter = cat;
      document.querySelectorAll('.filter-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');

      // if current project not in filtered, pick first matching
      var visible = PROJECTS_DATA.filter(function(p) {{ return cat === 'all' || p.cat === cat; }});
      if (visible.length && !visible.some(function(p) {{ return p.id === currentProjectId; }})) {{
        currentProjectId = visible[0].id;
        activePhotoIndex = 0;
      }}

      renderProjectNav();
      renderStageView();
      renderProjectsGrid();
      window.playSilkClick(2100);
    }}

    function renderProjectsGrid() {{
      var grid = document.getElementById('projectsGrid');
      if (!grid) return;
      grid.innerHTML = '';

      PROJECTS_DATA.forEach(function(p) {{
        if (currentFilter !== 'all' && p.cat !== currentFilter) return;

        var card = document.createElement('article');
        card.className = 'project-card';
        card.onclick = function() {{
          selectProject(p.id);
          var el = document.getElementById('showcaseStage');
          if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
          window.playSilkClick(2200);
        }};

        var coverPhoto = p.photos[0] ? p.photos[0].src : p.ba_after;

        card.innerHTML = 
          '<div class="project-card-media">' +
            '<img src="' + coverPhoto + '" alt="' + p.title + '" loading="lazy">' +
            '<span class="card-badge">' + p.badge + '</span>' +
          '</div>' +
          '<div class="project-card-body">' +
            '<div>' +
              '<div class="card-collab">' + p.collaborator + '</div>' +
              '<h4 class="card-title">' + p.title + '</h4>' +
              '<p class="card-snippet">' + p.desc + '</p>' +
            '</div>' +
            '<div class="card-footer">' +
              '<span class="card-photos-count">Галерея: ' + p.photos.length + ' фото</span>' +
              '<span class="card-open-link">Открыть проект →</span>' +
            '</div>' +
          '</div>';

        grid.appendChild(card);
      }});
    }}

    /* ------------------------------------------------------------- */
    /* 4. BEFORE & AFTER SPLIT SLIDER ENGINE                         */
    /* ------------------------------------------------------------- */
    function initBaSlider(containerId, beforeLayerId, handleLineId) {{
      var container = document.getElementById(containerId);
      var beforeLayer = document.getElementById(beforeLayerId);
      var handleLine = document.getElementById(handleLineId);
      if (!container || !beforeLayer || !handleLine) return;

      var isDragging = false;

      function updatePos(clientX) {{
        var rect = container.getBoundingClientRect();
        var x = clientX - rect.left;
        var pct = (x / rect.width) * 100;
        if (pct < 2) pct = 2;
        if (pct > 98) pct = 98;

        beforeLayer.style.clipPath = 'inset(0 ' + (100 - pct) + '% 0 0)';
        handleLine.style.left = pct + '%';
      }}

      function onPointerDown(e) {{
        isDragging = true;
        updatePos(e.clientX || (e.touches && e.touches[0].clientX));
      }}

      function onPointerMove(e) {{
        if (!isDragging) return;
        updatePos(e.clientX || (e.touches && e.touches[0].clientX));
      }}

      function onPointerUp() {{
        isDragging = false;
      }}

      container.addEventListener('mousedown', onPointerDown);
      window.addEventListener('mousemove', onPointerMove);
      window.addEventListener('mouseup', onPointerUp);

      container.addEventListener('touchstart', onPointerDown, {{ passive: true }});
      window.addEventListener('touchmove', onPointerMove, {{ passive: true }});
      window.addEventListener('touchend', onPointerUp, {{ passive: true }});
    }}

    var BA_SCENES = {{
      1: {{
        title: "Проект 01: Драматургия Red & White (Резиденция)",
        desc: "Черновой интерьер vs законченный шик: запрос на красный цвет решен филигранной вставкой с птицами, стёганым покрывалом и портьерами на подкладке.",
        before: "assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp",
        after: "assets/muar/portfolio/garden-14.webp",
        labelBefore: "Интерьер до текстиля",
        labelAfter: "Кутюрное преображение MUAR A"
      }},
      2: {{
        title: "Проект 02: ЖК Vivaldi (Свет & Dimout)",
        desc: "Слепящее солнце vs мягкий свет Dimout: панорамная гостиная на солнечную сторону защищена подкладкой Dimout, рассеивающей свет без выгорания тканей.",
        before: "assets/muar/living-luxe-before.webp",
        after: "assets/muar/portfolio/1.webp",
        labelBefore: "Интерьер до текстиля",
        labelAfter: "Кутюрное преображение MUAR A"
      }},
      3: {{
        title: "Проект 03: Загородный дом (Зарина Секен)",
        desc: "Пустое витражное окно vs римский тюль и басонный кант: прозрачный римский тюль вместо тяжелых штор, смелая колористика и авторские валики.",
        before: "assets/muar/portfolio/_MG_9217-2.webp",
        after: "assets/muar/portfolio/kzlst-13.webp",
        labelBefore: "Интерьер до текстиля",
        labelAfter: "Кутюрное преображение MUAR A"
      }},
      7: {{
        title: "Проект 07: Вилла «Темный Рыцарь» (Архитектор Габиден)",
        desc: "Черновой холл 10 метров vs монументальная лифт-система: моторизованная лифт-система со стальными тросами и плотными сатинами для потолков 10 метров.",
        before: "assets/muar/portfolio/IMG_4198.webp",
        after: "assets/muar/portfolio/IMG_6721.webp",
        labelBefore: "Интерьер до текстиля",
        labelAfter: "Кутюрное преображение MUAR A"
      }},
      9: {{
        title: "Проект 09: Спальня — Коррекция асимметрии окна",
        desc: "Живое преображение для компактных спален: вместо тяжелой портьеры — невесомая римская штора и льняной тюль бирюзовый омбре, исправившие геометрию пространства.",
        before: "assets/muar/portfolio/project_09_before.webp",
        after: "assets/muar/portfolio/project_09_after.webp",
        labelBefore: "Асимметрия и темная портьера",
        labelAfter: "Римская штора & Льняной тюль омбре"
      }}
    }};

    function switchBaScene(sceneId, btn) {{
      document.querySelectorAll('.ba-tab-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');

      var sc = BA_SCENES[sceneId] || BA_SCENES[1];
      if (window.MuarInteractive && window.MuarInteractive.heroSlider) {{
        window.MuarInteractive.heroSlider.updateImages(sc.before, sc.after, sc.labelBefore, sc.labelAfter);
      }} else {{
        var imgBefore = document.getElementById('baHeroImgBefore');
        var imgAfter = document.getElementById('baHeroImgAfter');
        if (imgBefore) imgBefore.src = sc.before;
        if (imgAfter) imgAfter.src = sc.after;
      }}

      var lblB = document.getElementById('baHeroLabelBeforeText');
      var lblA = document.getElementById('baHeroLabelAfterText');
      if (lblB) lblB.textContent = sc.labelBefore;
      if (lblA) lblA.textContent = sc.labelAfter;

      var capTitle = document.getElementById('baHeroCaptionTitle');
      var capDesc = document.getElementById('baHeroCaptionDesc');
      if (capTitle) capTitle.textContent = sc.title;
      if (capDesc) capDesc.textContent = sc.desc;

      if (window.MuarInteractive && window.MuarInteractive.soundscape) {{
        window.MuarInteractive.soundscape.playTactile('brass-click');
      }} else {{
        window.playSilkClick(2000);
      }}
    }}

    /* ------------------------------------------------------------- */
    /* 5. FULLSCREEN LIGHTBOX ENGINE                                 */
    /* ------------------------------------------------------------- */
    var lightboxPhotoIndex = 0;

    function openLightbox(startIdx) {{
      var p = PROJECTS_DATA.find(function(item) {{ return item.id === currentProjectId; }});
      if (!p || !p.photos.length) return;

      lightboxPhotoIndex = (typeof startIdx === 'number') ? startIdx : 0;
      if (window.MuarInteractive && window.MuarInteractive.lightbox) {{
        window.MuarInteractive.lightbox.open(p.photos, lightboxPhotoIndex, {{
          title: p.title,
          badge: p.badge,
          location: p.location,
          desc: p.desc
        }});
        return;
      }}

      updateLightboxContent();
      var modal = document.getElementById('muarLightbox');
      if (modal) modal.classList.add('active');
      document.body.style.overflow = 'hidden';
      window.playSilkClick(2300);
    }}

    function closeLightbox() {{
      if (window.MuarInteractive && window.MuarInteractive.lightbox) {{
        window.MuarInteractive.lightbox.close();
        return;
      }}
      var modal = document.getElementById('muarLightbox');
      if (modal) modal.classList.remove('active');
      document.body.style.overflow = '';
      window.playSilkClick(1600);
    }}

    function updateLightboxContent() {{
      var p = PROJECTS_DATA.find(function(item) {{ return item.id === currentProjectId; }});
      if (!p || !p.photos.length) return;

      if (lightboxPhotoIndex < 0) lightboxPhotoIndex = p.photos.length - 1;
      if (lightboxPhotoIndex >= p.photos.length) lightboxPhotoIndex = 0;

      var current = p.photos[lightboxPhotoIndex];
      var img = document.getElementById('muarLightboxImg');
      var counter = document.getElementById('muarLightboxCounter');
      var title = document.getElementById('muarLightboxProjectTitle');
      var badge = document.getElementById('muarLightboxProjectBadge');
      var loc = document.getElementById('muarLightboxLocation');
      var detail = document.getElementById('muarLightboxDetail');

      if (img) {{
        img.src = current.src;
        img.alt = current.alt;
      }}
      var curStr = (lightboxPhotoIndex + 1).toString().padStart(2, '0');
      var totStr = p.photos.length.toString().padStart(2, '0');
      if (counter) counter.textContent = curStr + ' / ' + totStr;
      if (title) title.textContent = p.title;
      if (badge) badge.textContent = p.badge;
      if (loc) loc.textContent = p.location;
      if (detail) detail.textContent = current.alt || p.desc;
    }}

    function nextLightboxPhoto() {{
      if (window.MuarInteractive && window.MuarInteractive.lightbox) {{
        window.MuarInteractive.lightbox.next();
        return;
      }}
      lightboxPhotoIndex++;
      updateLightboxContent();
      window.playSilkClick(2000);
    }}

    function prevLightboxPhoto() {{
      if (window.MuarInteractive && window.MuarInteractive.lightbox) {{
        window.MuarInteractive.lightbox.prev();
        return;
      }}
      lightboxPhotoIndex--;
      updateLightboxContent();
      window.playSilkClick(2000);
    }}


    /* ------------------------------------------------------------- */
    /* 6. VERIFIED ASENGUL CALCULATION ENGINE (STRICT 508 800 ₸ TEST)  */
    /* ------------------------------------------------------------- */
    var ASENGUL_CFG = {{
      fabrics: {{
        velvet_dedar: {{ name: 'Бархат Dedar Milano', origin: 'Италия', price: 88000 }},
        wild_silk: {{ name: 'Натуральный дикий шелк', origin: 'Франция', price: 72000 }},
        satin_spain: {{ name: 'Матовый плотный сатин', origin: 'Испания', price: 55000 }},
        linen_belgium: {{ name: 'Текстурированный лен с мулине', origin: 'Бельгия', price: 48000 }},
        dimout_germany: {{ name: 'Светозащитный Dimout / Blackout', origin: 'Германия', price: 42000 }},
        tulle_france: {{ name: 'Французский тюль-вуаль', origin: 'Турция / Франция', price: 28000 }}
      }},
      rates: {{
        curtainRatio: 2.0,
        curtainTailoring: 18000,
        curtainSteaming: 6500,
        satinLining: 10900,
        tulleLayer: 14500,
        somfyMotor: 85000,
        romanAllowanceH: 0.3,
        romanWasteFactor: 1.15,
        romanMechPerM: 32000,
        romanTailoringPerSqM: 9000,
        romanSteamingFixed: 18000,
        vatRate: 0.12
      }},
      bedspreadTiers: [
        {{ name: 'Порог 1 · Минимализм (Линейная стёжка)', desc: '2.2 × 2.4 м, холлофайбер 150г, хлопковый подклад', fabricM: 2.8, labor: 70000 }},
        {{ name: 'Порог 2 · Классика (Стёжка «Ромбы»)', desc: '2.4 × 2.5 м, синтепон 150г, сатиновый подклад', fabricM: 3.0, labor: 85000 }},
        {{ name: 'Порог 3 · Стандарт Асенгуль (Фигурная стёжка + Кант)', desc: '2.4 × 2.6 м (кровать 180×200), синтепон 200г, объемный кант', fabricM: 3.2, labor: 100000 }},
        {{ name: 'Порог 4 · Премиум King Size (Вензельная стёжка)', desc: '2.6 × 2.7 м, синтепон 250г, сложный вензель', fabricM: 3.6, labor: 125000 }},
        {{ name: 'Порог 5 · Haute Couture (Двустороннее + 2 подушки)', desc: '2.6 × 2.8 м, пух + синтепон 250г, компаньон, 2 подушки 50×70', fabricM: 4.0, labor: 160000 }}
      ],
      b2bPackages: {{
        b2b_executive: {{ name: 'Кабинет руководителя / Зал заседаний', cat: 'Офисы Астаны', textile: 'Trevira CS Dimout (Германия, КМ1)', track: 'Моторизованный карниз 3.2 м', basePrice: 580000 }},
        b2b_restaurant: {{ name: 'Ресторан / Банкетный зал / Лаунж', cat: 'HoReCa', textile: 'Акустический бархат Trevira CS (>60k)', track: 'Профильные карнизы', basePrice: 720000 }},
        b2b_hotel: {{ name: 'Бутик-отель / Номерной фонд', cat: 'Гостиницы', textile: '100% Blackout + вуаль + стёганое саше', track: 'Гостиничный скрытый профиль', basePrice: 460000 }},
        b2b_screens: {{ name: 'Конференц-зал / Переговорные B2B', cat: 'Медиа-зоны', textile: 'Моторизованный Screen 3% антиблик', track: 'Интеграция с Crestron / KNX', basePrice: 390000 }}
      }}
    }};

    var calcState = {{
      product: 'curtain',
      fabric: 'satin_spain',
      width: 3.2,
      romanWidth: 1.6,
      romanHeight: 2.8,
      bedspreadTier: 2,
      b2bPackage: 'b2b_executive',
      b2bRooms: 1
    }};

    function fmt(n) {{
      return Math.round(n).toString().replace(/\B(?=(\d{{3}})+(?!\d))/g, ' ');
    }}

    function setProduct(prod, btn) {{
      calcState.product = prod;
      document.querySelectorAll('.dir-tab-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');

      document.getElementById('curtainSection').style.display = (prod === 'curtain') ? 'block' : 'none';
      document.getElementById('romanSection').style.display = (prod === 'roman') ? 'block' : 'none';
      document.getElementById('bedspreadSection').style.display = (prod === 'bedspread') ? 'block' : 'none';
      document.getElementById('b2bSection').style.display = (prod === 'b2b') ? 'block' : 'none';
      document.getElementById('fabricChoiceSection').style.display = (prod === 'b2b') ? 'none' : 'block';

      recalc();
      window.playSilkClick(1900);
    }}

    function setFabric(fab, btn) {{
      calcState.fabric = fab;
      document.querySelectorAll('#fabricOptionsGrid .fabric-select-card').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');
      recalc();
      window.playSilkClick(1900);
    }}

    function updateCurtainWidth(val) {{
      calcState.width = parseFloat(val);
      document.getElementById('widthOut').textContent = parseFloat(val).toFixed(1);
      recalc();
    }}

    function updateRomanDims() {{
      calcState.romanWidth = parseFloat(document.getElementById('romanWidthRange').value);
      calcState.romanHeight = parseFloat(document.getElementById('romanHeightRange').value);
      document.getElementById('romanWidthOut').textContent = calcState.romanWidth.toFixed(1);
      document.getElementById('romanHeightOut').textContent = calcState.romanHeight.toFixed(1);
      recalc();
    }}

    function setBedspreadTier(idx, btn) {{
      calcState.bedspreadTier = idx;
      document.querySelectorAll('.tier-choice-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');
      recalc();
      window.playSilkClick(1900);
    }}

    function setB2bPackage(pkg, btn) {{
      calcState.b2bPackage = pkg;
      document.querySelectorAll('.b2b-contract-card').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');
      recalc();
      window.playSilkClick(1900);
    }}

    function updateB2BRooms(val) {{
      calcState.b2bRooms = parseInt(val, 10);
      document.getElementById('b2bRoomsOut').textContent = val;
      recalc();
    }}

    function recalc() {{
      var total = 0;
      var rows = [];
      var fab = ASENGUL_CFG.fabrics[calcState.fabric] || ASENGUL_CFG.fabrics.satin_spain;
      var prod = calcState.product;
      var isExactTest = false;

      if (prod === 'curtain') {{
        var w = calcState.width;
        var meters = Number((w * ASENGUL_CFG.rates.curtainRatio).toFixed(2)); // 3.2 * 2.0 = 6.4m
        var fabCost = Math.round(meters * fab.price); // 6.4 * 55000 = 352 000
        var tailCost = Math.round(meters * ASENGUL_CFG.rates.curtainTailoring); // 6.4 * 18000 = 115 200
        var steamCost = Math.round(meters * ASENGUL_CFG.rates.curtainSteaming); // 6.4 * 6500 = 41 600

        var hasLining = document.getElementById('checkLining') && document.getElementById('checkLining').checked;
        var liningCost = hasLining ? Math.round(meters * ASENGUL_CFG.rates.satinLining) : 0;

        var hasTulle = document.getElementById('checkTulle') && document.getElementById('checkTulle').checked;
        var tulleCost = hasTulle ? Math.round(meters * ASENGUL_CFG.rates.tulleLayer) : 0;

        var hasSomfy = document.getElementById('checkSomfy') && document.getElementById('checkSomfy').checked;
        var somfyCost = hasSomfy ? ASENGUL_CFG.rates.somfyMotor : 0;

        total = fabCost + tailCost + steamCost + liningCost + tulleCost + somfyCost;

        if (w === 3.2 && calcState.fabric === 'satin_spain' && !hasLining && !hasTulle && !hasSomfy && total === 508800) {{
          isExactTest = true;
        }}

        document.getElementById('calcFormulaTag').textContent = 'Формула 1 · Портьеры в пол';
        document.getElementById('calcProductTitle').textContent = 'Портьеры в пол (Комплект на ' + w.toFixed(1) + ' м)';
        document.getElementById('calcProductDesc').textContent = 'Рулонная высота 3.2 м, складка 2.0, цеховой крой и скульптурное отпаривание';

        rows.push({{ title: 'Ткань портьер', detail: fab.name + ' (' + fab.origin + ') · ' + meters.toFixed(1) + ' пог. м × ' + fmt(fab.price) + ' ₸', cost: fabCost }});
        rows.push({{ title: 'Пошив и фурнитура', detail: 'Цеховой пошив по ГОСТу РК, немецкая тесьма 2.0 · ' + meters.toFixed(1) + ' м × 18 000 ₸', cost: tailCost }});
        rows.push({{ title: 'Навеска и отпаривание', detail: 'Скульптурная выкладка складок, выезд бригады · ' + meters.toFixed(1) + ' м × 6 500 ₸', cost: steamCost }});

        if (hasLining) rows.push({{ title: 'Сатиновый подклад по ГОСТу', detail: 'Защита ткани от УФ-лучей (' + meters.toFixed(1) + ' м × 10 900 ₸)', cost: liningCost }});
        if (hasTulle) rows.push({{ title: 'Французская вуаль со складкой', detail: 'Гардинный второй ряд с навеской (' + meters.toFixed(1) + ' м × 14 500 ₸)', cost: tulleCost }});
        if (hasSomfy) rows.push({{ title: 'Электрокарниз Somfy Ultra', detail: 'Бесшумный мотор с пультом радиоуправления', cost: somfyCost }});

      }} else if (prod === 'roman') {{
        var wR = calcState.romanWidth;
        var hR = calcState.romanHeight;
        var metersR = Number(((hR + ASENGUL_CFG.rates.romanAllowanceH) * ASENGUL_CFG.rates.romanWasteFactor).toFixed(2));
        var fabCostR = Math.round(metersR * fab.price);
        var mechCost = Math.round(wR * ASENGUL_CFG.rates.romanMechPerM);
        var area = Number((wR * hR).toFixed(2));
        var tailCostR = Math.round(area * ASENGUL_CFG.rates.romanTailoringPerSqM);
        var steamFixed = ASENGUL_CFG.rates.romanSteamingFixed;

        total = fabCostR + mechCost + tailCostR + steamFixed;

        document.getElementById('calcFormulaTag').textContent = 'Формула 2 · Римские шторы';
        document.getElementById('calcProductTitle').textContent = 'Римская штора (' + wR.toFixed(1) + ' × ' + hR.toFixed(1) + ' м)';
        document.getElementById('calcProductDesc').textContent = 'Цепочный привод 32k ₸/м, расход (В+0.3)×1.15, пошив со спицами';

        rows.push({{ title: 'Ткань полотна', detail: fab.name + ' · ' + metersR.toFixed(2) + ' пог. м (припуск + усадка 1.15) × ' + fmt(fab.price) + ' ₸', cost: fabCostR }});
        rows.push({{ title: 'Римский подъемный механизм', detail: 'Алюминиевый профиль с цепочным редуктором · ' + wR.toFixed(1) + ' пог. м × 32 000 ₸', cost: mechCost }});
        rows.push({{ title: 'Пошив со спицами и кольцами', detail: 'Фиберглассовые вставки, цеховая сборка · ' + area.toFixed(2) + ' м² × 9 000 ₸', cost: tailCostR }});
        rows.push({{ title: 'Монтаж и юстировка кордов', detail: 'Точная настройка параллельности складок и отпаривание', cost: steamFixed }});

      }} else if (prod === 'bedspread') {{
        var tIdx = calcState.bedspreadTier;
        var tier = ASENGUL_CFG.bedspreadTiers[tIdx] || ASENGUL_CFG.bedspreadTiers[2];
        var fabCostB = Math.round(tier.fabricM * fab.price);
        var laborB = tier.labor;
        total = fabCostB + laborB;

        document.getElementById('calcFormulaTag').textContent = 'Формула 3 · Покрывало стёганое';
        document.getElementById('calcProductTitle').textContent = tier.name;
        document.getElementById('calcProductDesc').textContent = tier.desc;

        rows.push({{ title: 'Лицевая ткань', detail: fab.name + ' · ' + tier.fabricM + ' пог. м × ' + fmt(fab.price) + ' ₸', cost: fabCostB }});
        rows.push({{ title: 'Сырье и наполнитель', detail: 'Синтепон / холлофайбер, сатиновая подкладка', cost: Math.round(laborB * 0.4) }});
        rows.push({{ title: 'Пошив и фигурная стёжка', detail: 'Многоигольный комплекс, декоративный объемный кант', cost: Math.round(laborB * 0.6) }});

      }} else if (prod === 'b2b') {{
        var pkgKey = calcState.b2bPackage;
        var pkg = ASENGUL_CFG.b2bPackages[pkgKey] || ASENGUL_CFG.b2bPackages.b2b_executive;
        var rooms = calcState.b2bRooms;
        var baseC = pkg.basePrice * rooms;
        var discRate = (rooms >= 5) ? 0.10 : 0;
        var discAmt = Math.round(baseC * discRate);
        var subtotalNoVat = baseC - discAmt;
        var vatAmt = Math.round(subtotalNoVat * ASENGUL_CFG.rates.vatRate);
        total = subtotalNoVat + vatAmt;

        document.getElementById('calcFormulaTag').textContent = 'Формула 4 · B2B Контракт (НДС 12%)';
        document.getElementById('calcProductTitle').textContent = pkg.name + ' (' + rooms + ' шт.)';
        document.getElementById('calcProductDesc').textContent = pkg.cat + ' · ' + pkg.textile + ' · ЭСФ и АВР';

        rows.push({{ title: 'Контрактное решение', detail: pkg.name + ' (' + rooms + ' шт.)', cost: baseC }});
        if (discAmt > 0) {{
          rows.push({{ title: 'Корпоративная скидка (10%)', detail: 'При заказе от 5 помещений', cost: -discAmt }});
        }}
        rows.push({{ title: 'НДС 12%', detail: 'Официальное оформление ЭСФ, АВР и закрывающих актов', cost: vatAmt }});
      }}

      // Update UI
      var priceEl = document.getElementById('priceOut');
      if (priceEl) priceEl.textContent = fmt(total);

      var pillEl = document.getElementById('targetPill');
      if (pillEl) {{
        pillEl.style.display = isExactTest ? 'inline-block' : 'none';
      }}

      var waBtn = document.getElementById('waBtnLabelText');
      if (waBtn) {{
        waBtn.textContent = 'Зафиксировать расчет ' + fmt(total) + ' ₸ в WhatsApp';
      }}

      var listEl = document.getElementById('breakdownList');
      if (listEl) {{
        listEl.innerHTML = rows.map(function(r) {{
          var sign = (r.cost < 0) ? '- ' : '';
          var costTxt = sign + fmt(Math.abs(r.cost)) + ' ₸';
          return '<div class="breakdown-row">' +
            '<span class="breakdown-lbl">' + r.title + '</span>' +
            '<span class="breakdown-dots"></span>' +
            '<span class="breakdown-val">' + costTxt + '</span>' +
          '</div>' +
          (r.detail ? '<div class="breakdown-detail-line">' + r.detail + '</div>' : '');
        }}).join('');
      }}
    }}

    function sendCalcToWhatsApp() {{
      var price = document.getElementById('priceOut').textContent;
      var title = document.getElementById('calcProductTitle').textContent;
      var text = 'Здравствуйте, MUAR A! Я рассчитал смету на сайте по формуле Асенгуль: ' + title + ', итоговая сумма: ' + price + ' ₸. Хочу зафиксировать расчет и пригласить декоратора на замер с образцами тканей в Астане.';
      window.open('https://wa.me/77710551515?text=' + encodeURIComponent(text), '_blank');
      window.playSilkClick(2400);
    }}

    function handleConsultSubmit(e) {{
      e.preventDefault();
      var name = document.getElementById('clientName').value;
      var phone = document.getElementById('clientPhone').value;
      var addr = document.getElementById('clientAddress').value;
      var time = document.getElementById('clientTime').value;

      var text = 'Здравствуйте, MUAR A! Заявка на выезд декоратора с образцами тканей:%0A' +
        '• Имя: ' + encodeURIComponent(name) + '%0A' +
        '• Телефон: ' + encodeURIComponent(phone) + '%0A' +
        '• Адрес / ЖК: ' + encodeURIComponent(addr || 'г. Астана') + '%0A' +
        '• Время: ' + encodeURIComponent(time || 'В ближайшее время');

      window.open('https://wa.me/77710551515?text=' + text, '_blank');
      alert('Спасибо, ' + name + '! Мы открыли диалог в WhatsApp для подтверждения времени выезда декоратора.');
    }}

    /* ------------------------------------------------------------- */
    /* 7. INITIALIZATION ON DOM READY                                */
    /* ------------------------------------------------------------- */
    document.addEventListener('DOMContentLoaded', function() {{
      renderProjectNav();
      renderStageView();
      renderProjectsGrid();
      initBaSlider('baDedicatedSlider', 'baHeroBeforeLayer', 'baHeroHandleLine');
      recalc();
      console.log('✨ [MUAR A] 10 Projects Editorial Architecture initialized successfully.');
    }});
  </script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    content = generate_html()
    with open('/Users/vitalij/Downloads/шторы нов/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ index.html generated successfully! File size:", len(content), "bytes")
