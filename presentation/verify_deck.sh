#!/usr/bin/env bash
# ==============================================================================
# MARÉ Decorative Studio · Executive Interactive Deck QA Verification Suite
# ==============================================================================

set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

GREEN="[0;32m"
RED="[0;31m"
YELLOW="[1;33m"
CYAN="[0;36m"
BOLD="[1m"
NC="[0m"

PASSED_CHECKS=0
FAILED_CHECKS=0

echo -e "${BOLD}${CYAN}======================================================================${NC}"
echo -e "${BOLD}${CYAN}  MARÉ DECORATIVE STUDIO · EXECUTIVE DECK VERIFICATION SUITE         ${NC}"
echo -e "${BOLD}${CYAN}  Target: Standalone SPA Executive Deck Release                      ${NC}"
echo -e "${BOLD}${CYAN}======================================================================${NC}"
echo ""

report_pass() {
    echo -e "  [${GREEN}PASS${NC}] $1"
    ((PASSED_CHECKS++)) || true
}

report_fail() {
    echo -e "  [${RED}FAIL${NC}] $1"
    ((FAILED_CHECKS++)) || true
}

report_warn() {
    echo -e "  [${YELLOW}WARN${NC}] $1"
}

echo -e "${BOLD}[1/5] Checking Release Files Presence & Sizes...${NC}"

REQUIRED_FILES=(
    ".nojekyll:GitHub Pages Configuration:0"
    "index.html:Interactive Presentation Engine:20000"
    "README.md:Executive Deck Manual & Hotkeys:5000"
    "DELIVERY.md:Delivery Passport & SLA Spec:5000"
    "STRATEGY_AND_ROI.md:Strategic Foundation & Client Psychology:10000"
    "DESIGN_SYSTEM_AND_ART_DIRECTION.md:Art Direction & UI Kit Spec:10000"
    "SLIDE_NARRATIVES_AND_COPY.md:Slide Narratives & Luxury Copy:10000"
    "PITCH_SPEECH.md:15-min Pitch Script & Objection Handling:5000"
    "mobile.html:Mobile WhatsApp Story Presentation:10000"
)

for item in "${REQUIRED_FILES[@]}"; do
    IFS=":" read -r file desc min_size <<< "$item"
    if [[ -f "$file" ]]; then
        size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo 0)
        if (( size >= min_size )); then
            report_pass "File exists: $file ($desc, $size bytes)"
        else
            report_fail "File $file is smaller than expected ($size < $min_size bytes)"
        fi
    else
        report_fail "Missing mandatory file: $file ($desc)"
    fi
done

echo ""

echo -e "${BOLD}[2/5] Checking Local Media Assets Referenced by index.html...${NC}"

MEDIA_ASSETS=(
    "../assets/atelier-poster.jpg"
    "../assets/hero-curtains.mp4"
    "../screenshot-ba-living.png"
    "../screenshot-kp-evening.png"
    "../screenshot-kp-night.png"
)

for asset in "${MEDIA_ASSETS[@]}"; do
    if [[ -f "$asset" ]]; then
        size=$(stat -f%z "$asset" 2>/dev/null || stat -c%s "$asset" 2>/dev/null || echo 0)
        report_pass "Media asset located: $asset ($size bytes)"
    else
        report_fail "Referenced media asset NOT found: $asset"
    fi
done

echo ""

echo -e "${BOLD}[3/5] Validating HTML5 Structure & Inline JavaScript...${NC}"

if grep -qi "<!doctype html>" index.html; then
    report_pass "HTML5 DOCTYPE declared"
else
    report_fail "Missing HTML5 DOCTYPE in index.html"
fi

if grep -q 'name="viewport"' index.html; then
    report_pass "Responsive viewport meta tag present"
else
    report_fail "Missing viewport meta tag in index.html"
fi

if grep -qi 'charset="utf-8"' index.html; then
    report_pass "UTF-8 character encoding specified"
else
    report_fail "Missing UTF-8 charset declaration"
fi

if command -v node >/dev/null 2>&1; then
    if node -e "
        const fs = require('fs');
        const html = fs.readFileSync('index.html', 'utf8');
        const scriptMatch = html.match(/<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>/i);
        if (!scriptMatch) { console.error('No script found'); process.exit(1); }
        new Function(scriptMatch[1]);
    " 2>/dev/null; then
        report_pass "Inline JavaScript syntax parsed without errors (Node.js engine)"
    else
        report_fail "Inline JavaScript syntax error detected in index.html"
    fi
else
    report_warn "Node.js not found in PATH; skipping AST JS syntax check"
fi

echo ""

echo -e "${BOLD}[4/5] Checking Key Interactive Components & Slide Nodes...${NC}"

REQUIRED_ELEMENTS=(
    "slide-1:Slide 1: Manifest"
    "slide-2:Slide 2: Drapery Math & Configurator"
    "slide-3:Slide 3: Lighting Scenario Simulator"
    "slide-4:Slide 4: Mobile Dossier & Client KP"
    "slide-5:Slide 5: Two Doors B2B/B2C"
    "slide-6:Slide 6: Voice AI & PWA"
    "slide-7:Slide 7: Labor Breakdown 155-225h"
    "slide-8:Slide 8: ROI & Commercial Proposal"
)

for el in "${REQUIRED_ELEMENTS[@]}"; do
    IFS=":" read -r el_id el_desc <<< "$el"
    if grep -q "id=\"${el_id}\"" index.html; then
        report_pass "Slide anchor node verified: #${el_id} (${el_desc})"
    else
        report_fail "Missing slide anchor node: #${el_id} in index.html"
    fi
done

echo ""

echo -e "${BOLD}[5/5] Testing Local HTTP Server Startup & Serving...${NC}"

TEST_PORT=$((8100 + RANDOM % 800))
python3 -m http.server "$TEST_PORT" >/dev/null 2>&1 &
SERVER_PID=$!

trap "kill $SERVER_PID 2>/dev/null || true" EXIT

sleep 1

HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:$TEST_PORT/index.html" || echo "000")

if [[ "$HTTP_STATUS" == "200" ]]; then
    report_pass "Local HTTP server responds with HTTP 200 OK on port $TEST_PORT"
else
    report_fail "HTTP server smoke test failed (status: $HTTP_STATUS)"
fi

kill $SERVER_PID 2>/dev/null || true
trap - EXIT

echo ""
echo -e "${BOLD}${CYAN}======================================================================${NC}"
echo -e "${BOLD}  VERIFICATION SUMMARY: ${GREEN}$PASSED_CHECKS PASSED${NC}, ${RED}$FAILED_CHECKS FAILED${NC}"
echo -e "${BOLD}${CYAN}======================================================================${NC}"

if (( FAILED_CHECKS == 0 )); then
    echo -e "${GREEN}${BOLD}>>> EXECUTIVE DECK RELEASE QA AUDIT: 100% SUCCESSFUL <<<${NC}"
    echo -e "Presentation is fully verified, self-contained, and ready for deployment."
    exit 0
else
    echo -e "${RED}${BOLD}>>> QA AUDIT DETECTED FAILURES. PLEASE INSPECT LOG ABOVE. <<<${NC}"
    exit 1
fi
