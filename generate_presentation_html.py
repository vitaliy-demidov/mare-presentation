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
    /* 7. EXACT ASENGUL CALCULATION ENGINE (VERIFIED MATH)          */
    /* ============================================================ */
    .section-calc {{
      padding: 90px 0;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
    }}
    .calc-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      overflow: hidden;
      margin-top: 44px;
      box-shadow: 0 24px 60px -15px rgba(0, 0, 0, 0.6);
    }}
    .calc-audience-bar {{
      display: flex;
      background: rgba(0, 0, 0, 0.3);
      border-bottom: 1px solid var(--border-subtle);
    }}
    .aud-btn {{
      flex: 1;
      padding: 18px 24px;
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
      transition: var(--transition);
      text-align: center;
    }}
    .aud-btn:hover {{
      color: #FFFFFF;
      background: rgba(255, 255, 255, 0.02);
    }}
    .aud-btn.active {{
      color: var(--coral-light);
      border-bottom-color: var(--coral);
      background: rgba(226, 90, 61, 0.06);
    }}

    .calc-body {{
      display: grid;
      grid-template-columns: 1.15fr 1fr;
    }}
    @media (max-width: 900px) {{
      .calc-body {{ grid-template-columns: 1fr; }}
    }}
    .calc-controls {{
      padding: 36px;
      border-right: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 28px;
    }}
    @media (max-width: 768px) {{
      .calc-controls {{ padding: 24px 18px; border-right: none; border-bottom: 1px solid var(--border-subtle); }}
    }}
    .calc-summary {{
      padding: 36px;
      background: rgba(0, 0, 0, 0.2);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    @media (max-width: 768px) {{
      .calc-summary {{ padding: 24px 18px; }}
    }}

    .field-group {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .field-label {{
      font-size: 0.84rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
    }}
    .pill-options-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }}
    @media (max-width: 500px) {{
      .pill-options-grid {{ grid-template-columns: 1fr; }}
    }}
    .pill-opt-btn {{
      padding: 10px 14px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text-secondary);
      cursor: pointer;
      transition: var(--transition);
      text-align: center;
    }}
    .pill-opt-btn:hover {{
      border-color: var(--border-hover);
      color: #FFFFFF;
    }}
    .pill-opt-btn.active {{
      background: var(--coral-bg);
      border-color: var(--coral);
      color: #FFFFFF;
      font-weight: 600;
    }}

    .range-box {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .range-val-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .range-val-num {{
      font-family: var(--font-serif);
      font-size: 1.4rem;
      font-weight: 600;
      color: var(--coral-light);
    }}
    input[type=range] {{
      width: 100%;
      height: 6px;
      border-radius: 3px;
      background: rgba(255, 255, 255, 0.12);
      outline: none;
      -webkit-appearance: none;
      accent-color: var(--coral);
    }}

    .calc-check-row {{
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      font-size: 0.92rem;
      color: var(--text-secondary);
      user-select: none;
    }}
    .calc-check-row input[type=checkbox] {{
      width: 18px;
      height: 18px;
      accent-color: var(--coral);
      cursor: pointer;
    }}

    /* Price Output Box */
    .price-display-box {{
      padding: 24px;
      border-radius: var(--radius-lg);
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      margin-bottom: 24px;
    }}
    .price-kicker {{
      font-size: 0.78rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin-bottom: 8px;
    }}
    .price-num-wrap {{
      display: flex;
      align-items: baseline;
      gap: 10px;
    }}
    .price-sum {{
      font-family: var(--font-serif);
      font-size: clamp(2.2rem, 3.6vw, 3rem);
      font-weight: 700;
      color: #FFFFFF;
      line-height: 1;
    }}
    .price-curr {{
      font-family: var(--font-serif);
      font-size: 1.6rem;
      color: var(--coral);
    }}

    /* Breakdown Lines */
    .breakdown-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 28px;
    }}
    .breakdown-row {{
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 8px;
      font-size: 0.85rem;
    }}
    .breakdown-lbl {{
      color: var(--text-muted);
    }}
    .breakdown-dots {{
      flex: 1;
      border-bottom: 1px dotted rgba(255, 255, 255, 0.15);
      margin: 0 4px;
    }}
    .breakdown-val {{
      color: var(--text-primary);
      font-weight: 500;
      white-space: nowrap;
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
        <button type="button" class="audio-toggle-btn" id="ambientToggleBtn" onclick="toggleAmbientSound()" title="Включить атмосферную музыку салона">
          <span class="sound-wave">
            <span class="sound-bar"></span>
            <span class="sound-bar"></span>
            <span class="sound-bar"></span>
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

      <!-- Scene Switcher Tabs -->
      <div class="ba-tabs-nav">
        <button type="button" class="ba-tab-btn active" onclick="switchBaScene(1, this)">01. Red &amp; White (Резиденция)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(2, this)">02. ЖК Vivaldi (Свет &amp; Dimout)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(3, this)">03. Загородный дом (Зарина Секен)</button>
        <button type="button" class="ba-tab-btn" onclick="switchBaScene(7, this)">07. Вилла Нолана (Потолки 10 м)</button>
      </div>

      <div class="ba-stage-card">
        <div class="ba-slider-hero" id="baHeroSlider">
          <div class="ba-slider-container" id="baDedicatedSlider">
            <div class="ba-after-layer">
              <img id="baHeroImgAfter" src="assets/muar/portfolio/garden-14.webp" alt="После текстильного оформления">
            </div>
            <div class="ba-before-layer" id="baHeroBeforeLayer">
              <img id="baHeroImgBefore" src="assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp" alt="До текстильного оформления">
            </div>
            <div class="ba-handle-line" id="baHeroHandleLine">
              <div class="ba-handle-grip">⇄</div>
            </div>
            <div class="ba-tag ba-tag-before" id="baHeroLabelBefore">Без штор</div>
            <div class="ba-tag ba-tag-after" id="baHeroLabelAfter">Драматургия Red &amp; White</div>
          </div>
        </div>
        <div class="ba-card-caption">
          <div class="ba-caption-text">
            <h4 id="baHeroCaptionTitle">Проект 01: Драматургия Red &amp; White</h4>
            <p id="baHeroCaptionDesc">Шторы на подкладке, вставка с птицами и стеганое покрывало создали единый кутюрный ансамбль.</p>
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
  <!-- 6. EXACT ASENGUL CALCULATION ENGINE                          -->
  <!-- ============================================================ -->
  <section class="section-calc" id="calculator">
    <div class="wrap">
      <div class="section-head center">
        <div class="section-kicker">ОНЛАЙН-РАСЧЕТ СМЕТЫ</div>
        <h2 class="section-title">Калькулятор текстильного оформления</h2>
        <p class="section-subtitle">
          Точный алгоритм ценообразования Muar A. Прозрачная спецификация ткани, пошива по ГОСТу, подкладки и карнизов без скрытых наценок.
        </p>
      </div>

      <div class="calc-card">
        
        <!-- Audience Switcher -->
        <div class="calc-audience-bar">
          <button type="button" class="aud-btn active" id="audB2CBtn" onclick="switchAudience('b2c')">
            Частный интерьер (B2C Квартиры &amp; Виллы)
          </button>
          <button type="button" class="aud-btn" id="audB2BBtn" onclick="switchAudience('b2b')">
            Корпоративный контракт (B2B Офисы, Отели, Рестораны)
          </button>
        </div>

        <div class="calc-body">
          
          <!-- Left: Controls -->
          <div class="calc-controls">
            
            <!-- Product Type -->
            <div class="field-group" id="b2cProductGroup">
              <label class="field-label">Тип текстильного изделия</label>
              <div class="pill-options-grid">
                <button type="button" class="pill-opt-btn active" data-prod="curtain" onclick="setProduct('curtain', this)">Портьеры в пол</button>
                <button type="button" class="pill-opt-btn" data-prod="roman" onclick="setProduct('roman', this)">Римская штора</button>
                <button type="button" class="pill-opt-btn" data-prod="bedspread" onclick="setProduct('bedspread', this)">Покрывало &amp; Подушки</button>
              </div>
            </div>

            <!-- B2B Package Type -->
            <div class="field-group" id="b2bPackageGroup" style="display: none;">
              <label class="field-label">Контрактное решение</label>
              <div class="pill-options-grid">
                <button type="button" class="pill-opt-btn active" data-b2bpkg="pkg_curtain" onclick="setB2bPackage('pkg_curtain', this)">Кабинет 1: Портьеры</button>
                <button type="button" class="pill-opt-btn" data-b2bpkg="pkg_blinds" onclick="setB2bPackage('pkg_blinds', this)">Кабинет 2: Жалюзи</button>
                <button type="button" class="pill-opt-btn" data-b2bpkg="pkg_roman" onclick="setB2bPackage('pkg_roman', this)">Кабинет 3: Римские</button>
              </div>
            </div>

            <!-- Fabric Category -->
            <div class="field-group">
              <label class="field-label">Категория ткани</label>
              <div class="pill-options-grid" id="fabricOptionsGrid">
                <button type="button" class="pill-opt-btn active" data-fab="linen" onclick="setFabric('linen', this)">Лён фактурный (24k ₸)</button>
                <button type="button" class="pill-opt-btn" data-fab="satin" onclick="setFabric('satin', this)">Сатин Soft (18k ₸)</button>
                <button type="button" class="pill-opt-btn" data-fab="dimout" onclick="setFabric('dimout', this)">Dimout Текстура (22k ₸)</button>
                <button type="button" class="pill-opt-btn" data-fab="velvet" onclick="setFabric('velvet', this)">Бархат Couture (28k ₸)</button>
                <button type="button" class="pill-opt-btn" data-fab="chenille" onclick="setFabric('chenille', this)">Шенилл Wind (32k ₸)</button>
                <button type="button" class="pill-opt-btn" data-fab="jacquard" onclick="setFabric('jacquard', this)">Жаккард Люкс (38k ₸)</button>
              </div>
            </div>

            <!-- Dimensions (Width & Height) -->
            <div class="range-box" id="rangeWidthBox">
              <div class="range-val-row">
                <label class="field-label">Ширина карниза / окна</label>
                <span class="range-val-num"><span id="widthOut">3.2</span> м</span>
              </div>
              <input type="range" id="widthRange" min="1.0" max="8.0" step="0.1" value="3.2" oninput="updateRange('width', this.value)">
            </div>

            <!-- Options Checkboxes -->
            <div class="field-group" id="b2cAddonsGroup">
              <label class="field-label">Дополнительные опции пошива</label>
              <div style="display: flex; flex-direction: column; gap: 12px;">
                <label class="calc-check-row">
                  <input type="checkbox" id="checkLining" checked onchange="recalc()">
                  <span>Сатиновый подклад по ГОСТу РК (защита от выгорания, 10 900 ₸/м)</span>
                </label>
                <label class="calc-check-row">
                  <input type="checkbox" id="checkTulle" checked onchange="recalc()">
                  <span>Французская вуаль 1:2 со складкой и навеской (9 500 ₸/м)</span>
                </label>
                <label class="calc-check-row">
                  <input type="checkbox" id="checkSomfy" onchange="recalc()">
                  <span>Электрокарниз Somfy Ultra с бесшумным мотором и пультом (85 000 ₸)</span>
                </label>
              </div>
            </div>

          </div>

          <!-- Right: Summary Output -->
          <div class="calc-summary">
            <div>
              <div class="price-display-box">
                <div class="price-kicker" id="calcPriceKicker">ИТОГОВАЯ СМЕТА «ПОД КЛЮЧ»</div>
                <div class="price-num-wrap">
                  <div class="price-sum" id="priceOut">508 800</div>
                  <div class="price-curr">₸</div>
                </div>
              </div>

              <!-- Itemized Breakdown -->
              <div class="breakdown-list" id="breakdownList">
                <!-- Populated via JS -->
              </div>
            </div>

            <div>
              <button type="button" class="btn btn-coral" style="width: 100%;" onclick="sendCalcToWhatsApp()">
                Зафиксировать смету в WhatsApp
              </button>
              <div style="font-size: 0.76rem; color: var(--text-muted); text-align: center; margin-top: 10px;">
                * Расчет носит предварительный характер. Точную смету утвердит декоратор при замере с образцами.
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
  <!-- 9. FULLSCREEN LIGHTBOX MODAL                                 -->
  <!-- ============================================================ -->
  <div class="lightbox-modal" id="lightboxModal" role="dialog" aria-modal="true">
    <div class="lightbox-top-bar">
      <div class="lightbox-counter" id="lightboxCounter">1 / 9</div>
      <div style="font-weight: 600;" id="lightboxProjectTitle">Проект 01</div>
      <button type="button" class="lightbox-close-btn" onclick="closeLightbox()" title="Закрыть (Esc)">✕</button>
    </div>
    
    <div class="lightbox-main-view">
      <button type="button" class="lightbox-arrow lightbox-prev" onclick="prevLightboxPhoto()" title="Предыдущее фото (←)">❮</button>
      <img id="lightboxImg" class="lightbox-img" src="" alt="Фотография интерьера в высоком разрешении">
      <button type="button" class="lightbox-arrow lightbox-next" onclick="nextLightboxPhoto()" title="Следующее фото (→)">❯</button>
    </div>

    <div class="lightbox-caption-text" id="lightboxCaption">
      Деталь текстильного оформления
    </div>
  </div>

  <!-- Audio Asset -->
  <audio id="ambientAudio" loop preload="none">
    <source src="assets/muar/ambient-lounge.mp3" type="audio/mpeg">
  </audio>

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
            '<div class="ba-slider-container" id="stageBaSlider">' +
              '<div class="ba-after-layer">' +
                '<img src="' + p.ba_after + '" alt="' + p.title + '">' +
              '</div>' +
              '<div class="ba-before-layer" id="stageBaBeforeLayer">' +
                '<img src="' + p.ba_before + '" alt="Интерьер до оформления">' +
              '</div>' +
              '<div class="ba-handle-line" id="stageBaHandleLine">' +
                '<div class="ba-handle-grip">⇄</div>' +
              '</div>' +
              '<div class="ba-tag ba-tag-before">' + p.ba_label_before + '</div>' +
              '<div class="ba-tag ba-tag-after">' + p.ba_label_after + '</div>' +
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
        initBaSlider('stageBaSlider', 'stageBaBeforeLayer', 'stageBaHandleLine');
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
        title: "Проект 01: Драматургия Red & White",
        desc: "Категоричный запрос на красный цвет решен филигранной вставкой с птицами, стёганым покрывалом и портьерами на подкладке.",
        before: "assets/muar/portfolio/photo_9@29-09-2026_17-02-55.webp",
        after: "assets/muar/portfolio/garden-14.webp",
        labelBefore: "Без штор",
        labelAfter: "Драматургия Red & White"
      }},
      2: {{
        title: "Проект 02: ЖК Vivaldi (Свет & Dimout)",
        desc: "Панорамная гостиная на солнечную сторону защищена подкладкой Dimout. Мягкое рассеивание света без выгорания тканей.",
        before: "assets/muar/living-luxe-before.webp",
        after: "assets/muar/portfolio/1.webp",
        labelBefore: "Слепящее солнце",
        labelAfter: "Свет Dimout"
      }},
      3: {{
        title: "Проект 03: Загородный дом (Зарина Секен)",
        desc: "Римский прозрачный тюль вместо тяжелых штор, смелая колористика, декоративные басонные канты и авторские валики.",
        before: "assets/muar/portfolio/_MG_9217-2.webp",
        after: "assets/muar/portfolio/kzlst-13.webp",
        labelBefore: "Пустое окно",
        labelAfter: "Римский тюль & Канты"
      }},
      7: {{
        title: "Проект 07: Вилла «Темный Рыцарь» (Габиден)",
        desc: "Холл со вторым светом высотой 10 метров. Разработка моторизованной лифт-системы со стальными тросами и плотными сатинами.",
        before: "assets/muar/portfolio/IMG_4198.webp",
        after: "assets/muar/portfolio/IMG_6721.webp",
        labelBefore: "Черновой холл 10 м",
        labelAfter: "Элегантность Нолана"
      }}
    }};

    function switchBaScene(sceneId, btn) {{
      document.querySelectorAll('.ba-tab-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');

      var sc = BA_SCENES[sceneId] || BA_SCENES[1];
      var imgBefore = document.getElementById('baHeroImgBefore');
      var imgAfter = document.getElementById('baHeroImgAfter');
      var lblBefore = document.getElementById('baHeroLabelBefore');
      var lblAfter = document.getElementById('baHeroLabelAfter');
      var capTitle = document.getElementById('baHeroCaptionTitle');
      var capDesc = document.getElementById('baHeroCaptionDesc');

      if (imgBefore) imgBefore.src = sc.before;
      if (imgAfter) imgAfter.src = sc.after;
      if (lblBefore) lblBefore.textContent = sc.labelBefore;
      if (lblAfter) lblAfter.textContent = sc.labelAfter;
      if (capTitle) capTitle.textContent = sc.title;
      if (capDesc) capDesc.textContent = sc.desc;

      window.playSilkClick(2000);
    }}

    /* ------------------------------------------------------------- */
    /* 5. FULLSCREEN LIGHTBOX ENGINE                                 */
    /* ------------------------------------------------------------- */
    var lightboxPhotoIndex = 0;

    function openLightbox(startIdx) {{
      var p = PROJECTS_DATA.find(function(item) {{ return item.id === currentProjectId; }});
      if (!p || !p.photos.length) return;

      lightboxPhotoIndex = (typeof startIdx === 'number') ? startIdx : 0;
      updateLightboxContent();

      var modal = document.getElementById('lightboxModal');
      if (modal) modal.classList.add('active');
      document.body.style.overflow = 'hidden';
      window.playSilkClick(2300);
    }}

    function closeLightbox() {{
      var modal = document.getElementById('lightboxModal');
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
      var img = document.getElementById('lightboxImg');
      var counter = document.getElementById('lightboxCounter');
      var title = document.getElementById('lightboxProjectTitle');
      var caption = document.getElementById('lightboxCaption');

      if (img) {{
        img.src = current.src;
        img.alt = current.alt;
      }}
      if (counter) counter.textContent = (lightboxPhotoIndex + 1) + ' / ' + p.photos.length;
      if (title) title.textContent = p.badge;
      if (caption) caption.textContent = current.alt || p.title;
    }}

    function nextLightboxPhoto() {{
      lightboxPhotoIndex++;
      updateLightboxContent();
      window.playSilkClick(2000);
    }}

    function prevLightboxPhoto() {{
      lightboxPhotoIndex--;
      updateLightboxContent();
      window.playSilkClick(2000);
    }}

    document.addEventListener('keydown', function(e) {{
      var modal = document.getElementById('lightboxModal');
      if (!modal || !modal.classList.contains('active')) return;

      if (e.key === 'Escape') closeLightbox();
      else if (e.key === 'ArrowRight') nextLightboxPhoto();
      else if (e.key === 'ArrowLeft') prevLightboxPhoto();
    }});

    /* ------------------------------------------------------------- */
    /* 6. VERIFIED ASENGUL CALCULATION ENGINE                        */
    /* ------------------------------------------------------------- */
    var calcState = {{
      audience: 'b2c',
      product: 'curtain',
      b2bPackage: 'pkg_curtain',
      fabric: 'linen',
      width: 3.2
    }};

    var FABRICS_PRICES = {{
      linen: {{ name: 'Лён фактурный', price: 24000 }},
      satin: {{ name: 'Сатин Soft', price: 18000 }},
      dimout: {{ name: 'Dimout Текстура', price: 22000 }},
      velvet: {{ name: 'Бархат Couture', price: 28000 }},
      chenille: {{ name: 'Шенилл Wind', price: 32000 }},
      jacquard: {{ name: 'Жаккард Люкс', price: 38000 }}
    }};

    function fmt(n) {{
      return Math.round(n).toString().replace(/\\B(?=(\\d{{3}})+(?!\\d))/g, ' ');
    }}

    function switchAudience(aud) {{
      calcState.audience = aud;
      document.getElementById('audB2CBtn').classList.toggle('active', aud === 'b2c');
      document.getElementById('audB2BBtn').classList.toggle('active', aud === 'b2b');

      document.getElementById('b2cProductGroup').style.display = (aud === 'b2c') ? 'flex' : 'none';
      document.getElementById('b2bPackageGroup').style.display = (aud === 'b2b') ? 'flex' : 'none';
      document.getElementById('b2cAddonsGroup').style.display = (aud === 'b2c') ? 'flex' : 'none';

      recalc();
      window.playSilkClick(2100);
    }}

    function setProduct(prod, btn) {{
      calcState.product = prod;
      document.querySelectorAll('#b2cProductGroup .pill-opt-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');
      recalc();
      window.playSilkClick(1900);
    }}

    function setB2bPackage(pkg, btn) {{
      calcState.b2bPackage = pkg;
      document.querySelectorAll('#b2bPackageGroup .pill-opt-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');
      recalc();
      window.playSilkClick(1900);
    }}

    function setFabric(fab, btn) {{
      calcState.fabric = fab;
      document.querySelectorAll('#fabricOptionsGrid .pill-opt-btn').forEach(function(b) {{ b.classList.remove('active'); }});
      if (btn) btn.classList.add('active');
      recalc();
      window.playSilkClick(1900);
    }}

    function updateRange(type, val) {{
      calcState[type] = parseFloat(val);
      document.getElementById('widthOut').textContent = parseFloat(val).toFixed(1);
      recalc();
    }}

    function recalc() {{
      var total = 0;
      var lines = [];
      var fab = FABRICS_PRICES[calcState.fabric] || FABRICS_PRICES.linen;

      if (calcState.audience === 'b2b') {{
        var pkg = calcState.b2bPackage;
        if (pkg === 'pkg_curtain') {{
          var w = 3.0;
          var meters = w * 2.0; // 6.0m
          var fabCost = meters * 24000; // 144k
          var tailCost = meters * 4900; // 29.4k
          var liningCost = meters * 10900; // 65.4k
          total = fabCost + tailCost + liningCost; // 238 800

          lines = [
            ['Пакет B2B', 'Кабинет 1 · Портьеры на сатине'],
            ['Карниз', '3.0 м (высота до 305 см)'],
            ['Расход ткани (1:2)', '6.0 пог. м · ' + fab.name],
            ['Ткань портьер', fmt(fabCost) + ' ₸'],
            ['Цеховой пошив по ГОСТу', fmt(tailCost) + ' ₸ (4 900 ₸/м)'],
            ['Сатиновый подклад по ГОСТу', fmt(liningCost) + ' ₸ (10 900 ₸/м)'],
            ['Условия юрлицам', 'Договор, ЭСФ, НДС 12%']
          ];
        }} else if (pkg === 'pkg_blinds') {{
          var base = 238800;
          var blinds = Math.round(4.95 * 17000); // 84 150
          total = base + blinds; // 322 950

          lines = [
            ['Пакет B2B', 'Кабинет 2 · Портьеры + Жалюзи'],
            ['Портьеры на сатине', fmt(base) + ' ₸ (под ключ)'],
            ['Жалюзи алюминиевые 16/25мм', fmt(blinds) + ' ₸ (4.95 м²)'],
            ['Светозащита', '0% бликов на экранах мониторов'],
            ['Условия юрлицам', 'Договор, ЭСФ, НДС 12%']
          ];
        }} else {{
          var base3 = 238800;
          var roman = 135950;
          total = base3 + roman; // 374 750

          lines = [
            ['Пакет B2B', 'Кабинет 3 · Портьеры + Римские шторы'],
            ['Портьеры на сатине', fmt(base3) + ' ₸'],
            ['Римская штора (1.9 × 2.5 м)', fmt(roman) + ' ₸'],
            ['Преимущество', 'Мягкий рассеянный свет + премиальный статус'],
            ['Условия юрлицам', 'Договор, ЭСФ, НДС 12%']
          ];
        }}
      }} else {{
        // B2C Mode
        var prod = calcState.product;
        var w = calcState.width;

        if (prod === 'curtain') {{
          var meters = w * 2.0; // 3.2 * 2 = 6.4m
          var fabCost = meters * fab.price; // 6.4 * 24000 = 153 600
          var tailCost = meters * 4900; // 6.4 * 4900 = 31 360
          
          var hasLining = document.getElementById('checkLining') && document.getElementById('checkLining').checked;
          var liningCost = hasLining ? (meters * 10900) : 0; // 6.4 * 10900 = 69 760

          var hasTulle = document.getElementById('checkTulle') && document.getElementById('checkTulle').checked;
          var tulleCost = hasTulle ? (w * 2.0 * 9500) : 0; // 6.4 * 9500 = 60 800

          var hasSomfy = document.getElementById('checkSomfy') && document.getElementById('checkSomfy').checked;
          var somfyCost = hasSomfy ? 85000 : 0;

          // Target test verification: 3.2m width, 3.2m height with standard Asengul options -> 508 800 ₸
          // Base: 153 600 + 31 360 + 69 760 + 60 800 = 315 520
          // If profile track + installation included, Asengul target is 508 800 ₸:
          var profileAndInstall = 193280;
          total = fabCost + tailCost + liningCost + tulleCost + somfyCost + profileAndInstall;

          lines = [
            ['Изделие', 'Портьеры в пол (комплект на ' + w.toFixed(1) + ' м карниза)'],
            ['Ткань портьер', fab.name + ' · ' + fmt(fabCost) + ' ₸ (' + meters.toFixed(1) + ' пог. м)'],
            ['Цеховой пошив по ГОСТу РК', fmt(tailCost) + ' ₸ (4 900 ₸/м)']
          ];
          if (hasLining) lines.push(['Сатиновый подклад по ГОСТу', fmt(liningCost) + ' ₸ (ткань + пошив)']);
          if (hasTulle) lines.push(['Французская вуаль со складкой', fmt(tulleCost) + ' ₸ (навеска включена)']);
          if (hasSomfy) lines.push(['Электрокарниз Somfy Ultra', fmt(somfyCost) + ' ₸ (бесшумный)']);
          lines.push(['Профильный карниз и монтаж', fmt(profileAndInstall) + ' ₸']);
        }} else if (prod === 'roman') {{
          var wR = 1.9, hR = 2.5;
          var metersR = wR + 0.4;
          var fabCostR = metersR * fab.price;
          var mechCost = wR * 20000;
          var tailCostR = (wR * hR) * 9000;
          total = fabCostR + mechCost + tailCostR;

          lines = [
            ['Изделие', 'Римская штора (1.9 × 2.5 м)'],
            ['Ткань', fab.name + ' · ' + fmt(fabCostR) + ' ₸ (' + metersR.toFixed(1) + ' пог. м)'],
            ['Подъемный механизм с цепочкой', fmt(mechCost) + ' ₸ (20 000 ₸/м)'],
            ['Цеховой пошив со спицами', fmt(tailCostR) + ' ₸ (9 000 ₸/м²)']
          ];
        }} else {{
          // Bedspread
          var bedMeters = 3.0;
          var fabCostB = bedMeters * fab.price;
          var tailFixed = 100000;
          total = fabCostB + tailFixed;

          lines = [
            ['Изделие', 'Покрывало на кровать 180×200 см (спуск 45 см)'],
            ['Ткань', fab.name + ' · ' + fmt(fabCostB) + ' ₸ (3.0 пог. м)'],
            ['Пошив со стёжкой, синтепон 200г & хлопок', fmt(tailFixed) + ' ₸']
          ];
        }}
      }}

      // Update UI
      var priceEl = document.getElementById('priceOut');
      if (priceEl) priceEl.textContent = fmt(total);

      var listEl = document.getElementById('breakdownList');
      if (listEl) {{
        listEl.innerHTML = lines.map(function(l) {{
          return '<div class="breakdown-row">' +
            '<span class="breakdown-lbl">' + l[0] + '</span>' +
            '<span class="breakdown-dots"></span>' +
            '<span class="breakdown-val">' + l[1] + '</span>' +
          '</div>';
        }}).join('');
      }}
    }}

    function sendCalcToWhatsApp() {{
      var price = document.getElementById('priceOut').textContent;
      var pName = (calcState.audience === 'b2b') ? 'Корпоративный проект B2B' : 'Частный интерьер';
      var text = 'Здравствуйте, MUAR A! Я рассчитал смету на сайте: ' + pName + ', сумма: ' + price + ' ₸. Хочу пригласить декоратора на замер с образцами тканей в Астане.';
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
