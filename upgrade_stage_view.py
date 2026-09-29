#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upgrades renderStageView in generate_presentation_html.py to use the new tactile slider.
"""

file_path = '/Users/vitalij/Downloads/шторы нов/generate_presentation_html.py'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_stage_ba = '''      if (p.has_ba) {{
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
      }}'''

new_stage_ba = '''      if (p.has_ba) {{
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
      }}'''

old_stage_rebind = '''      // Re-bind BA slider if present
      if (p.has_ba) {{
        initBaSlider('stageBaSlider', 'stageBaBeforeLayer', 'stageBaHandleLine');
      }}'''

new_stage_rebind = '''      // Re-bind BA slider if present
      if (p.has_ba) {{
        if (window.MuarInteractive && window.MuarInteractive.MuarBeforeAfterSlider) {{
          window.MuarInteractive.stageSlider = new window.MuarInteractive.MuarBeforeAfterSlider('stageBaSlider', {{
            soundEngine: window.MuarInteractive.soundscape
          }});
        }} else {{
          initBaSlider('stageBaSlider', 'stageBaBeforeLayer', 'stageBaHandleLine');
        }}
      }}'''

if old_stage_ba in content:
    content = content.replace(old_stage_ba, new_stage_ba, 1)

if old_stage_rebind in content:
    content = content.replace(old_stage_rebind, new_stage_rebind, 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Stage BA view upgraded in generate_presentation_html.py!")
