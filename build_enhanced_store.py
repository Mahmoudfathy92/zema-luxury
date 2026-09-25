import base64
import os

base_dir = r'C:\Users\User\.gemini\antigravity\scratch\zema-luxury'
assets_dir = os.path.join(base_dir, 'assets')
products_dir = os.path.join(base_dir, 'products')

def get_b64(filepath, mime='image/jpeg'):
    if not os.path.exists(filepath):
        print('Missing:', filepath)
        return ''
    with open(filepath, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f'data:{mime};base64,{data}'

logo_b64 = get_b64(os.path.join(base_dir, 'zema-logo.png'), 'image/png')
hero_b64 = get_b64(os.path.join(assets_dir, 'zema-hero-D2aEWRdl.jpg'))
burgundy_b64 = get_b64(os.path.join(assets_dir, 'zema-burgundy-iHdryKjr.jpg'))
olive_b64 = get_b64(os.path.join(assets_dir, 'zema-olive-daIBNZJC.jpg'))
hobo_b64 = get_b64(os.path.join(assets_dir, 'zema-hobo-DtHUMc-D.jpg'))

bag_burgundy_b64 = get_b64(os.path.join(products_dir, 'bag-burgundy.jpg'))
bag_camel_b64 = get_b64(os.path.join(products_dir, 'bag-camel-tote.jpg'))
bag_crossbody_b64 = get_b64(os.path.join(products_dir, 'bag-mini-crossbody.jpg'))
bag_quilted_b64 = get_b64(os.path.join(products_dir, 'bag-quilted-noir.jpg'))

css_file = r'C:\Users\User\.gemini\antigravity\scratch\zema-vibes-hub.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

template = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5" />
  <title>ZEMA | Contemporary Luxury Handbags & Accessories</title>
  <meta name="description" content="ZEMA - حقائب وإكسسوارات نسائية معاصرة وفاخرة صُممت بكل فخر في مصر." />
  
  <!-- Google Fonts: Cairo & Playfair Display -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
  __CSS_CONTENT__

  /* Quiet Luxury Palette & Variables */
  :root {
    --zema-espresso: #1A1918;
    --zema-cream: #FAF9F6;
    --zema-sand: #EAE6DF;
    --zema-gold: #C5A059;
    --zema-green: #1B7D3F;
    --zema-border: #EFECE6;
  }

  * { box-sizing: border-box; }

  body {
    font-family: 'Cairo', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    background-color: var(--zema-cream);
    color: var(--zema-espresso);
    margin: 0;
    padding: 0;
    overflow-x: hidden;
    transition: all 0.2s ease;
  }

  [dir="ltr"] body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  }

  /* ========================================================== */
  /* ⚡ 1. ANIMATED TICKER ANNOUNCEMENT BAR (EGP 2,500 THRESHOLD) */
  /* ========================================================== */
  .ticker-wrap {
    width: 100%;
    overflow: hidden;
    background: var(--zema-espresso);
    color: #FAF9F6;
    padding: 9px 0;
    position: relative;
    border-bottom: 1px solid rgba(197, 160, 89, 0.25);
    z-index: 100;
  }
  .ticker-track {
    display: inline-flex;
    white-space: nowrap;
    will-change: transform;
    animation: marquee-scroll 24s linear infinite;
  }
  .ticker-wrap:hover .ticker-track {
    animation-play-state: paused;
  }
  .ticker-item {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 0 34px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.6px;
  }
  .ticker-item i {
    color: var(--zema-gold);
    width: 14px;
    height: 14px;
  }
  .ticker-dot {
    display: inline-block;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: var(--zema-gold);
    margin: 0 4px;
  }

  @keyframes marquee-scroll {
    0% { transform: translate3d(0, 0, 0); }
    100% { transform: translate3d(-50%, 0, 0); }
  }
  [dir="rtl"] @keyframes marquee-scroll {
    0% { transform: translate3d(0, 0, 0); }
    100% { transform: translate3d(50%, 0, 0); }
  }

  /* ========================================================== */
  /* 💎 BRAND LOGO: Prominent, High-Resolution & Elegant */
  /* ========================================================== */
  .brand-link {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 6px 14px;
    text-decoration: none;
  }
  .brand-logo-img {
    height: 68px;
    max-height: 74px;
    width: auto;
    object-fit: contain;
    display: block;
    filter: drop-shadow(0 1px 2px rgba(0,0,0,0.06));
    transition: transform 0.25s ease;
  }
  .brand-logo-img:hover {
    transform: scale(1.03);
  }
  @media (max-width: 768px) {
    .brand-logo-img {
      height: 56px;
      max-height: 60px;
    }
  }

  /* Language Switcher Button */
  .lang-switcher-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 700;
    background: rgba(26, 25, 24, 0.05);
    border: 1px solid rgba(26, 25, 24, 0.15);
    border-radius: 20px;
    color: var(--zema-espresso);
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .lang-switcher-btn:hover {
    background: var(--zema-espresso);
    color: #ffffff;
    border-color: var(--zema-espresso);
  }

  /* Utility Icons */
  .icon-btn {
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: transparent;
    border: none;
    color: var(--zema-espresso);
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.15s ease;
  }
  .icon-btn:hover {
    background: rgba(26, 25, 24, 0.06);
    transform: translateY(-1px);
  }
  .icon-btn .counter {
    position: absolute;
    top: 3px;
    right: 3px;
    background: var(--zema-espresso);
    color: #ffffff;
    font-size: 10px;
    font-weight: 700;
    min-width: 17px;
    height: 17px;
    line-height: 17px;
    border-radius: 9px;
    text-align: center;
    padding: 0 4px;
  }
  [dir="rtl"] .icon-btn .counter {
    right: auto;
    left: 3px;
  }

  /* ========================================================== */
  /* 🛍️ HOMEPAGE PRODUCT CARDS */
  /* ========================================================== */
  .product-card {
    position: relative;
    display: flex;
    flex-direction: column;
    background: #ffffff;
    border-radius: 12px;
    overflow: hidden;
    cursor: pointer;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
  }
  .product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.08);
  }
  .product-image-wrap {
    position: relative;
    aspect-ratio: 4/5;
    background: #f4f2ee;
    overflow: hidden;
  }
  .product-image-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }
  .product-card:hover .product-image-wrap img {
    transform: scale(1.05);
  }
  .sale-badge {
    position: absolute;
    top: 12px;
    right: 12px;
    background: #991b1b;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 8px;
    border-radius: 4px;
    letter-spacing: 0.5px;
    z-index: 2;
  }
  [dir="rtl"] .sale-badge {
    right: auto;
    left: 12px;
  }
  .favorite-button {
    position: absolute;
    top: 12px;
    left: 12px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.9);
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    z-index: 2;
    transition: background 0.2s, transform 0.15s;
  }
  [dir="rtl"] .favorite-button {
    left: auto;
    right: 12px;
  }
  .favorite-button:hover { transform: scale(1.1); }
  .favorite-button.active { color: #e11d48; }
  .favorite-button.active svg { fill: #e11d48; }

  .product-info-box {
    padding: 16px;
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: space-between;
  }
  .product-category {
    font-size: 12px;
    color: #88847d;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0 0 4px 0;
  }
  .prod-title {
    font-size: 15px;
    font-weight: 700;
    margin: 0 0 8px 0;
    color: var(--zema-espresso);
  }
  .price {
    display: flex;
    align-items: baseline;
    gap: 8px;
    margin-bottom: 12px;
  }
  .price strong {
    font-size: 16px;
    font-weight: 800;
    color: var(--zema-espresso);
  }
  .price del {
    font-size: 13px;
    color: #999;
  }

  .card-quick-add-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    padding: 11px 14px;
    background: var(--zema-espresso);
    color: #ffffff;
    border: none;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    transition: background 0.2s ease, transform 0.15s ease;
  }
  .card-quick-add-btn:hover {
    background: #383533;
    transform: translateY(-1px);
  }

  /* ========================================================== */
  /* 📄 2. PRODUCT DETAIL PAGE (PDP) */
  /* ========================================================== */
  #pdp-view {
    display: none;
    min-height: 80vh;
    padding-bottom: 90px;
    background: var(--zema-cream);
  }
  .pdp-breadcrumbs {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: #777;
    margin: 20px 0 28px 0;
    flex-wrap: wrap;
  }
  .pdp-breadcrumbs a {
    color: #777;
    text-decoration: none;
  }
  .pdp-breadcrumbs a:hover {
    color: var(--zema-espresso);
  }
  .pdp-breadcrumbs span.active {
    color: var(--zema-espresso);
    font-weight: 700;
  }

  .pdp-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 48px;
    max-width: 1240px;
    margin: 0 auto;
    align-items: start;
  }
  @media (max-width: 900px) {
    .pdp-layout {
      grid-template-columns: 1fr;
      gap: 32px;
    }
  }

  /* Gallery */
  .pdp-gallery {
    position: sticky;
    top: 90px;
  }
  .pdp-main-image-wrap {
    width: 100%;
    aspect-ratio: 4/5;
    background: #f0eee9;
    border-radius: 14px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
  }
  .pdp-main-image-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.35s ease;
  }
  .pdp-main-image-wrap:hover img {
    transform: scale(1.04);
  }
  .pdp-thumbnails-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-top: 14px;
  }
  .pdp-thumb-btn {
    aspect-ratio: 1;
    background: #f0eee9;
    border-radius: 8px;
    overflow: hidden;
    border: 2px solid transparent;
    cursor: pointer;
    padding: 0;
    transition: all 0.2s;
  }
  .pdp-thumb-btn img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .pdp-thumb-btn.active {
    border-color: var(--zema-espresso);
    box-shadow: 0 0 0 1px var(--zema-espresso);
  }

  /* PDP Content Details */
  .pdp-details {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .pdp-eyebrow {
    font-size: 13px;
    font-weight: 700;
    color: var(--zema-gold);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin: 0;
  }
  .pdp-title {
    font-size: 32px;
    font-weight: 800;
    line-height: 1.2;
    margin: 4px 0 12px 0;
  }
  .pdp-price-row {
    display: flex;
    align-items: baseline;
    gap: 12px;
  }
  .pdp-price-current {
    font-size: 26px;
    font-weight: 900;
    color: var(--zema-espresso);
  }
  .pdp-price-old {
    font-size: 18px;
    color: #999;
    text-decoration: line-through;
  }
  .pdp-saving-badge {
    background: #fef2f2;
    color: #991b1b;
    border: 1px solid #fecaca;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 700;
  }

  /* Guarantees Box */
  .pdp-perks-box {
    background: #ffffff;
    border: 1px solid var(--zema-border);
    border-radius: 10px;
    padding: 16px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 8px 0;
  }
  .pdp-perk-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 12px;
    font-weight: 700;
  }
  .pdp-perk-item i {
    color: var(--zema-green);
    width: 18px;
    height: 18px;
    flex-shrink: 0;
  }

  /* Actions */
  .pdp-qty-action-row {
    display: flex;
    gap: 12px;
    align-items: stretch;
    margin-top: 10px;
  }
  .pdp-qty-selector {
    display: flex;
    align-items: center;
    border: 1px solid #dcd7ce;
    border-radius: 8px;
    background: #ffffff;
  }
  .pdp-qty-btn {
    width: 44px;
    height: 100%;
    background: none;
    border: none;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
  }
  .pdp-qty-num {
    padding: 0 12px;
    font-size: 16px;
    font-weight: 800;
  }
  .pdp-add-cart-btn {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 16px 28px;
    background: var(--zema-espresso);
    color: #ffffff;
    border: none;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    transition: background 0.2s, transform 0.15s;
  }
  .pdp-add-cart-btn:hover {
    background: #33312e;
    transform: translateY(-1px);
  }

  /* Accordions */
  .pdp-accordion-box {
    margin-top: 20px;
    border: 1px solid var(--zema-border);
    border-radius: 10px;
    background: #ffffff;
    overflow: hidden;
  }
  .pdp-acc-item {
    border-bottom: 1px solid var(--zema-border);
  }
  .pdp-acc-item:last-child {
    border-bottom: none;
  }
  .pdp-acc-header {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 20px;
    background: none;
    border: none;
    font-size: 15px;
    font-weight: 800;
    color: var(--zema-espresso);
    cursor: pointer;
    text-align: inherit;
  }
  .pdp-acc-content {
    display: none;
    padding: 0 20px 18px 20px;
    font-size: 14px;
    color: #555;
    line-height: 1.7;
  }
  .pdp-acc-content.open {
    display: block;
  }

  /* ========================================================== */
  /* 📱 STICKY BOTTOM BAR ON MOBILE FOR PDP */
  /* ========================================================== */
  .mobile-sticky-bar {
    display: none;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(10px);
    border-top: 1px solid #e8e4db;
    padding: 12px 16px;
    z-index: 999;
    box-shadow: 0 -4px 16px rgba(0,0,0,0.08);
    align-items: center;
    justify-content: space-between;
    gap: 12px;
  }
  @media (max-width: 768px) {
    body.is-pdp .mobile-sticky-bar {
      display: flex;
    }
  }

      /* ========================================================== */
  /* 🛍️ 3. EXACT PREVIOUS PROJECT CART & CHECKOUT PAGES */
  /* ========================================================== */
  .page-view-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px 80px 20px;
  }
  .page-header-box {
    text-align: center;
    margin-bottom: 32px;
  }
  .page-eyebrow {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.15em;
    color: var(--zema-gold);
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .page-main-title {
    font-size: 32px;
    font-family: var(--zema-serif);
    font-weight: 700;
    color: var(--zema-espresso);
    margin: 0;
  }

  /* Free Shipping Meter (Threshold 2,500 EGP) */
  .cart-shipping-meter {
    background: #fbfaf8;
    border: 1px solid #eae6de;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 24px;
    text-align: center;
  }
  .meter-bar-track {
    width: 100%;
    height: 8px;
    background: #e8e4db;
    border-radius: 4px;
    margin-top: 10px;
    overflow: hidden;
  }
  .meter-bar-fill {
    height: 100%;
    background: var(--zema-green);
    border-radius: 4px;
    transition: width 0.35s ease;
  }

  /* Cart Items Table / List (Exact Previous Project) */
  .cart-items-table {
    border-top: 1px solid #eae6de;
    border-bottom: 1px solid #eae6de;
    margin-bottom: 24px;
  }
  .cart-row {
    display: flex;
    gap: 20px;
    padding: 20px 0;
    border-bottom: 1px solid #f2efe9;
    align-items: center;
  }
  .cart-row:last-child {
    border-bottom: none;
  }
  .cart-img-thumb {
    width: 90px;
    height: 110px;
    object-fit: cover;
    border-radius: 8px;
    background: #f4f2ee;
    border: 1px solid #eae6de;
    flex-shrink: 0;
  }
  .cart-item-details {
    flex: 1;
    min-width: 0;
  }
  .cart-item-heading {
    font-size: 16px;
    font-weight: 700;
    margin: 0 0 4px 0;
  }
  .cart-sku-badge {
    font-size: 12px;
    color: #888;
    font-family: monospace;
    margin-bottom: 8px;
  }
  .cart-item-price-val {
    font-size: 15px;
    font-weight: 800;
    color: var(--zema-espresso);
  }
  .cart-actions-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 12px;
  }
  .cart-qty-control {
    display: inline-flex;
    align-items: center;
    border: 1px solid #dcd7ce;
    border-radius: 6px;
    background: #faf9f6;
  }
  .cart-qty-btn {
    background: none;
    border: none;
    width: 32px;
    height: 32px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .cart-qty-btn:hover { background: #eeebe3; }
  .cart-qty-display {
    padding: 0 12px;
    font-size: 14px;
    font-weight: 700;
  }
  .cart-remove-link {
    background: none;
    border: none;
    cursor: pointer;
    color: #dc2626;
    font-size: 13px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 4px;
  }
  .cart-remove-link:hover { text-decoration: underline; }

  /* Cart Bottom Summary Bar */
  .cart-bottom-bar {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    padding: 16px 0;
  }
  .cart-subtotal-text {
    font-size: 16px;
    color: #555;
  }
  .cart-subtotal-val {
    font-size: 20px;
    font-weight: 800;
    color: var(--zema-espresso);
  }
  .btn-proceed-co {
    padding: 14px 36px;
    background: var(--zema-espresso);
    color: #ffffff;
    font-weight: 800;
    font-size: 15px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    transition: background 0.2s, transform 0.15s;
  }
  .btn-proceed-co:hover {
    background: #3c3937;
    transform: translateY(-1px);
  }

  /* Empty Cart View */
  .cart-empty-view {
    text-align: center;
    padding: 80px 20px;
    background: #faf9f6;
    border: 1px solid #eae6de;
    border-radius: 16px;
  }
  .btn-start-shopping {
    display: inline-block;
    padding: 12px 30px;
    background: var(--zema-espresso);
    color: #ffffff;
    font-size: 13px;
    font-weight: 800;
    border-radius: 8px;
    text-decoration: none;
    margin-top: 16px;
    cursor: pointer;
    border: none;
  }

  /* ========================================================== */
  /* 🇪🇬 CHECKOUT PAGE CONTAINER (EXACT PREVIOUS PROJECT) */
  /* ========================================================== */
  .co-page-wrapper {
    max-width: 780px;
    margin: 0 auto;
    padding: 40px 20px 90px 20px;
  }
  .co-card-box {
    background: #ffffff;
    border: 1px solid #eae6de;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  }

  /* 1. Ordered Items Summary at Top (Previous Project exact layout) */
  .co-products-summary-list {
    list-style: none;
    padding: 20px 24px;
    margin: 0;
    background: #faf9f6;
    border-bottom: 1px solid #eae6de;
  }
  .co-prod-item-line {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    margin-bottom: 10px;
    color: #444;
  }
  .co-prod-item-line:last-child {
    margin-bottom: 0;
  }
  .co-prod-name-qty {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .co-prod-qty-badge {
    color: #888;
    font-size: 13px;
  }
  .co-prod-price-badge {
    font-weight: 700;
    color: var(--zema-espresso);
  }

  /* 2. Order Totals Block */
  .co-totals-block {
    padding: 20px 24px;
    background: #ffffff;
    border-bottom: 1px solid #eae6de;
  }
  .co-total-row {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    color: #666;
    margin-bottom: 8px;
  }
  .co-total-row.discount-active {
    color: #16a34a;
    font-weight: 700;
  }
  .co-final-total-row {
    display: flex;
    justify-content: space-between;
    font-size: 18px;
    font-weight: 800;
    color: var(--zema-espresso);
    padding-top: 12px;
    margin-top: 12px;
    border-top: 1px dashed #dcd7ce;
  }

  /* 3. Promo Code Form */
  .co-promo-row {
    display: flex;
    gap: 10px;
    margin-top: 14px;
    padding-top: 14px;
    border-top: 1px solid #f0eee9;
  }
  .co-promo-input {
    flex: 1;
    padding: 9px 14px;
    border: 1px solid #dcd7ce;
    border-radius: 6px;
    font-size: 13px;
    background: #faf9f6;
  }
  .co-promo-btn {
    padding: 9px 18px;
    background: #2c2a29;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
  }
  .co-promo-btn:hover { background: #444; }
  .co-promo-msg {
    font-size: 12px;
    margin-top: 6px;
    text-align: center;
  }
  .co-promo-msg.ok { color: #16a34a; font-weight: 700; }
  .co-promo-msg.err { color: #dc2626; }

  /* 4. Form Fields Area */
  .co-form-area {
    padding: 28px 24px;
    background: #faf9f6;
  }
  .co-form-group {
    margin-bottom: 16px;
  }
  .co-form-group label {
    display: block;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 6px;
    color: var(--zema-espresso);
  }
  .co-input {
    width: 100%;
    padding: 11px 14px;
    border: 1px solid #dcd7ce;
    border-radius: 8px;
    font-size: 14px;
    font-family: inherit;
    background: #ffffff;
  }
  .co-input:focus {
    outline: none;
    border-color: var(--zema-espresso);
    box-shadow: 0 0 0 2px rgba(44, 42, 41, 0.12);
  }
  .co-input.input-error {
    border-color: #dc2626;
  }
  .co-err-text {
    font-size: 11px;
    color: #dc2626;
    margin-top: 4px;
  }

  /* Account Toggle Box */
  .co-account-box {
    background: #ffffff;
    border: 1px solid #eae6de;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 18px;
  }

  /* Payment Methods Fieldset (Previous Project) */
  .co-payment-fieldset {
    border: 1px solid #e2ded5;
    border-radius: 10px;
    padding: 16px;
    background: #ffffff;
    margin-bottom: 20px;
  }
  .co-payment-legend {
    font-size: 11px;
    font-weight: 800;
    color: #666;
    text-transform: uppercase;
    padding: 0 6px;
  }
  .co-pay-option {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 14px;
    border: 1px solid #dcd7ce;
    border-radius: 8px;
    margin-top: 10px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .co-pay-option.active {
    border: 2px solid #b45309;
    background: #fef3c7;
    box-shadow: 0 2px 8px rgba(180, 83, 9, 0.12);
  }
  .co-pay-option.disabled {
    opacity: 0.5;
    cursor: not-allowed;
    background: #faf9f6;
  }
  .co-pay-badge-soon {
    font-size: 10px;
    background: #eee;
    color: #666;
    padding: 2px 8px;
    border-radius: 4px;
    margin-left: auto;
  }
  [dir="rtl"] .co-pay-badge-soon {
    margin-left: 0;
    margin-right: auto;
  }

  /* Submit Button & Notes */
  .btn-submit-order-final {
    width: 100%;
    padding: 16px;
    background: var(--zema-espresso);
    color: #ffffff;
    border: 2px solid var(--zema-espresso);
    border-radius: 8px;
    font-size: 16px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 4px 16px rgba(0,0,0,0.18);
    transition: background 0.2s, transform 0.15s;
    margin-bottom: 12px;
  }
  .btn-submit-order-final:hover {
    background: #3c3937;
    transform: translateY(-1px);
  }
  .co-guarantee-note {
    font-size: 12px;
    color: #666;
    text-align: center;
    line-height: 1.6;
    padding-top: 12px;
    border-top: 1px solid #eae6de;
    margin-top: 14px;
  }

  /* Thank You Page */
  .ty-page-container {
    max-width: 680px;
    margin: 0 auto;
    padding: 60px 20px 90px 20px;
    text-align: center;
  }
  .ty-check-circle {
    width: 72px;
    height: 72px;
    border-radius: 50%;
    border: 2px solid var(--zema-green);
    color: var(--zema-green);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 20px auto;
  }
  .ty-order-box {
    display: inline-block;
    border: 1px solid #eae6de;
    padding: 12px 28px;
    background: #faf9f6;
    border-radius: 8px;
    margin: 20px 0;
  }
  .ty-details-card {
    background: #ffffff;
    border: 1px solid #eae6de;
    border-radius: 12px;
    padding: 22px;
    text-align: start;
    line-height: 1.9;
    font-size: 14px;
    margin: 24px 0;
  }

  /* RTL Specific Adjustments */
  [dir="rtl"] .utility-left { order: 1; }
  [dir="rtl"] .utility-right { order: 3; }
  [dir="rtl"] .brand-link { order: 2; }
  [dir="rtl"] .hero-arrow.left { right: 20px; left: auto; }
  [dir="rtl"] .hero-arrow.right { left: 20px; right: auto; }
  </style>
</head>
<body>

  <!-- ========================================================== -->
  <!-- ⚡ 1. ANIMATED TICKER (EGP 2,500 THRESHOLD) -->
  <!-- ========================================================== -->
  <div class="ticker-wrap" aria-label="Announcements">
    <div class="ticker-track">
      <div class="ticker-item">
        <i data-lucide="truck"></i>
        <span id="ticker-msg-1">شحن مجاني لكافة محافظات مصر للطلبات فوق 2,500 ج.م</span>
        <span class="ticker-dot"></span>
      </div>
      <div class="ticker-item">
        <i data-lucide="zap"></i>
        <span id="ticker-msg-2">توصيل سريع لباب بيتك خلال 24 - 48 ساعة</span>
        <span class="ticker-dot"></span>
      </div>
      <div class="ticker-item">
        <i data-lucide="shield-check"></i>
        <span id="ticker-msg-3">حق معاينة وفحص الشحنة قبل الاستلام والدفع</span>
        <span class="ticker-dot"></span>
      </div>
      <div class="ticker-item">
        <i data-lucide="sparkles"></i>
        <span id="ticker-msg-4">جلد طبيعي فاخر 100% بضمان زيما الرسمي</span>
        <span class="ticker-dot"></span>
      </div>
      <!-- Duplicate set for seamless infinite loop -->
      <div class="ticker-item">
        <i data-lucide="truck"></i>
        <span>شحن مجاني لكافة محافظات مصر للطلبات فوق 2,500 ج.م</span>
        <span class="ticker-dot"></span>
      </div>
      <div class="ticker-item">
        <i data-lucide="zap"></i>
        <span>توصيل سريع لباب بيتك خلال 24 - 48 ساعة</span>
        <span class="ticker-dot"></span>
      </div>
      <div class="ticker-item">
        <i data-lucide="shield-check"></i>
        <span>حق معاينة وفحص الشحنة قبل الاستلام والدفع</span>
        <span class="ticker-dot"></span>
      </div>
      <div class="ticker-item">
        <i data-lucide="sparkles"></i>
        <span>جلد طبيعي فاخر 100% بضمان زيما الرسمي</span>
        <span class="ticker-dot"></span>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="site-header">
    <div class="utility-row">
      <div class="utility-side utility-left">
        <button class="icon-btn mobile-menu-trigger" aria-label="Open menu" onclick="toggleMobileMenu()">
          <i data-lucide="menu"></i>
        </button>
        <button class="icon-btn" aria-label="Search" onclick="toggleSearchModal(true)">
          <i data-lucide="search"></i>
        </button>
        <a class="utility-link hidden sm:inline" href="#story" id="nav-our-story">قصتنا</a>
        
        <!-- Language Switcher Button -->
        <button class="lang-switcher-btn" onclick="toggleLanguage()" id="langSwitcherBtn">
          <span>🌐</span>
          <span id="currentLangLabel">English</span>
        </button>
      </div>

      <!-- Center Logo -->
      <a href="#top" class="brand-link" aria-label="ZEMA Home" onclick="showHomePage()">
        <img src="__LOGO_B64__" alt="ZEMA Luxury" class="brand-logo-img" />
      </a>

      <!-- Utility Right -->
      <div class="utility-side utility-right">
        <button class="icon-btn" aria-label="Account" onclick="toggleAccountModal(true)">
          <i data-lucide="user"></i>
        </button>
        <button class="icon-btn" aria-label="Wishlist" onclick="toggleWishlistDrawer(true)">
          <i data-lucide="heart"></i>
          <span class="counter" id="wishlistCountBadge">0</span>
        </button>
        <button class="icon-btn" aria-label="Shopping bag" onclick="showCartView()">
          <i data-lucide="shopping-bag"></i>
          <span class="counter" id="cartCountBadge">0</span>
        </button>
      </div>
    </div>

    <!-- Navigation Bar -->
    <nav class="desktop-nav" aria-label="Main navigation">
      <a href="#top" id="nav-home" onclick="showHomePage()">الرئيسية</a>
      <div class="bags-menu">
        <button class="nav-button" id="nav-bags">
          حقائب اليد <i data-lucide="chevron-down" style="width:14px;height:14px;"></i>
        </button>
        <div class="bags-dropdown">
          <a href="#bags-section" onclick="showHomePage()">حقائب اليد</a>
          <a href="#bags-section" onclick="showHomePage()">حقائب كتف</a>
          <a href="#bags-section" onclick="showHomePage()">حقائب كروس</a>
          <a href="#bags-section" onclick="showHomePage()">حقائب توت</a>
          <a href="#bags-section" onclick="showHomePage()">حقائب سهرة</a>
        </div>
      </div>
      <a href="#wallets" id="nav-wallets" onclick="showHomePage()">محافظ</a>
      <a href="#belts" id="nav-belts" onclick="showHomePage()">أحزمة</a>
      <a href="#accessories" id="nav-accessories" onclick="showHomePage()">إكسسوارات</a>
      <a href="#bags-section" id="nav-bestsellers" onclick="showHomePage()">الأكثر مبيعاً</a>
      <a href="#bags-section" class="nav-sale" id="nav-sale" onclick="showHomePage()">تخفيضات</a>
    </nav>
  </header>

  <!-- ========================================================== -->
  <!-- 🏠 1. HOMEPAGE VIEW (DEFAULT) -->
  <!-- ========================================================== -->
  <main id="home-view">
    
    <!-- Hero Slider -->
    <section id="top" class="hero-section">
      <article class="hero-slide is-active" id="hero-slide-1">
        <img src="__HERO_B64__" alt="ZEMA Luxury Campaign" class="hero-image" />
        <div class="hero-overlay"></div>
        <div class="hero-copy">
          <p class="eyebrow" id="hero-eye-1">صُممت لتناسب يومك</p>
          <h1 id="hero-title-1">Made for Your Everyday</h1>
          <p class="hero-subtitle" id="hero-sub-1">تصاميم مدروسة لترافقك بكل سلاسة وأناقة من أيام العمل إلى عطلات نهاية الأسبوع.</p>
          <a href="#bags-section" class="card-quick-add-btn" style="width:auto; padding: 12px 28px; border-radius: 30px; display:inline-flex;" id="hero-cta-1">تسوقي الحقائب</a>
        </div>
      </article>

      <article class="hero-slide" id="hero-slide-2" style="display:none;">
        <img src="__BURGUNDY_B64__" alt="ZEMA Luxury Handbag" class="hero-image" style="object-position:center 44%;" />
        <div class="hero-overlay"></div>
        <div class="hero-copy">
          <p class="eyebrow" id="hero-eye-2">ثقة وتألق دائم</p>
          <h1 id="hero-title-2">Carry Your Signature Style</h1>
          <p class="hero-subtitle" id="hero-sub-2">قطع يومية فاخرة صُممت خصيصاً للمرأة العصرية الواثقة من حضورها.</p>
          <a href="#bags-section" class="card-quick-add-btn" style="width:auto; padding: 12px 28px; border-radius: 30px; display:inline-flex;" id="hero-cta-2">اكتشفي حقائب اليد</a>
        </div>
      </article>

      <article class="hero-slide" id="hero-slide-3" style="display:none;">
        <img src="__OLIVE_B64__" alt="ZEMA Luxury Olive Bag" class="hero-image" style="object-position:center 38%;" />
        <div class="hero-overlay"></div>
        <div class="hero-copy">
          <p class="eyebrow" id="hero-eye-3">فخامة هادئة</p>
          <h1 id="hero-title-3">Timeless Pieces. Modern You.</h1>
          <p class="hero-subtitle" id="hero-sub-3">اكتشفي إكسسوارات راقية صُنعت بعناية لتناسب كل لحظاتك.</p>
          <a href="#bags-section" class="card-quick-add-btn" style="width:auto; padding: 12px 28px; border-radius: 30px; display:inline-flex;" id="hero-cta-3">تسوقي المجموعة</a>
        </div>
      </article>

      <button class="hero-arrow left" onclick="prevSlide()"><i data-lucide="chevron-right"></i></button>
      <button class="hero-arrow right" onclick="nextSlide()"><i data-lucide="chevron-left"></i></button>
    </section>

    <!-- Benefits Section -->
    <section class="benefit-grid">
      <div class="benefit">
        <i data-lucide="truck" style="width:28px;height:28px;"></i>
        <div>
          <strong id="ben-t1">شحن مجاني</strong>
          <span id="ben-d1">للطلبات فوق 2,500 ج.م</span>
        </div>
      </div>
      <div class="benefit">
        <i data-lucide="zap" style="width:28px;height:28px;"></i>
        <div>
          <strong id="ben-t2">توصيل سريع</strong>
          <span id="ben-d2">لجميع محافظات مصر</span>
        </div>
      </div>
      <div class="benefit">
        <i data-lucide="credit-card" style="width:28px;height:28px;"></i>
        <div>
          <strong id="ben-t3">دفع مرن</strong>
          <span id="ben-d3">دفع عند الاستلام متاح</span>
        </div>
      </div>
      <div class="benefit">
        <i data-lucide="package-check" style="width:28px;height:28px;"></i>
        <div>
          <strong id="ben-t4">استبدال سهل</strong>
          <span id="ben-d4">خلال 14 يوماً بكل سهولة</span>
        </div>
      </div>
    </section>

    <!-- Products Grid Section -->
    <section id="bags-section" class="product-section">
      <div class="section-heading">
        <div>
          <p class="eyebrow" id="prod-eye">مجموعة الحقائب المختارة</p>
          <h2 id="prod-heading">Designed for Your Everyday</h2>
          <p class="section-description" id="prod-desc">اضغطي على أي حقيبة لرؤية التفاصيل الكاملة، الزوايا المتعددة والخامات.</p>
        </div>
        <a href="#bags-section" class="text-link" id="view-all-bags">عرض كل الحقائب &larr;</a>
      </div>

      <div style="display:grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; max-width: 1280px; margin: 0 auto; padding: 0 16px;">
        
        <!-- Product 1 -->
        <article class="product-card" onclick="openPDP('p1')">
          <div class="product-image-wrap">
            <span class="sale-badge">SALE</span>
            <img src="__HOBO_B64__" alt="Mila Soft Hobo Bag" loading="lazy" />
            <button class="favorite-button" id="fav-btn-p1" onclick="event.stopPropagation(); toggleWishlistItem('p1', this)">
              <i data-lucide="heart"></i>
            </button>
          </div>
          <div class="product-info-box">
            <div>
              <p class="product-category">حقيبة كتف</p>
              <h3 class="prod-title">حقيبة ميلا هوبو ناعمة</h3>
              <div class="price">
                <strong>1,299.00 ج.م</strong>
                <del>1,699.00 ج.م</del>
              </div>
            </div>
            <button class="card-quick-add-btn" onclick="event.stopPropagation(); addToCart('p1', 1)">
              <i data-lucide="shopping-bag" style="width:16px;height:16px;"></i>
              <span class="btn-text-qa">إضافة سريعة للسلة</span>
            </button>
          </div>
        </article>

        <!-- Product 2 -->
        <article class="product-card" onclick="openPDP('p2')">
          <div class="product-image-wrap">
            <span class="sale-badge">SALE</span>
            <img src="__BURGUNDY_B64__" alt="Noor Curved Shoulder Bag" loading="lazy" />
            <button class="favorite-button" id="fav-btn-p2" onclick="event.stopPropagation(); toggleWishlistItem('p2', this)">
              <i data-lucide="heart"></i>
            </button>
          </div>
          <div class="product-info-box">
            <div>
              <p class="product-category">حقيبة كتف</p>
              <h3 class="prod-title">حقيبة نور كتف منحنية</h3>
              <div class="price">
                <strong>1,150.00 ج.م</strong>
                <del>1,450.00 ج.م</del>
              </div>
            </div>
            <button class="card-quick-add-btn" onclick="event.stopPropagation(); addToCart('p2', 1)">
              <i data-lucide="shopping-bag" style="width:16px;height:16px;"></i>
              <span class="btn-text-qa">إضافة سريعة للسلة</span>
            </button>
          </div>
        </article>

        <!-- Product 3 -->
        <article class="product-card" onclick="openPDP('p3')">
          <div class="product-image-wrap">
            <img src="__OLIVE_B64__" alt="Lina Structured Tote Bag" loading="lazy" />
            <button class="favorite-button" id="fav-btn-p3" onclick="event.stopPropagation(); toggleWishlistItem('p3', this)">
              <i data-lucide="heart"></i>
            </button>
          </div>
          <div class="product-info-box">
            <div>
              <p class="product-category">حقيبة توت</p>
              <h3 class="prod-title">حقيبة لينا توت منظمة</h3>
              <div class="price">
                <strong>1,499.00 ج.م</strong>
              </div>
            </div>
            <button class="card-quick-add-btn" onclick="event.stopPropagation(); addToCart('p3', 1)">
              <i data-lucide="shopping-bag" style="width:16px;height:16px;"></i>
              <span class="btn-text-qa">إضافة سريعة للسلة</span>
            </button>
          </div>
        </article>

        <!-- Product 4 -->
        <article class="product-card" onclick="openPDP('p4')">
          <div class="product-image-wrap">
            <span class="sale-badge">SALE</span>
            <img src="__HERO_B64__" alt="Aya Everyday Tote Bag" loading="lazy" />
            <button class="favorite-button" id="fav-btn-p4" onclick="event.stopPropagation(); toggleWishlistItem('p4', this)">
              <i data-lucide="heart"></i>
            </button>
          </div>
          <div class="product-info-box">
            <div>
              <p class="product-category">حقيبة توت</p>
              <h3 class="prod-title">حقيبة آية توت يومية</h3>
              <div class="price">
                <strong>1,399.00 ج.م</strong>
                <del>1,799.00 ج.م</del>
              </div>
            </div>
            <button class="card-quick-add-btn" onclick="event.stopPropagation(); addToCart('p4', 1)">
              <i data-lucide="shopping-bag" style="width:16px;height:16px;"></i>
              <span class="btn-text-qa">إضافة سريعة للسلة</span>
            </button>
          </div>
        </article>

      </div>
    </section>

    <!-- Editorial Banner -->
    <section class="editorial-banner">
      <img src="__HOBO_B64__" alt="ZEMA Luxury Editorial" loading="lazy" />
      <div class="editorial-shade"></div>
      <div class="editorial-copy">
        <p class="eyebrow" id="edit-eye">حقائب لكل الأوقات</p>
        <h2 id="edit-title">Designed for every chapter of your day.</h2>
        <a href="#bags-section" class="card-quick-add-btn" style="width:auto; padding: 12px 28px; border-radius: 30px; display:inline-flex;" id="edit-cta">اكتشفي الحقائب</a>
      </div>
    </section>

    <!-- Story Section -->
    <section id="story" class="story-section">
      <div class="story-image">
        <img src="__OLIVE_B64__" alt="ZEMA Craftsmanship" loading="lazy" />
      </div>
      <div class="story-copy">
        <p class="eyebrow" id="story-eye">قصة زيما</p>
        <h2 id="story-title">Designed for the way you live.</h2>
        <p id="story-p">في زيما (ZEMA)، نؤمن بأن القطع التي ترافقك يجب أن تعكس تفرد أسلوبك ونمط حياتك. مجموعاتنا توازن بين التصاميم الراقية والعملية الفائقة لتمنحك أناقة دائمة تليق بك في كل خطوة.</p>
        <a href="#bags-section" class="card-quick-add-btn" style="width:auto; padding: 12px 24px; border-radius: 30px; display:inline-flex;" id="story-cta">تعرفي أكثر على قصتنا</a>
      </div>
    </section>

  </main>

  <!-- ========================================================== -->
  <!-- 📄 2. DEDICATED PRODUCT DETAIL PAGE (PDP VIEW) -->
  <!-- ========================================================== -->
  <section id="pdp-view">
    <div style="max-width: 1240px; margin: 0 auto; padding: 0 16px;">
      
      <!-- Breadcrumbs -->
      <nav class="pdp-breadcrumbs">
        <a href="#top" onclick="showHomePage()">الرئيسية</a>
        <span>&larr;</span>
        <a href="#bags-section" onclick="showHomePage()" id="pdp-crumb-cat">حقائب اليد</a>
        <span>&larr;</span>
        <span class="active" id="pdp-crumb-title">حقيبة ميلا هوبو</span>
      </nav>

      <div class="pdp-layout">
        
        <!-- Left: Image Gallery with Multiple Angles -->
        <div class="pdp-gallery">
          <div class="pdp-main-image-wrap">
            <img id="pdpMainImage" src="__HOBO_B64__" alt="Product Angle" />
          </div>
          <div class="pdp-thumbnails-row" id="pdpThumbnailsContainer">
            <!-- 4 angles thumbnails rendered dynamically -->
          </div>
        </div>

        <!-- Right: Information, Materials, Dimensions, Sticky Mobile Cart -->
        <div class="pdp-details">
          <div>
            <p class="pdp-eyebrow" id="pdpEyebrow">MAISON ZEMA · إصدار محدود</p>
            <h1 class="pdp-title" id="pdpTitle">حقيبة ميلا هوبو ناعمة</h1>
            
            <div class="pdp-price-row">
              <span class="pdp-price-current" id="pdpPrice">1,299.00 ج.م</span>
              <span class="pdp-price-old" id="pdpOldPrice">1,699.00 ج.م</span>
              <span class="pdp-saving-badge" id="pdpSavingBadge">توفير 400 ج.م</span>
            </div>
          </div>

          <!-- Perks Box -->
          <div class="pdp-perks-box">
            <div class="pdp-perk-item">
              <i data-lucide="truck"></i>
              <span>شحن مجاني فوق 2,500 ج.م</span>
            </div>
            <div class="pdp-perk-item">
              <i data-lucide="shield-check"></i>
              <span>فحص ومعاينة عند الاستلام</span>
            </div>
            <div class="pdp-perk-item">
              <i data-lucide="clock"></i>
              <span>توصيل خلال 24 - 48 ساعة</span>
            </div>
            <div class="pdp-perk-item">
              <i data-lucide="rotate-ccw"></i>
              <span>استرجاع واستبدال 14 يوم</span>
            </div>
          </div>

          <!-- Color Swatches -->
          <div>
            <label style="display:block; font-size:13px; font-weight:700; margin-bottom:8px;">
              اللون المتاح: <span id="pdpSelectedColorName" style="color:#666;">هافان طبيعي</span>
            </label>
            <div style="display:flex; gap:10px;">
              <span style="background:#5C4033; width:26px; height:26px; border-radius:50%; display:inline-block; border:2px solid #000; cursor:pointer;"></span>
              <span style="background:#111111; width:26px; height:26px; border-radius:50%; display:inline-block; border:1px solid #ddd; cursor:pointer;"></span>
              <span style="background:#F5F2EB; width:26px; height:26px; border-radius:50%; display:inline-block; border:1px solid #ddd; cursor:pointer;"></span>
            </div>
          </div>

          <!-- Quantity & Add to Cart -->
          <div class="pdp-qty-action-row">
            <div class="pdp-qty-selector">
              <button class="pdp-qty-btn" onclick="changePdpQty(-1)">-</button>
              <span class="pdp-qty-num" id="pdpQtyNumber">1</span>
              <button class="pdp-qty-btn" onclick="changePdpQty(1)">+</button>
            </div>
            <button class="pdp-add-cart-btn" onclick="addCurrentPdpToCart()">
              <i data-lucide="shopping-bag"></i>
              <span id="pdpAddToCartBtnText">إضافة إلى سلة المشتريات</span>
            </button>
          </div>

          <!-- Accordion Specs -->
          <div class="pdp-accordion-box">
            
            <!-- Description -->
            <div class="pdp-acc-item">
              <button class="pdp-acc-header" onclick="togglePdpAccordion(this)">
                <span>الوصف وتفاصيل التصميم</span>
                <i data-lucide="chevron-down"></i>
              </button>
              <div class="pdp-acc-content open" id="pdpDescContent">
                حقيبة كتف عصرية تجمع بين الفخامة الهادئة والعملية اليومية. مصممة بانسيابية تمنحك إطلالة راقية في العمل، اللقاءات الرسمية وعطلات نهاية الأسبوع، مع مقصورة واسعة تسع كافة مقتنياتك الأساسية.
              </div>
            </div>

            <!-- Materials -->
            <div class="pdp-acc-item">
              <button class="pdp-acc-header" onclick="togglePdpAccordion(this)">
                <span>الخامات والصناعة الفاخرة</span>
                <i data-lucide="chevron-down"></i>
              </button>
              <div class="pdp-acc-content" id="pdpMaterialsContent">
                • <strong>جلد طبيعي فاخر 100%</strong> (Full-Grain Genuine Leather) بملمس ناعم ومقاوم للخدش.<br>
                • بطانة داخلية مخملية مقاومة للرطوبة وسهلة التنظيف.<br>
                • إكسسوارات معدنية ومفصلات مطلية بالذهب عيار 18 مقاومة لتغير اللون والصدأ.<br>
                • سحابات يابانية YKK عالية المتانة لنعومة تامة في الفتح والإغلاق.
              </div>
            </div>

            <!-- Dimensions -->
            <div class="pdp-acc-item">
              <button class="pdp-acc-header" onclick="togglePdpAccordion(this)">
                <span>الأبعاد والمقاسات</span>
                <i data-lucide="chevron-down"></i>
              </button>
              <div class="pdp-acc-content" id="pdpDimensionsContent">
                • <strong>العرض:</strong> 34 سم<br>
                • <strong>الارتفاع:</strong> 26 سم<br>
                • <strong>العمق:</strong> 12 سم<br>
                • <strong>طول حزام الكتف:</strong> 48 إلى 58 سم (قابل للتعديل)<br>
                • <strong>الوزن الإجمالي:</strong> 620 جرام خفيف ومريح للاستخدام طوال اليوم.
              </div>
            </div>

          </div>

          <!-- WhatsApp Direct Order -->
          <a id="pdpWaOrderBtn" href="#" target="_blank" class="btn-wa-checkout" style="padding:14px; font-size:14px; text-decoration:none;">
            <i data-lucide="message-circle"></i>
            <span>طلب فوري لهذه الحقيبة عبر WhatsApp</span>
          </a>

        </div>

      </div>

    </div>
  </section>

  <!-- Sticky Mobile Bottom Bar -->
  <aside class="mobile-sticky-bar" id="mobileStickyBar">
    <div style="display:flex; align-items:center; gap:10px;">
      <img id="stickyBarImg" src="__HOBO_B64__" style="width:42px; height:50px; object-fit:cover; border-radius:4px;" />
      <div>
        <strong id="stickyBarTitle" style="font-size:13px; display:block; max-width:140px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">حقيبة ميلا</strong>
        <span id="stickyBarPrice" style="font-size:13px; color:var(--zema-espresso); font-weight:800;">1,299 ج.م</span>
      </div>
    </div>
    <button class="card-quick-add-btn" style="width:auto; padding:10px 18px;" onclick="addCurrentPdpToCart()">
      <i data-lucide="shopping-bag" style="width:16px;height:16px;"></i>
      <span>أضف للسلة</span>
    </button>
  </aside>

  <!-- Footer -->
  <footer>
    <div class="footer-brand">
      <img src="__LOGO_B64__" alt="ZEMA Logo" style="height:58px; width:auto; margin-bottom: 12px;" />
      <p id="footer-desc">حقائب وإكسسوارات معاصرة وفاخرة صُممت للمرأة العصرية في مصر.</p>
    </div>
    <div class="footer-column">
      <h3>تسوقي</h3>
      <a href="#bags-section" onclick="showHomePage()">الحقائب</a>
      <a href="#wallets" onclick="showHomePage()">المحافظ</a>
      <a href="#belts" onclick="showHomePage()">الأحزمة</a>
      <a href="#accessories" onclick="showHomePage()">الإكسسوارات</a>
      <a href="#bags-section" onclick="showHomePage()">الأكثر مبيعاً</a>
    </div>
    <div class="footer-column">
      <h3>المساعدة</h3>
      <a href="#contact" onclick="toggleAccountModal(true)">تتبع شحنتك</a>
      <a href="#contact" onclick="showCartView()">سلة المشتريات</a>
      <a href="https://wa.me/201032117373" target="_blank">خدمة العملاء</a>
    </div>
    <div class="footer-column">
      <h3>تواصلي معنا</h3>
      <a href="https://wa.me/201032117373" target="_blank">واتساب: 01032117373</a>
      <a href="#contact">انستجرام</a>
      <a href="#contact">فيسبوك</a>
    </div>
    <div class="footer-bottom">
      <p>© 2026 ZEMA Luxury. All rights reserved.</p>
      <p>صُممت بكل فخر وشغف في مصر 🇪🇬</p>
    </div>
  </footer>

  <!-- ========================================================== -->
  <!-- 🛍️ 3. DEDICATED CART VIEW (EXACT PREVIOUS PROJECT) -->
  <!-- ========================================================== -->
  <section id="cartView" style="display:none;" aria-label="Shopping Cart Page">
    <div class="page-view-container">
      <div class="page-header-box">
        <p class="page-eyebrow" id="cart-header-eyebrow">YOUR CART</p>
        <h1 class="page-main-title" id="cart-header-title">حقيبة التسوق</h1>
      </div>

      <!-- Free Shipping Meter (Threshold 2,500 EGP) -->
      <div class="cart-shipping-meter" id="cartShippingMeter">
        <div id="cartShippingStatusText">🚚 تبقى لك <strong>2,500 ج.م</strong> للحصول على شحن مجاني!</div>
        <div class="meter-bar-track">
          <div class="meter-bar-fill" id="cartMeterBarFill" style="width: 0%;"></div>
        </div>
      </div>

      <!-- Cart Content (Filled dynamically) -->
      <div id="cartContentContainer">
        <!-- List or Empty State -->
      </div>
    </div>
  </section>

  <!-- ========================================================== -->
  <!-- 🇪🇬 4. DEDICATED CHECKOUT VIEW (EXACT PREVIOUS PROJECT) -->
  <!-- ========================================================== -->
  <section id="checkoutView" style="display:none;" aria-label="Checkout Page">
    <div class="co-page-wrapper">
      <div class="page-header-box">
        <p class="page-eyebrow" id="co-header-eyebrow">CHECKOUT</p>
        <h1 class="page-main-title" id="co-header-title">إتمام الطلب</h1>
      </div>

      <div class="co-card-box">
        <!-- 1. Ordered Products Summary List at Top -->
        <ul class="co-products-summary-list" id="coProductsSummaryList">
          <!-- Dynamically populated: Name × Qty ... Line Price -->
        </ul>

        <!-- 2. Totals Summary Block -->
        <div class="co-totals-block">
          <div class="co-total-row">
            <span id="co-lbl-subtotal">المجموع الفرعي:</span>
            <span id="coSubtotalVal">0 ج.م</span>
          </div>
          <div class="co-total-row discount-active" id="coDiscountRow" style="display:none;">
            <span id="coDiscountLabel">خصم (ZEMA10):</span>
            <span id="coDiscountVal">-0 ج.م</span>
          </div>
          <div class="co-total-row">
            <span id="co-lbl-shipping">الشحن:</span>
            <span id="coShippingVal">اختر المحافظة لحساب الشحن</span>
          </div>
          <div class="co-final-total-row">
            <span id="co-lbl-total">الإجمالي:</span>
            <span id="coFinalTotalVal">0 ج.م</span>
          </div>

          <!-- Promo Code Input -->
          <div class="co-promo-row">
            <input type="text" id="coCouponInput" class="co-promo-input" placeholder="كود الخصم (مثال: ZEMA10)" />
            <button type="button" class="co-promo-btn" onclick="applyCheckoutCoupon()">تطبيق</button>
          </div>
          <div id="coCouponFeedback" class="co-promo-msg" style="display:none;"></div>
        </div>

        <!-- 3. Customer Form & Payment Methods -->
        <form id="exactCheckoutForm" onsubmit="handleCheckoutFormSubmit(event)" class="co-form-area">
          <div style="margin-bottom:20px;">
            <p class="page-eyebrow" style="margin-bottom:2px;" id="co-form-eyebrow">CHECKOUT</p>
            <h3 style="font-size:18px; font-weight:800; margin:0;" id="co-form-title">اطلب الآن — الدفع عند الاستلام</h3>
          </div>

          <!-- Full Name -->
          <div class="co-form-group">
            <label id="lbl-name">الاسم بالكامل *</label>
            <input type="text" id="coName" class="co-input" placeholder="مثال: ياسمين أحمد" required minlength="3" maxlength="80" />
          </div>

          <!-- Phone Number with Live Egyptian Regex -->
          <div class="co-form-group">
            <label id="lbl-phone">رقم الهاتف (مثال: 01012345678) *</label>
            <input type="tel" id="coPhone" class="co-input" placeholder="01012345678" dir="ltr" inputmode="numeric" required oninput="validatePhoneLive()" />
            <div id="coPhoneErr" class="co-err-text" style="display:none;">رقم غير صحيح. يبدأ بـ 01 و11 رقم.</div>
          </div>

          <!-- Governorate Selection -->
          <div class="co-form-group">
            <label id="lbl-gov">المحافظة *</label>
            <select id="coGov" class="co-input" required onchange="onCheckoutGovChange()">
              <option value="">اختر محافظتك</option>
              <option value="القاهرة">القاهرة</option>
              <option value="الجيزة">الجيزة</option>
              <option value="الإسكندرية">الإسكندرية</option>
              <option value="القليوبية">القليوبية</option>
              <option value="الدقهلية">الدقهلية</option>
              <option value="الشرقية">الشرقية</option>
              <option value="الغربية">الغربية</option>
              <option value="المنوفية">المنوفية</option>
              <option value="البحيرة">البحيرة</option>
              <option value="دمياط">دمياط</option>
              <option value="كفر الشيخ">كفر الشيخ</option>
              <option value="بورسعيد">بورسعيد</option>
              <option value="الإسماعيلية">الإسماعيلية</option>
              <option value="السويس">السويس</option>
              <option value="الفيوم">الفيوم</option>
              <option value="بني سويف">بني سويف</option>
              <option value="المنيا">المنيا</option>
              <option value="أسيوط">أسيوط</option>
              <option value="سوهاج">سوهاج</option>
              <option value="قنا">قنا</option>
              <option value="الأقصر">الأقصر</option>
              <option value="أسوان">أسوان</option>
              <option value="البحر الأحمر">البحر الأحمر</option>
              <option value="الوادي الجديد">الوادي الجديد</option>
              <option value="مطروح">مرسى مطروح</option>
              <option value="شمال سيناء">شمال سيناء</option>
              <option value="جنوب سيناء">جنوب سيناء</option>
            </select>
          </div>

          <!-- City / Area (Optional) -->
          <div class="co-form-group">
            <label id="lbl-city">المدينة / المنطقة (اختياري)</label>
            <input type="text" id="coCity" class="co-input" placeholder="مثال: مدينة نصر / التجمع / سموحة" maxlength="80" />
          </div>

          <!-- Detailed Address -->
          <div class="co-form-group">
            <label id="lbl-address">العنوان بالتفصيل *</label>
            <textarea id="coAddress" class="co-input" rows="3" placeholder="اسم الشارع، رقم العقار، الشقة أو علامة مميزة" required minlength="8" maxlength="300" style="resize:vertical;"></textarea>
          </div>

          <!-- Email (Optional) -->
          <div class="co-form-group">
            <label id="lbl-email">البريد الإلكتروني (اختياري)</label>
            <input type="email" id="coEmail" class="co-input" placeholder="name@example.com" dir="ltr" />
          </div>

          <!-- Account Creation Option -->
          <div class="co-account-box">
            <label style="display:flex; align-items:center; gap:8px; font-size:12px; cursor:pointer; font-weight:700;">
              <input type="checkbox" id="coCreateAccountChk" onchange="toggleCoPasswordInput()" />
              <span id="lbl-create-acc">أنشئ حساباً لحفظ طلبي (اختياري)</span>
            </label>
            <div id="coPasswordBox" style="display:none; margin-top:8px;">
              <input type="password" id="coAccountPassword" class="co-input" placeholder="كلمة المرور (٦ أحرف على الأقل)" minlength="6" />
            </div>
            <p style="font-size:11px; color:#888; margin:4px 0 0 0;" id="lbl-guest-note">يمكنك إتمام الطلب كضيف بدون تسجيل.</p>
          </div>

          <!-- Payment Methods Fieldset -->
          <div class="co-payment-fieldset">
            <div class="co-payment-legend" id="lbl-payment-title">طريقة الدفع</div>
            
            <!-- COD: Active -->
            <label class="co-pay-option active">
              <input type="radio" name="paymentOption" value="cod" checked />
              <i data-lucide="banknote" style="width:20px;height:20px;color:#16a34a;"></i>
              <div>
                <strong style="display:block; font-size:13px;" id="lbl-pay-cod-title">الدفع عند الاستلام</strong>
                <span style="font-size:11px; color:#666;" id="lbl-pay-cod-desc">ادفع نقداً للمندوب عند وصول طلبك</span>
              </div>
            </label>

            <!-- Card: Coming soon -->
            <div class="co-pay-option disabled">
              <input type="radio" disabled />
              <i data-lucide="credit-card" style="width:20px;height:20px;color:#999;"></i>
              <span style="font-size:13px; color:#666;" id="lbl-pay-card-title">فيزا / ماستركارد</span>
              <span class="co-pay-badge-soon" id="lbl-soon-1">قريباً</span>
            </div>

            <!-- Apple Pay: Coming soon -->
            <div class="co-pay-option disabled">
              <input type="radio" disabled />
              <i data-lucide="smartphone" style="width:20px;height:20px;color:#999;"></i>
              <span style="font-size:13px; color:#666;">Apple Pay</span>
              <span class="co-pay-badge-soon" id="lbl-soon-2">قريباً</span>
            </div>

            <!-- InstaPay: Coming soon -->
            <div class="co-pay-option disabled">
              <input type="radio" disabled />
              <i data-lucide="send" style="width:20px;height:20px;color:#999;"></i>
              <span style="font-size:13px; color:#666;" id="lbl-pay-instapay-title">إنستاباي</span>
              <span class="co-pay-badge-soon" id="lbl-soon-3">قريباً</span>
            </div>

            <p style="font-size:11px; color:#888; margin-top:8px; line-height:1.4;" id="lbl-pay-note">
              الدفع عند الاستلام هو الطريقة المتاحة حالياً. باقي الطرق قيد التفعيل.
            </p>
          </div>

          <!-- Submit Order Button -->
          <button type="submit" class="btn-submit-order-final" id="btnConfirmOrderFinal">
            <span id="btnConfirmOrderText">تأكيد الطلب</span>
          </button>

          <p style="font-size:11px; color:#777; text-align:center; margin-bottom:12px;" id="lbl-co-delivery-note">
            توصيل سريع خلال ٢ - ٤ أيام عمل لجميع المحافظات
          </p>

          <p class="co-guarantee-note" id="lbl-co-guarantee-note">
            🛡️ الدفع عند الاستلام متاح — حقك في الاستبدال أو الاسترجاع مكفول خلال ١٤ يوماً.
          </p>
        </form>
      </div>
    </div>
  </section>

  <!-- ========================================================== -->
  <!-- 🌟 5. THANK YOU / ORDER CONFIRMED VIEW -->
  <!-- ========================================================== -->
  <section id="thankYouView" style="display:none;" aria-label="Thank You Page">
    <div class="ty-page-container">
      <div class="ty-check-circle">
        <i data-lucide="check" style="width:40px;height:40px;"></i>
      </div>
      <p class="page-eyebrow" id="ty-eyebrow">ORDER CONFIRMED</p>
      <h1 class="page-main-title" style="margin-bottom:12px;" id="ty-main-title">شكراً لثقتك في زِيما</h1>
      
      <div class="ty-order-box">
        <div style="font-size:11px; color:#888; text-transform:uppercase; margin-bottom:2px;" id="ty-order-no-lbl">رقم الطلب</div>
        <div style="font-size:18px; font-weight:800; color:var(--zema-espresso); font-family:monospace;" id="tyOrderNumberDisplay">#ZM260925-1001</div>
      </div>

      <p style="font-size:15px; color:#555; max-width:540px; margin:0 auto 24px auto; line-height:1.8;" id="ty-body-msg">
        تم تسجيل طلبك بنجاح! سيقوم فريق خدمة العملاء بالتواصل معك عبر الهاتف خلال ٢٤ ساعة لتأكيد تفاصيل الشحن والتسليم.
      </p>

      <div class="ty-details-card" id="tyDetailsCard">
        <div><strong id="ty-card-name">الاسم:</strong> <span id="tyCustomerName">--</span></div>
        <div><strong id="ty-card-phone">الهاتف:</strong> <span id="tyCustomerPhone">--</span></div>
        <div><strong id="ty-card-addr">العنوان:</strong> <span id="tyCustomerAddress">--</span></div>
        <div><strong id="ty-card-total">الإجمالي المطلوب عند الاستلام:</strong> <strong style="color:var(--zema-espresso);" id="tyCustomerTotal">--</strong></div>
        <div><strong id="ty-card-time">موعد التوصيل المتوقع:</strong> <span style="color:#16a34a; font-weight:700;">خلال 24 - 48 ساعة</span></div>
      </div>

      <div style="display:flex; justify-content:center; gap:12px; margin-top:28px;">
        <button class="btn-start-shopping" onclick="showHomePage()" style="margin:0; padding:14px 32px;" id="ty-btn-store">
          العودة للمتجر
        </button>
        <button class="btn-start-shopping" onclick="toggleAccountModal(true)" style="margin:0; background:#f4f2ee; color:var(--zema-espresso); border:1px solid #dcd7ce; padding:14px 28px;" id="ty-btn-track">
          تتبع شحنتك
        </button>
      </div>
    </div>
  </section>

  <!-- Wishlist Drawer -->
  <div class="modal-overlay" id="wishlistOverlay" onclick="toggleWishlistDrawer(false)"></div>
  <aside class="drawer-panel" id="wishlistDrawer">
    <div class="drawer-header">
      <h3 id="wishlist-drawer-title">قائمة المفضلة (<span id="wishlistTotalItems">0</span>)</h3>
      <button class="drawer-close-btn" onclick="toggleWishlistDrawer(false)"><i data-lucide="x"></i></button>
    </div>
    <div class="drawer-body" id="wishlistItemsContainer">
      <!-- Rendered dynamically -->
    </div>
    <div class="drawer-footer">
      <button class="card-quick-add-btn" onclick="addAllWishlistToCart()">
        <i data-lucide="shopping-bag"></i> إضافة كل المفضلة إلى السلة
      </button>
    </div>
  </aside>

  <!-- Search Modal -->
  <div class="modal-overlay" id="searchOverlay" onclick="toggleSearchModal(false)"></div>
  <div class="checkout-modal" id="searchModal" style="max-width:560px;">
    <div class="checkout-header">
      <input type="text" id="liveSearchInput" class="form-control" style="border:none; background:none; font-size:16px; font-weight:700;" placeholder="ابحثي عن حقائب، محافظ، إكسسوارات..." oninput="handleLiveSearch(this.value)" />
      <button class="drawer-close-btn" onclick="toggleSearchModal(false)"><i data-lucide="x"></i></button>
    </div>
    <div style="padding:16px 20px; max-height:360px; overflow-y:auto;" id="searchResultsList">
      <p style="font-size:12px; color:#888;">الأكثر بحثاً: <span style="cursor:pointer; color:#000; text-decoration:underline;" onclick="searchFor('ميلا')">ميلا</span> · <span style="cursor:pointer; color:#000; text-decoration:underline;" onclick="searchFor('نور')">نور</span> · <span style="cursor:pointer; color:#000; text-decoration:underline;" onclick="searchFor('توت')">توت</span></p>
      <div id="liveMatchesContainer" style="margin-top:12px;"></div>
    </div>
  </div>

  <!-- Account Modal -->
  <div class="modal-overlay" id="accountOverlay" onclick="toggleAccountModal(false)"></div>
  <div class="checkout-modal" id="accountModal" style="max-width:480px;">
    <div class="checkout-header">
      <h3>👤 حسابي ومتابعة الطلب</h3>
      <button class="drawer-close-btn" onclick="toggleAccountModal(false)"><i data-lucide="x"></i></button>
    </div>
    <div class="checkout-body">
      <div style="margin-bottom:14px;">
        <label style="font-size:13px; font-weight:700; display:block; margin-bottom:6px;">تتبع مسار شحنتك:</label>
        <div style="display:flex; gap:8px;">
          <input type="text" id="accTrackInput" class="form-control" placeholder="رقم الهاتف أو كود الطلب ZM-..." />
          <button class="card-quick-add-btn" style="width:auto; padding:10px 18px;" onclick="trackCustomerOrder()">تتبع</button>
        </div>
      </div>
      <div id="accTrackResult" style="display:none; background:#f4f9f4; border:1px solid #86efac; border-radius:8px; padding:14px; font-size:13px;">
        <strong style="color:#16a34a; display:block; margin-bottom:4px;">✓ الشحنة مع مندوب التوصيل الآن</strong>
        <span>التسليم المتوقع خلال 24 ساعة إلى عنوانك.</span>
      </div>
    </div>
  </div>

  <!-- Master Interactive Engine -->
  <script>
    // Products Master Catalog with 4 Angles Each
    const CATALOG = [
      {
        id: 'p1',
        nameAr: 'حقيبة ميلا هوبو ناعمة',
        nameEn: 'Mila Soft Hobo Bag',
        catAr: 'حقيبة كتف',
        catEn: 'Shoulder Bag',
        price: 1299,
        originalPrice: 1699,
        angles: ['__HOBO_B64__', '__BAG_QUILTED_B64__', '__BAG_CROSSBODY_B64__', '__HERO_B64__'],
        descAr: 'حقيبة كتف عصرية بتصميم هوبو انسيابي يفيض بالأنوثة والهدوء. تتسع لأغراضك اليومية بحرية كاملة مع سحاب أمان وحزام كتف مريح.',
        descEn: 'A modern shoulder bag with a fluid hobo silhouette that exudes quiet luxury. Spacious interior with secure zipper and comfortable shoulder strap.',
        materialsAr: '100% جلد طبيعي مع بطانة مخملية وإكسسوارات مطلية بالذهب مقاومة للخدش.',
        materialsEn: '100% genuine full-grain leather with plush velvet lining and scratch-resistant gold-tone hardware.',
        dimAr: 'العرض: 34 سم | الارتفاع: 26 سم | العمق: 12 سم | حزام الكتف: 52 سم',
        dimEn: 'Width: 34 cm | Height: 26 cm | Depth: 12 cm | Shoulder Strap: 52 cm'
      },
      {
        id: 'p2',
        nameAr: 'حقيبة نور كتف منحنية',
        nameEn: 'Noor Curved Shoulder Bag',
        catAr: 'حقيبة كتف',
        catEn: 'Shoulder Bag',
        price: 1150,
        originalPrice: 1450,
        angles: ['__BURGUNDY_B64__', '__BAG_BURGUNDY_B64__', '__BAG_CROSSBODY_B64__', '__HOBO_B64__'],
        descAr: 'تصميم مقوس مميز باللون البورجوندي الملكي يمنح إطلالتك سحراً لافتاً. مثالية للأمسيات والمناسبات والعمل الراقي.',
        descEn: 'Distinctive curved design in regal burgundy that adds undeniable sophistication to your look. Perfect for evenings and refined workdays.',
        materialsAr: 'جلد طبيعي مرن مع لمسات معدنية ذهبية وقفل مغناطيسي متين.',
        materialsEn: 'Supple genuine leather with gold-finished hardware and secure magnetic closure.',
        dimAr: 'العرض: 28 سم | الارتفاع: 20 سم | العمق: 8 سم | حزام الكتف: 48 سم',
        dimEn: 'Width: 28 cm | Height: 20 cm | Depth: 8 cm | Shoulder Strap: 48 cm'
      },
      {
        id: 'p3',
        nameAr: 'حقيبة لينا توت منظمة',
        nameEn: 'Lina Structured Tote Bag',
        catAr: 'حقيبة توت',
        catEn: 'Tote Bag',
        price: 1499,
        originalPrice: null,
        angles: ['__OLIVE_B64__', '__BAG_CAMEL_B64__', '__BAG_QUILTED_B64__', '__HERO_B64__'],
        descAr: 'حقيبة توت رحبة ومنظمة بعناية تتسع للكمبيوتر المحمول والملفات مع جيوب مخصصة للهاتف والمحفظة بلون زيتوني فاخر.',
        descEn: 'A spacious and structured tote that effortlessly accommodates your laptop and essentials with dedicated compartments in a rich olive tone.',
        materialsAr: 'جلد طبيعي صلب يحتفظ بهيكله المميز مع يدين مزدوجتين متينتين.',
        materialsEn: 'Structured genuine leather that retains its shape with reinforced double carry handles.',
        dimAr: 'العرض: 38 سم | الارتفاع: 30 سم | العمق: 14 سم',
        dimEn: 'Width: 38 cm | Height: 30 cm | Depth: 14 cm'
      },
      {
        id: 'p4',
        nameAr: 'حقيبة آية توت يومية',
        nameEn: 'Aya Everyday Tote Bag',
        catAr: 'حقيبة توت',
        catEn: 'Tote Bag',
        price: 1399,
        originalPrice: 1799,
        angles: ['__HERO_B64__', '__BAG_CAMEL_B64__', '__BAG_QUILTED_B64__', '__OLIVE_B64__'],
        descAr: 'رفيقة كل يوم المصممة لتلائم وتيرة حياتك السريعة بأناقة لا تخبو. خفيفة وعملية ومصممة لتحمل الاستخدام اليومي.',
        descEn: 'Your everyday companion crafted to match your dynamic lifestyle with timeless elegance. Lightweight, functional, and durable.',
        materialsAr: 'جلد طبيعي ناعم مع معالجة واقية من البقع والرطوبة.',
        materialsEn: 'Soft full-grain leather treated with protective coating against stains and moisture.',
        dimAr: 'العرض: 36 سم | الارتفاع: 28 سم | العمق: 13 سم',
        dimEn: 'Width: 36 cm | Height: 28 cm | Depth: 13 cm'
      }
    ];

    // State Variables
    let currentLang = 'ar';
    let cart = JSON.parse(localStorage.getItem('zema_cart') || '[]');
    let wishlist = JSON.parse(localStorage.getItem('zema_wishlist') || '[]');
    let activePdpProduct = CATALOG[0];
    let pdpSelectedQty = 1;

    // Carousel
    let currentSlide = 0;
    const slides = [document.getElementById('hero-slide-1'), document.getElementById('hero-slide-2'), document.getElementById('hero-slide-3')];
    function showSlide(idx) {
      slides.forEach((s, i) => {
        s.style.display = i === idx ? 'block' : 'none';
        s.classList.toggle('is-active', i === idx);
      });
      currentSlide = idx;
    }
    function nextSlide() { showSlide((currentSlide + 1) % slides.length); }
    function prevSlide() { showSlide((currentSlide - 1 + slides.length) % slides.length); }
    setInterval(nextSlide, 5000);

    // ==========================================
    // 📄 2. PDP LOGIC & NAVIGATION
    // ==========================================
    function openPDP(productId) {
      const prod = CATALOG.find(p => p.id === productId) || CATALOG[0];
      activePdpProduct = prod;
      pdpSelectedQty = 1;

      // Update URL hash without reload
      window.location.hash = 'product-' + prod.id;
      document.body.classList.add('is-pdp');

      // Hide Home, Show PDP
      document.getElementById('home-view').style.display = 'none';
      document.getElementById('pdp-view').style.display = 'block';

      // Update Texts
      const isAr = currentLang === 'ar';
      document.getElementById('pdp-crumb-title').textContent = isAr ? prod.nameAr : prod.nameEn;
      document.getElementById('pdp-crumb-cat').textContent = isAr ? prod.catAr : prod.catEn;
      document.getElementById('pdpTitle').textContent = isAr ? prod.nameAr : prod.nameEn;
      document.getElementById('pdpPrice').textContent = prod.price.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      
      if (prod.originalPrice) {
        document.getElementById('pdpOldPrice').style.display = 'inline';
        document.getElementById('pdpOldPrice').textContent = prod.originalPrice.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
        document.getElementById('pdpSavingBadge').style.display = 'inline';
        document.getElementById('pdpSavingBadge').textContent = (isAr ? 'توفير ' : 'Save ') + (prod.originalPrice - prod.price) + (isAr ? ' ج.م' : ' EGP');
      } else {
        document.getElementById('pdpOldPrice').style.display = 'none';
        document.getElementById('pdpSavingBadge').style.display = 'none';
      }

      document.getElementById('pdpDescContent').innerHTML = isAr ? prod.descAr : prod.descEn;
      document.getElementById('pdpMaterialsContent').innerHTML = isAr ? prod.materialsAr : prod.materialsEn;
      document.getElementById('pdpDimensionsContent').innerHTML = isAr ? prod.dimAr : prod.dimEn;

      // Update Gallery
      document.getElementById('pdpMainImage').src = prod.angles[0];
      const thumbsContainer = document.getElementById('pdpThumbnailsContainer');
      thumbsContainer.innerHTML = '';
      prod.angles.forEach((imgSrc, idx) => {
        const btn = document.createElement('button');
        btn.className = 'pdp-thumb-btn' + (idx === 0 ? ' active' : '');
        btn.innerHTML = `<img src="${imgSrc}" alt="Angle ${idx+1}" />`;
        btn.onclick = () => {
          document.querySelectorAll('.pdp-thumb-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          document.getElementById('pdpMainImage').src = imgSrc;
        };
        thumbsContainer.appendChild(btn);
      });

      // Update Mobile Sticky Bar
      document.getElementById('stickyBarImg').src = prod.angles[0];
      document.getElementById('stickyBarTitle').textContent = isAr ? prod.nameAr : prod.nameEn;
      document.getElementById('stickyBarPrice').textContent = prod.price.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      // Update Direct WhatsApp PDP Order Link
      const waMsg = (isAr ? 'مرحباً ZEMA، أرغب في طلب: ' : 'Hello ZEMA, I want to order: ') + (isAr ? prod.nameAr : prod.nameEn) + ' (' + prod.price + ' EGP)';
      document.getElementById('pdpWaOrderBtn').href = 'https://wa.me/201032117373?text=' + encodeURIComponent(waMsg);

      // Scroll smoothly to top of PDP
      window.scrollTo({ top: 0, behavior: 'smooth' });
      lucide.createIcons();
    }

    function showHomePage() {
      window.location.hash = '';
      document.body.classList.remove('is-pdp');
      document.getElementById('pdp-view').style.display = 'none';
      document.getElementById('home-view').style.display = 'block';
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function changePdpQty(delta) {
      pdpSelectedQty = Math.max(1, pdpSelectedQty + delta);
      document.getElementById('pdpQtyNumber').textContent = pdpSelectedQty;
    }

    function addCurrentPdpToCart() {
      addToCart(activePdpProduct.id, pdpSelectedQty);
    }

    function togglePdpAccordion(btn) {
      const content = btn.nextElementSibling;
      const isOpen = content.classList.contains('open');
      content.classList.toggle('open', !isOpen);
      const icon = btn.querySelector('svg');
      if (icon) {
        icon.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
      }
    }

            // ==========================================
    // 🛍️ 3. EXACT PREVIOUS PROJECT CART & CHECKOUT
    // ==========================================
    let activePromo = null; // { code: 'ZEMA10', rate: 0.1 }

    function showCartView() {
      document.getElementById('homeMain').style.display = 'none';
      document.getElementById('pdpView').style.display = 'none';
      document.getElementById('checkoutView').style.display = 'none';
      document.getElementById('thankYouView').style.display = 'none';
      
      const cartView = document.getElementById('cartView');
      cartView.style.display = 'block';
      window.scrollTo(0, 0);
      window.location.hash = 'cart';
      renderCartView();
    }

    function showCheckoutView() {
      if (cart.length === 0) {
        showCartView();
        return;
      }
      document.getElementById('homeMain').style.display = 'none';
      document.getElementById('pdpView').style.display = 'none';
      document.getElementById('cartView').style.display = 'none';
      document.getElementById('thankYouView').style.display = 'none';

      const checkoutView = document.getElementById('checkoutView');
      checkoutView.style.display = 'block';
      window.scrollTo(0, 0);
      window.location.hash = 'checkout';
      renderCheckoutView();
    }

    function showThankYouView(orderData) {
      document.getElementById('homeMain').style.display = 'none';
      document.getElementById('pdpView').style.display = 'none';
      document.getElementById('cartView').style.display = 'none';
      document.getElementById('checkoutView').style.display = 'none';

      const tyView = document.getElementById('thankYouView');
      tyView.style.display = 'block';
      window.scrollTo(0, 0);
      window.location.hash = 'thank-you';

      if (orderData) {
        document.getElementById('tyOrderNumberDisplay').textContent = '#' + orderData.order_number;
        document.getElementById('tyCustomerName').textContent = orderData.customer_name;
        document.getElementById('tyCustomerPhone').textContent = orderData.customer_phone;
        document.getElementById('tyCustomerAddress').textContent = orderData.governorate + (orderData.city ? ' - ' + orderData.city : '') + ' - ' + orderData.address;
        document.getElementById('tyCustomerTotal').textContent = orderData.total.toLocaleString() + (currentLang === 'ar' ? ' ج.م' : ' EGP');
      }
      lucide.createIcons();
    }

    function showHomePage() {
      document.getElementById('cartView').style.display = 'none';
      document.getElementById('checkoutView').style.display = 'none';
      document.getElementById('thankYouView').style.display = 'none';
      document.getElementById('pdpView').style.display = 'none';
      document.getElementById('homeMain').style.display = 'block';
      window.location.hash = '';
      window.scrollTo(0, 0);
    }

    function addToCart(productId, qty = 1) {
      const prod = CATALOG.find(p => p.id === productId);
      if (!prod) return;

      const existing = cart.find(i => i.id === productId);
      if (existing) {
        existing.qty += qty;
      } else {
        cart.push({
          id: prod.id,
          sku: prod.sku || ('ZM-' + prod.id.toUpperCase()),
          nameAr: prod.nameAr,
          nameEn: prod.nameEn,
          price: prod.price,
          img: prod.angles[0],
          qty: qty
        });
      }
      saveCart();
      updateCartBadge();
      showCartView();
    }

    function changeCartItemQty(id, delta) {
      const item = cart.find(i => i.id === id);
      if (!item) return;
      item.qty += delta;
      if (item.qty <= 0) {
        cart = cart.filter(i => i.id !== id);
      }
      saveCart();
      updateCartBadge();
      renderCartView();
    }

    function saveCart() {
      localStorage.setItem('zema_cart', JSON.stringify(cart));
    }

    function updateCartBadge() {
      const countBadge = document.getElementById('cartCountBadge');
      const totalItems = cart.reduce((sum, i) => sum + i.qty, 0);
      if (countBadge) countBadge.textContent = totalItems;
    }

    function renderCartView() {
      updateCartBadge();
      const container = document.getElementById('cartContentContainer');
      const isAr = currentLang === 'ar';
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const threshold = 2500;
      const progress = Math.min(100, Math.round((subtotal / threshold) * 100));

      // Shipping Meter Fill
      const meterFill = document.getElementById('cartMeterBarFill');
      const meterText = document.getElementById('cartShippingStatusText');
      meterFill.style.width = progress + '%';
      if (subtotal >= threshold) {
        meterText.innerHTML = '🎉 <strong>' + (isAr ? 'مبروك! حصلت على شحن مجاني لكافة المحافظات!' : "Congrats! You've unlocked free shipping!") + '</strong>';
        meterFill.style.background = '#1b7d3f';
      } else {
        const remaining = threshold - subtotal;
        meterText.innerHTML = '🚚 ' + (isAr ? 'أضف منتجات بقيمة <strong>' + remaining.toLocaleString() + ' ج.م</strong> للحصول على شحن مجاني!' : 'Add products worth <strong>' + remaining.toLocaleString() + ' EGP</strong> more for free shipping!');
        meterFill.style.background = '#C5A059';
      }

      if (cart.length === 0) {
        container.innerHTML = `
          <div class="cart-empty-view">
            <i data-lucide="shopping-bag" style="width:52px;height:52px;margin:0 auto 16px auto; opacity:0.35;"></i>
            <h3 style="font-size:18px; margin:0 0 8px 0;">${isAr ? 'سلتك فارغة حالياً.' : 'Your cart is empty.'}</h3>
            <p style="color:#777; font-size:14px; margin:0 0 16px 0;">${isAr ? 'استكشف تشكيلاتنا الفاخرة واختر ما يناسب أناقتك' : 'Explore our luxury collections'}</p>
            <button class="btn-start-shopping" onclick="showHomePage()">
              ${isAr ? 'ابدأ التسوق' : 'Start Shopping'}
            </button>
          </div>
        `;
      } else {
        let html = '<div class="cart-items-table">';
        cart.forEach(item => {
          const title = isAr ? item.nameAr : item.nameEn;
          const lineTotal = item.price * item.qty;
          html += `
            <div class="cart-row">
              <img src="${item.img}" class="cart-img-thumb" alt="${title}" />
              <div class="cart-item-details">
                <h4 class="cart-item-heading">${title}</h4>
                <div class="cart-sku-badge">${item.sku}</div>
                <div class="cart-item-price-val">${lineTotal.toLocaleString()} ${isAr ? 'ج.م' : 'EGP'}</div>
                <div class="cart-actions-row">
                  <div class="cart-qty-control">
                    <button class="cart-qty-btn" onclick="changeCartItemQty('${item.id}', -1)" aria-label="-">−</button>
                    <span class="cart-qty-display">${item.qty}</span>
                    <button class="cart-qty-btn" onclick="changeCartItemQty('${item.id}', 1)" aria-label="+">+</button>
                  </div>
                  <button class="cart-remove-link" onclick="changeCartItemQty('${item.id}', -999)">
                    <i data-lucide="trash-2" style="width:14px;height:14px;"></i>
                    <span>${isAr ? 'حذف' : 'Remove'}</span>
                  </button>
                </div>
              </div>
            </div>
          `;
        });
        html += '</div>';

        html += `
          <div class="cart-bottom-bar">
            <div class="cart-subtotal-text">
              <span>${isAr ? 'المجموع الفرعي:' : 'Subtotal:'} </span>
              <span class="cart-subtotal-val">${subtotal.toLocaleString()} ${isAr ? 'ج.م' : 'EGP'}</span>
            </div>
            <button class="btn-proceed-co" onclick="showCheckoutView()">
              ${isAr ? 'إتمام الطلب' : 'Proceed to checkout'}
            </button>
          </div>
        `;
        container.innerHTML = html;
      }
      lucide.createIcons();
    }

    // ==========================================
    // 🇪🇬 CHECKOUT LOGIC & CALCULATIONS
    // ==========================================
    function calculateShipping(subtotal, gov) {
      if (subtotal >= 2500) return 0;
      if (!gov) return null;
      if (gov === 'القاهرة' || gov === 'الجيزة') return 50;
      return 65;
    }

    function renderCheckoutView() {
      const isAr = currentLang === 'ar';
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const gov = document.getElementById('coGov').value;
      const shipping = calculateShipping(subtotal, gov);

      // 1. Render Ordered Items Summary List
      const summaryList = document.getElementById('coProductsSummaryList');
      let itemsHtml = '';
      cart.forEach(item => {
        const title = isAr ? item.nameAr : item.nameEn;
        const lineTotal = item.price * item.qty;
        itemsHtml += `
          <li class="co-prod-item-line">
            <div class="co-prod-name-qty">
              <span>${title}</span>
              <span class="co-prod-qty-badge">× ${item.qty}</span>
            </div>
            <span class="co-prod-price-badge">${lineTotal.toLocaleString()} ${isAr ? 'ج.م' : 'EGP'}</span>
          </li>
        `;
      });
      summaryList.innerHTML = itemsHtml;

      // 2. Calculations
      let discountAmount = 0;
      if (activePromo) {
        discountAmount = Math.round(subtotal * activePromo.rate);
      }

      document.getElementById('coSubtotalVal').textContent = subtotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      const discRow = document.getElementById('coDiscountRow');
      if (discountAmount > 0) {
        discRow.style.display = 'flex';
        document.getElementById('coDiscountLabel').textContent = (isAr ? 'خصم ' : 'Discount ') + `(${activePromo.code}):`;
        document.getElementById('coDiscountVal').textContent = '- ' + discountAmount.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      } else {
        discRow.style.display = 'none';
      }

      const shippingEl = document.getElementById('coShippingVal');
      if (shipping === 0) {
        shippingEl.innerHTML = '<span style="color:#16a34a; font-weight:bold;">' + (isAr ? 'مجاني 🎉' : 'Free 🎉') + '</span>';
      } else if (shipping !== null) {
        shippingEl.textContent = shipping + (isAr ? ' ج.م' : ' EGP');
      } else {
        shippingEl.textContent = isAr ? 'اختر المحافظة لحساب الشحن' : 'Select governorate to calculate shipping';
      }

      const activeShipping = shipping !== null ? shipping : 0;
      const finalTotal = Math.max(0, subtotal - discountAmount + activeShipping);
      document.getElementById('coFinalTotalVal').textContent = finalTotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      document.getElementById('btnConfirmOrderText').textContent = (isAr ? 'تأكيد الطلب — ' : 'Confirm Order — ') + finalTotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
    }

    function onCheckoutGovChange() {
      renderCheckoutView();
    }

    function validatePhoneLive() {
      const phoneInput = document.getElementById('coPhone');
      const errBox = document.getElementById('coPhoneErr');
      const cleanPhone = phoneInput.value.replace(/\\D/g, '');
      phoneInput.value = cleanPhone;

      const isEgyptian = /^01[0125][0-9]{8}$/.test(cleanPhone);
      if (cleanPhone.length > 0 && !isEgyptian) {
        phoneInput.classList.add('input-error');
        errBox.style.display = 'block';
        return false;
      } else {
        phoneInput.classList.remove('input-error');
        errBox.style.display = 'none';
        return isEgyptian;
      }
    }

    function applyCheckoutCoupon() {
      const input = document.getElementById('coCouponInput');
      const feedback = document.getElementById('coCouponFeedback');
      const phone = document.getElementById('coPhone').value.trim();
      const code = input.value.trim().toUpperCase();
      const isAr = currentLang === 'ar';

      if (!code) return;

      if (!phone) {
        feedback.className = 'co-promo-msg err';
        feedback.textContent = isAr ? 'أدخل رقم هاتفك أولاً للتحقق من أهلية الخصم' : 'Enter your phone first to verify code eligibility';
        feedback.style.display = 'block';
        return;
      }

      if (code === 'ZEMA10') {
        activePromo = { code: 'ZEMA10', rate: 0.1 };
        feedback.className = 'co-promo-msg ok';
        feedback.textContent = isAr ? '✓ تم تطبيق خصم 10%' : '✓ Applied 10% discount';
        feedback.style.display = 'block';
        renderCheckoutView();
      } else {
        activePromo = null;
        feedback.className = 'co-promo-msg err';
        feedback.textContent = isAr ? 'كود الخصم غير صالح' : 'Invalid discount code';
        feedback.style.display = 'block';
        renderCheckoutView();
      }
    }

    function toggleCoPasswordInput() {
      const chk = document.getElementById('coCreateAccountChk');
      const box = document.getElementById('coPasswordBox');
      box.style.display = chk.checked ? 'block' : 'none';
    }

    function handleCheckoutFormSubmit(e) {
      e.preventDefault();
      const isAr = currentLang === 'ar';
      const name = document.getElementById('coName').value.trim();
      const phone = document.getElementById('coPhone').value.trim();
      const gov = document.getElementById('coGov').value;
      const city = document.getElementById('coCity').value.trim();
      const address = document.getElementById('coAddress').value.trim();
      const email = document.getElementById('coEmail').value.trim();

      if (!validatePhoneLive() && phone.length !== 11) {
        alert(isAr ? 'رقم الهاتف غير صحيح. يجب أن يبدأ بـ 01 ويتكوّن من 11 رقماً.' : 'Invalid phone. Must start with 01 and be 11 digits.');
        return;
      }

      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const shipping = calculateShipping(subtotal, gov) || 0;
      let discountAmount = 0;
      if (activePromo) discountAmount = Math.round(subtotal * activePromo.rate);
      const totalAmount = Math.max(0, subtotal - discountAmount + shipping);

      // Generate exact Order Number format: ZM + YYMMDD + '-' + 4 digits
      const now = new Date();
      const yy = String(now.getFullYear()).slice(-2);
      const mm = String(now.getMonth() + 1).padStart(2, '0');
      const dd = String(now.getDate()).padStart(2, '0');
      const random4 = Math.floor(1000 + Math.random() * 9000);
      const orderNumber = `ZM${yy}${mm}${dd}-${random4}`;

      const orderData = {
        order_number: orderNumber,
        customer_name: name,
        customer_phone: phone,
        customer_email: email,
        governorate: gov,
        city: city,
        address: address,
        items: cart,
        subtotal: subtotal,
        discount: discountAmount,
        shipping: shipping,
        total: totalAmount,
        payment_method: 'Cash on Delivery',
        created_at: new Date().toISOString()
      };

      // Save to localStorage
      try {
        const storedOrders = JSON.parse(localStorage.getItem('zema_orders') || '[]');
        storedOrders.unshift(orderData);
        localStorage.setItem('zema_orders', JSON.stringify(storedOrders));
      } catch (err) {
        console.warn('Could not save order locally:', err);
      }

      // Clear cart
      cart = [];
      saveCart();
      updateCartBadge();

      // Show Thank You Page View
      showThankYouView(orderData);
    }

    // Hash router handler
    window.addEventListener('hashchange', () => {
      const h = window.location.hash;
      if (h === '#cart') {
        showCartView();
      } else if (h === '#checkout') {
        showCheckoutView();
      } else if (h === '#thank-you') {
        showThankYouView();
      } else if (h.startsWith('#product-')) {
        const id = h.replace('#product-', '');
        showPDP(id);
      } else if (!h || h === '#' || h === '#story' || h === '#contact' || h === '#faq') {
        if (!h || h === '#') showHomePage();
      }
    });

    // Check initial hash on load
    window.addEventListener('DOMContentLoaded', () => {
      const h = window.location.hash;
      if (h === '#cart') showCartView();
      else if (h === '#checkout') showCheckoutView();
      else if (h === '#thank-you') showThankYouView();
      else if (h.startsWith('#product-')) showPDP(h.replace('#product-', ''));
      updateCartBadge();
    });

    // ==========================================
    // ❤️ 5. WISHLIST & SEARCH ENGINE
    // ==========================================
    function toggleWishlistDrawer(open) {
      const overlay = document.getElementById('wishlistOverlay');
      const drawer = document.getElementById('wishlistDrawer');
      if (open) {
        overlay.classList.add('open');
        drawer.classList.add('open');
        renderWishlistUI();
      } else {
        overlay.classList.remove('open');
        drawer.classList.remove('open');
      }
    }

    function toggleWishlistItem(id, btn) {
      const idx = wishlist.indexOf(id);
      if (idx !== -1) {
        wishlist.splice(idx, 1);
        if (btn) btn.classList.remove('active');
      } else {
        wishlist.push(id);
        if (btn) btn.classList.add('active');
      }
      localStorage.setItem('zema_wishlist', JSON.stringify(wishlist));
      updateWishlistBadge();
    }

    function updateWishlistBadge() {
      const count = wishlist.length;
      document.getElementById('wishlistCountBadge').textContent = count;
      document.getElementById('wishlistTotalItems').textContent = count;
      CATALOG.forEach(p => {
        const btn = document.getElementById('fav-btn-' + p.id);
        if (btn) btn.classList.toggle('active', wishlist.includes(p.id));
      });
    }

    function renderWishlistUI() {
      const container = document.getElementById('wishlistItemsContainer');
      const isAr = currentLang === 'ar';
      if (wishlist.length === 0) {
        container.innerHTML = `
          <div style="text-align:center; padding: 45px 10px; color:#888;">
            <i data-lucide="heart" style="width:48px;height:48px;margin: 0 auto 12px auto; opacity:0.3;"></i>
            <p>${isAr ? 'قائمة المفضلة فارغة حالياً' : 'Your wishlist is empty'}</p>
          </div>
        `;
      } else {
        let html = '';
        wishlist.forEach(id => {
          const item = CATALOG.find(p => p.id === id);
          if (!item) return;
          const title = isAr ? item.nameAr : item.nameEn;
          html += `
            <div class="cart-item-row">
              <img src="${item.angles[0]}" class="cart-item-img" alt="${title}" />
              <div class="cart-item-info">
                <div>
                  <h4 class="cart-item-title">${title}</h4>
                  <div class="cart-item-price">${item.price.toLocaleString()} ${isAr ? 'ج.م' : 'EGP'}</div>
                </div>
                <div style="display:flex; gap:8px; margin-top:8px;">
                  <button class="card-quick-add-btn" style="padding:6px 12px; font-size:12px;" onclick="addToCart('${item.id}', 1)">
                    + ${isAr ? 'أضف للسلة' : 'Add'}
                  </button>
                  <button onclick="toggleWishlistItem('${item.id}', null); renderWishlistUI();" style="background:none; border:none; cursor:pointer; color:#dc2626;">
                    <i data-lucide="trash-2" style="width:16px;height:16px;"></i>
                  </button>
                </div>
              </div>
            </div>
          `;
        });
        container.innerHTML = html;
      }
      lucide.createIcons();
    }

    function addAllWishlistToCart() {
      wishlist.forEach(id => addToCart(id, 1));
      toggleWishlistDrawer(false);
      showCartView();
    }

    // Search Engine
    function toggleSearchModal(open) {
      const overlay = document.getElementById('searchOverlay');
      const modal = document.getElementById('searchModal');
      if (open) {
        overlay.classList.add('open');
        modal.classList.add('open');
        const inp = document.getElementById('liveSearchInput');
        inp.value = '';
        inp.focus();
        handleLiveSearch('');
      } else {
        overlay.classList.remove('open');
        modal.classList.remove('open');
      }
    }

    function searchFor(term) {
      document.getElementById('liveSearchInput').value = term;
      handleLiveSearch(term);
    }

    function handleLiveSearch(query) {
      const q = query.trim().toLowerCase();
      const container = document.getElementById('liveMatchesContainer');
      if (!q) {
        container.innerHTML = '';
        return;
      }
      const matches = CATALOG.filter(p => 
        p.nameAr.toLowerCase().includes(q) || 
        p.nameEn.toLowerCase().includes(q) ||
        p.catAr.toLowerCase().includes(q)
      );

      if (matches.length === 0) {
        container.innerHTML = `<p style="font-size:13px; color:#888; text-align:center; padding:15px;">لا توجد نتائج مطابقة لـ "${query}"</p>`;
      } else {
        let html = '';
        matches.forEach(item => {
          const title = currentLang === 'ar' ? item.nameAr : item.nameEn;
          html += `
            <div style="display:flex; align-items:center; gap:12px; padding:10px 0; border-bottom:1px solid #f2efe9; cursor:pointer;" onclick="openPDP('${item.id}'); toggleSearchModal(false);">
              <img src="${item.angles[0]}" style="width:48px;height:58px;object-fit:cover;border-radius:4px;" />
              <div style="flex:1;">
                <strong style="font-size:14px; display:block;">${title}</strong>
                <span style="font-size:12px; color:#666;">${item.price.toLocaleString()} ${currentLang === 'ar' ? 'ج.م' : 'EGP'}</span>
              </div>
              <button class="card-quick-add-btn" style="width:auto; padding:6px 12px; font-size:12px;" onclick="event.stopPropagation(); addToCart('${item.id}', 1); toggleSearchModal(false);">
                + أضف للسلة
              </button>
            </div>
          `;
        });
        container.innerHTML = html;
      }
    }

    // Account Modal
    function toggleAccountModal(open) {
      const overlay = document.getElementById('accountOverlay');
      const modal = document.getElementById('accountModal');
      if (open) {
        overlay.classList.add('open');
        modal.classList.add('open');
      } else {
        overlay.classList.remove('open');
        modal.classList.remove('open');
      }
    }

    function trackCustomerOrder() {
      const val = document.getElementById('accTrackInput').value.trim();
      const res = document.getElementById('accTrackResult');
      if (val) {
        res.style.display = 'block';
      }
    }

    // ==========================================
    // 🌐 6. MULTILINGUAL SWITCHER
    // ==========================================
    function toggleLanguage() {
      currentLang = currentLang === 'ar' ? 'en' : 'ar';
      const isAr = currentLang === 'ar';
      
      document.documentElement.setAttribute('dir', isAr ? 'rtl' : 'ltr');
      document.documentElement.setAttribute('lang', currentLang);

      document.getElementById('currentLangLabel').textContent = isAr ? 'English' : 'العربية';
      document.getElementById('ticker-msg-1').textContent = isAr ? 'شحن مجاني لكافة محافظات مصر للطلبات فوق 2,500 ج.م' : 'FREE SHIPPING OVER EGP 2,500 ACROSS EGYPT';
      document.getElementById('ticker-msg-2').textContent = isAr ? 'توصيل سريع لباب بيتك خلال 24 - 48 ساعة' : 'FAST EXPRESS DELIVERY TO YOUR DOORSTEP (24-48H)';
      document.getElementById('ticker-msg-3').textContent = isAr ? 'حق معاينة وفحص الشحنة قبل الاستلام والدفع' : 'INSPECT BEFORE PAYING — 100% PEACE OF MIND';
      document.getElementById('ticker-msg-4').textContent = isAr ? 'جلد طبيعي فاخر 100% بضمان زيما الرسمي' : '100% GENUINE LUXURY LEATHER GUARANTEE';

      document.getElementById('nav-our-story').textContent = isAr ? 'قصتنا' : 'Our Story';
      document.getElementById('nav-home').textContent = isAr ? 'الرئيسية' : 'Home';
      document.getElementById('nav-wallets').textContent = isAr ? 'محافظ' : 'Wallets';
      document.getElementById('nav-belts').textContent = isAr ? 'أحزمة' : 'Belts';
      document.getElementById('nav-accessories').textContent = isAr ? 'إكسسوارات' : 'Accessories';
      document.getElementById('nav-bestsellers').textContent = isAr ? 'الأكثر مبيعاً' : 'Best Sellers';
      document.getElementById('nav-sale').textContent = isAr ? 'تخفيضات' : 'Sale';

      document.querySelectorAll('.btn-text-qa').forEach(el => el.textContent = isAr ? 'إضافة سريعة للسلة' : 'Quick Add');
      
      updateCartUI();
      renderWishlistUI();
      if (document.body.classList.contains('is-pdp')) {
        openPDP(activePdpProduct.id);
      }
      lucide.createIcons();
    }

    // Hashchange listener (Support Browser Back/Forward buttons)
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash;
      if (hash.startsWith('#product-')) {
        const id = hash.replace('#product-', '');
        openPDP(id);
      } else {
        showHomePage();
      }
    });

    // Check initial hash on page load
    if (window.location.hash.startsWith('#product-')) {
      const id = window.location.hash.replace('#product-', '');
      openPDP(id);
    }

    // Init
    updateCartUI();
    updateWishlistBadge();
    lucide.createIcons();
  </script>
</body>
</html>
'''

final_html = template.replace('__CSS_CONTENT__', css_content)
final_html = final_html.replace('__LOGO_B64__', logo_b64)
final_html = final_html.replace('__HERO_B64__', hero_b64)
final_html = final_html.replace('__BURGUNDY_B64__', burgundy_b64)
final_html = final_html.replace('__OLIVE_B64__', olive_b64)
final_html = final_html.replace('__HOBO_B64__', hobo_b64)
final_html = final_html.replace('__BAG_BURGUNDY_B64__', bag_burgundy_b64)
final_html = final_html.replace('__BAG_CAMEL_B64__', bag_camel_b64)
final_html = final_html.replace('__BAG_CROSSBODY_B64__', bag_crossbody_b64)
final_html = final_html.replace('__BAG_QUILTED_B64__', bag_quilted_b64)

# 1. Write to E:\lovable\template.html (for Extension)
with open(r'E:\lovable\template.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print('Wrote E:\\lovable\\template.html, size:', len(final_html))

# 2. Write to C:\Users\User\.gemini\antigravity\scratch\zema-luxury\index.html (for GitHub & Lovable)
with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(final_html)
print('Wrote index.html, size:', len(final_html))
