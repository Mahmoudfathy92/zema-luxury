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
    transition: background-color 0.2s ease, transform 0.15s ease, color 0.2s ease;
  }
  .icon-btn svg {
    width: 20px;
    height: 20px;
    stroke: currentColor;
    stroke-width: 1.7;
    fill: none;
    display: block;
    pointer-events: none;
    flex-shrink: 0;
  }
  .icon-btn:hover {
    background: rgba(26, 25, 24, 0.06);
    color: #978269;
    transform: translateY(-1px);
  }
  .icon-btn .counter {
    position: absolute;
    top: 2px;
    right: 2px;
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
    pointer-events: none;
  }
  [dir="rtl"] .icon-btn .counter {
    right: auto;
    left: 2px;
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
  /* 🛍️ 3. UNIFIED SLIDE-OVER CART & CHECKOUT DRAWER (PREVIOUS PROJECT) */
  /* ========================================================== */
  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    z-index: 99998;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .modal-overlay.open {
    opacity: 1;
    pointer-events: auto;
  }

  .drawer-panel {
    position: fixed;
    top: 0;
    bottom: 0;
    width: 100%;
    max-width: 520px;
    background: #ffffff;
    z-index: 99999;
    box-shadow: -6px 0 35px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: column;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  }
  [dir="rtl"] .drawer-panel {
    left: 0;
    right: auto;
    transform: translateX(-100%);
  }
  [dir="ltr"] .drawer-panel {
    right: 0;
    left: auto;
    transform: translateX(100%);
  }
  .drawer-panel.open {
    transform: translateX(0) !important;
  }

  /* Center Modals: Search & Account */
  .checkout-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.95);
    width: 92%;
    max-width: 540px;
    max-height: 85vh;
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.28);
    z-index: 100000;
    overflow-y: auto;
    opacity: 0;
    pointer-events: none;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .checkout-modal.open {
    opacity: 1;
    pointer-events: auto;
    transform: translate(-50%, -50%) scale(1);
  }
  .checkout-header {
    padding: 18px 24px;
    border-bottom: 1px solid #f0eee9;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #ffffff;
  }
  .checkout-header h3 {
    margin: 0;
    font-size: 18px;
    font-weight: 800;
  }

  /* Drawer Header */
  .drawer-header {
    padding: 18px 24px;
    border-bottom: 1px solid #f0eee9;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #ffffff;
    position: sticky;
    top: 0;
    z-index: 10;
  }
  .drawer-eyebrow {
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.12em;
    color: var(--zema-gold);
    text-transform: uppercase;
    margin-bottom: 2px;
  }
  .drawer-header h3 {
    margin: 0;
    font-size: 18px;
    font-weight: 800;
    color: var(--zema-espresso);
  }
  .drawer-close-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    color: #666;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s, color 0.2s;
  }
  .drawer-close-btn:hover {
    background: #f4f2ee;
    color: #000;
  }
  .drawer-back-btn {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 13px;
    font-weight: 700;
    color: #666;
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 4px 8px;
    border-radius: 6px;
  }
  .drawer-back-btn:hover {
    background: #f4f2ee;
    color: var(--zema-espresso);
  }

  /* Drawer Scrollable Body */
  .drawer-body {
    flex: 1;
    overflow-y: auto;
    padding: 22px 24px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }

  /* Reservation Timer Banner (Previous Project) */
  .drawer-timer-box {
    background: #fff8eb;
    border: 1px solid #fde68a;
    color: #92400e;
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* Free Shipping Meter (Threshold 2,500 EGP) */
  .drawer-shipping-meter {
    background: #faf9f6;
    border: 1px solid #eae6de;
    border-radius: 10px;
    padding: 14px 16px;
    font-size: 13px;
    color: #444;
  }
  .drawer-meter-track {
    width: 100%;
    height: 7px;
    background: #e8e4db;
    border-radius: 4px;
    margin-top: 8px;
    overflow: hidden;
  }
  .drawer-meter-fill {
    height: 100%;
    background: var(--zema-green);
    border-radius: 4px;
    transition: width 0.35s ease;
  }

  /* Cart Item Rows */
  .cart-item-row {
    display: flex;
    gap: 14px;
    padding-bottom: 16px;
    border-bottom: 1px solid #f2efe9;
  }
  .cart-item-img {
    width: 80px;
    height: 100px;
    object-fit: cover;
    border-radius: 8px;
    background: #f4f2ee;
    border: 1px solid #eae6de;
    flex-shrink: 0;
  }
  .cart-item-info {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .cart-item-title {
    font-size: 14px;
    font-weight: 700;
    margin: 0 0 2px 0;
    color: var(--zema-espresso);
  }
  .cart-item-sku {
    font-size: 11px;
    color: #888;
    font-family: monospace;
    margin-bottom: 4px;
  }
  .cart-item-price {
    font-size: 14px;
    font-weight: 800;
    color: var(--zema-espresso);
  }
  .cart-qty-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 6px;
  }
  .qty-box {
    display: inline-flex;
    align-items: center;
    border: 1px solid #dcd7ce;
    border-radius: 6px;
    background: #faf9f6;
  }
  .qty-btn {
    background: none;
    border: none;
    width: 28px;
    height: 28px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .qty-btn:hover { background: #eeebe3; }
  .qty-num {
    padding: 0 10px;
    font-size: 13px;
    font-weight: 700;
  }
  .cart-delete-btn {
    background: none;
    border: none;
    cursor: pointer;
    color: #dc2626;
    font-size: 12px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 3px;
  }
  .cart-delete-btn:hover { text-decoration: underline; }

  /* Drawer Footer */
  .drawer-footer {
    padding: 20px 24px;
    border-top: 1px solid #f0eee9;
    background: #faf9f6;
  }
  .drawer-summary-row {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    margin-bottom: 8px;
    color: #555;
  }
  .drawer-summary-row.total {
    font-size: 17px;
    font-weight: 800;
    color: var(--zema-espresso);
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px dashed #dcd7ce;
  }

  .btn-drawer-primary {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    padding: 15px;
    background: var(--zema-espresso);
    color: #ffffff;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 800;
    cursor: pointer;
    border: none;
    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    transition: background 0.2s, transform 0.15s;
    margin-top: 6px;
  }
  .btn-drawer-primary:hover {
    background: #3c3937;
    transform: translateY(-1px);
  }

  /* Empty Cart Inside Drawer */
  .cart-empty-inner {
    text-align: center;
    padding: 60px 10px;
    color: #888;
  }

  /* ========================================================== */
  /* 🇪🇬 CHECKOUT STEP (INSIDE DRAWER OR DEDICATED) */
  /* ========================================================== */
  .co-summary-box {
    background: #faf9f6;
    border: 1px solid #eae6de;
    border-radius: 10px;
    padding: 16px;
  }
  .co-products-summary-list {
    list-style: none;
    padding: 0 0 12px 0;
    margin: 0 0 12px 0;
    border-bottom: 1px solid #eae6de;
  }
  .co-prod-item-line {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    margin-bottom: 8px;
    color: #444;
  }
  .co-prod-item-line:last-child { margin-bottom: 0; }
  .co-prod-qty-badge { color: #888; font-size: 12px; }
  .co-prod-price-badge { font-weight: 700; color: var(--zema-espresso); }

  .co-summary-line {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: #555;
    margin-bottom: 6px;
  }
  .co-summary-line.highlight {
    color: #16a34a;
    font-weight: 700;
  }
  .co-summary-total {
    display: flex;
    justify-content: space-between;
    font-size: 16px;
    font-weight: 800;
    color: var(--zema-espresso);
    padding-top: 10px;
    margin-top: 10px;
    border-top: 1px dashed #dcd7ce;
  }

  /* Coupon Code */
  .coupon-row {
    display: flex;
    gap: 8px;
    margin-top: 12px;
    padding-top: 12px;
    border-top: 1px solid #eae6de;
  }
  .coupon-input {
    flex: 1;
    padding: 9px 12px;
    border: 1px solid #dcd7ce;
    border-radius: 6px;
    font-size: 13px;
    background: #ffffff;
  }
  .coupon-btn {
    padding: 9px 16px;
    background: #2c2a29;
    color: #fff;
    border: none;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
  }
  .coupon-btn:hover { background: #444; }
  .coupon-feedback {
    font-size: 12px;
    margin-top: 6px;
    text-align: center;
  }
  .coupon-feedback.ok { color: #16a34a; font-weight: 700; }
  .coupon-feedback.err { color: #dc2626; }

  /* Form Elements */
  .form-group {
    margin-bottom: 14px;
  }
  .form-group label {
    display: block;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 5px;
    color: var(--zema-espresso);
  }
  .form-control {
    width: 100%;
    padding: 10px 13px;
    border: 1px solid #dcd7ce;
    border-radius: 7px;
    font-size: 13px;
    font-family: inherit;
    background: #ffffff;
  }
  .form-control:focus {
    outline: none;
    border-color: var(--zema-espresso);
    box-shadow: 0 0 0 2px rgba(44, 42, 41, 0.1);
  }
  .form-control.input-error { border-color: #dc2626; }
  .field-error-msg { color: #dc2626; font-size: 11px; margin-top: 4px; }

  /* Payment Methods Fieldset */
  .payment-methods-fieldset {
    border: 1px solid #eae6de;
    border-radius: 10px;
    padding: 14px 16px;
    margin: 18px 0;
    background: #ffffff;
  }
  .payment-legend {
    font-size: 11px;
    font-weight: 800;
    color: #666;
    text-transform: uppercase;
    padding: 0 6px;
  }
  .payment-option-card {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 11px 12px;
    border: 1px solid #e5e0d4;
    border-radius: 8px;
    margin-top: 8px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .payment-option-card.active {
    border: 2px solid #b45309;
    background: #fef3c7;
    box-shadow: 0 2px 8px rgba(180, 83, 9, 0.12);
  }
  .payment-option-card.disabled {
    opacity: 0.5;
    cursor: not-allowed;
    background: #faf9f6;
  }
  .payment-badge-soon {
    font-size: 10px;
    background: #eee;
    color: #666;
    padding: 2px 7px;
    border-radius: 4px;
    margin-left: auto;
  }
  [dir="rtl"] .payment-badge-soon {
    margin-left: 0;
    margin-right: auto;
  }

  .account-toggle-box {
    background: #faf9f6;
    border: 1px solid #eae6de;
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 16px;
  }

  .guarantee-note-box {
    font-size: 12px;
    color: #666;
    text-align: center;
    line-height: 1.5;
    padding-top: 10px;
    border-top: 1px solid #f0eee9;
    margin-top: 12px;
  }

  /* Thank You State */
  .order-success-view {
    text-align: center;
    padding: 30px 10px;
  }
  .success-check-icon {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: #dcfce7;
    color: #16a34a;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 16px auto;
  }
  .order-number-badge {
    display: inline-block;
    padding: 8px 20px;
    background: #f4f2ee;
    border: 1px dashed #c5a059;
    border-radius: 20px;
    font-weight: 800;
    font-size: 16px;
    color: var(--zema-espresso);
    margin: 12px 0 16px 0;
  }

  /* RTL Specific Adjustments */
  [dir="rtl"] .utility-left { order: 1; }
  [dir="rtl"] .utility-right { order: 3; }
  [dir="rtl"] .brand-link { order: 2; }
  [dir="rtl"] .hero-arrow.left { right: 20px; left: auto; }
  [dir="rtl"] .hero-arrow.right { left: 20px; right: auto; }

  /* ========================================================== */
  /* 📩 ZEMA LUXURY NEWSLETTER (JOIN OUR CIRCLE) */
  /* ========================================================== */
  .zema-newsletter-section {
    border-top: 1px solid rgba(0, 0, 0, 0.08);
    background: linear-gradient(180deg, rgba(238, 231, 219, 0.25) 0%, #faf9f7 100%);
    padding: 85px 24px 75px 24px;
    text-align: center;
    direction: rtl;
  }
  .zema-newsletter-container {
    max-width: 680px;
    margin: 0 auto;
  }
  .zema-circle-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #978269;
    margin-bottom: 14px;
  }
  .zema-newsletter-title {
    font-size: clamp(28px, 4vw, 42px);
    font-weight: 800;
    color: #1A1918;
    margin: 0 0 16px 0;
    line-height: 1.25;
  }
  .zema-newsletter-desc {
    font-size: 15px;
    color: #67625d;
    line-height: 1.8;
    margin: 0 auto 32px auto;
    max-width: 520px;
    font-weight: 400;
  }
  .zema-newsletter-form {
    display: flex;
    gap: 10px;
    max-width: 440px;
    margin: 0 auto;
    align-items: stretch;
  }
  @media (max-width: 540px) {
    .zema-newsletter-form {
      flex-direction: column;
    }
  }
  .zema-newsletter-input {
    flex: 1;
    background: #ffffff;
    border: 1px solid #dcd7ce;
    border-radius: 4px;
    padding: 13px 18px;
    font-size: 14px;
    font-family: inherit;
    color: #1A1918;
    outline: none;
    transition: border-color 0.2s;
  }
  .zema-newsletter-input:focus {
    border-color: #978269;
  }
  .zema-newsletter-btn {
    background: #978269;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 13px 28px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.12em;
    cursor: pointer;
    transition: opacity 0.2s, transform 0.15s;
    white-space: nowrap;
    font-family: inherit;
  }
  .zema-newsletter-btn:hover {
    opacity: 0.92;
    transform: translateY(-1px);
  }

  /* ========================================================== */
  /* ❓ FAQ SECTION */
  /* ========================================================== */
  .zema-faq-section {
    border-top: 1px solid rgba(0, 0, 0, 0.08);
    border-bottom: 1px solid rgba(0, 0, 0, 0.08);
    background: #faf9f7;
    padding: 85px 24px 105px 24px;
    direction: rtl;
  }
  .zema-faq-container {
    max-width: 720px;
    margin: 0 auto;
  }
  .zema-faq-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #8c8880;
    margin-bottom: 12px;
  }
  .zema-faq-title {
    font-family: 'Playfair Display', 'Cairo', serif;
    font-size: clamp(32px, 4.5vw, 50px);
    font-weight: 800;
    color: #1A1918;
    margin: 0 0 45px 0;
    text-align: center;
  }
  .zema-faq-accordion {
    border-top: 1px solid rgba(0, 0, 0, 0.09);
    border-bottom: 1px solid rgba(0, 0, 0, 0.09);
  }
  .zema-faq-item {
    border-bottom: 1px solid rgba(0, 0, 0, 0.09);
  }
  .zema-faq-item:last-child {
    border-bottom: none;
  }
  .zema-faq-summary {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 22px 4px;
    font-size: 16px;
    font-weight: 700;
    color: #1A1918;
    cursor: pointer;
    list-style: none;
    user-select: none;
    transition: color 0.2s;
  }
  .zema-faq-summary::-webkit-details-marker {
    display: none;
  }
  .zema-faq-summary:hover {
    color: #978269;
  }
  .zema-faq-icon {
    font-size: 24px;
    line-height: 1;
    color: #978269;
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    font-weight: 300;
    margin-inline-start: 12px;
  }
  .zema-faq-item[open] .zema-faq-icon {
    transform: rotate(45deg);
  }
  .zema-faq-body {
    padding: 0 4px 22px 4px;
    font-size: 14.5px;
    color: #67625d;
    line-height: 1.85;
  }

  /* ========================================================== */
  /* 🏛️ FOOTER */
  /* ========================================================== */
  .zema-footer {
    border-top: 1px solid rgba(0, 0, 0, 0.08);
    background: rgba(238, 231, 219, 0.4);
    padding: 60px 24px 50px 24px;
    direction: rtl;
  }
  .zema-footer-grid {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1.4fr 1fr 1fr;
    gap: 48px;
  }
  @media (max-width: 768px) {
    .zema-footer-grid {
      grid-template-columns: 1fr;
      gap: 36px;
    }
  }
  .zema-footer-eyebrow {
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #67625d;
    margin: 0 0 16px 0;
  }
  .zema-footer-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 9px;
  }
  .zema-footer-list a {
    color: #1A1918;
    text-decoration: none;
    font-size: 13.5px;
    transition: color 0.2s, transform 0.15s;
    display: inline-block;
  }
  .zema-footer-list a:hover {
    color: #978269;
    transform: translateX(-2px);
  }
  .zema-footer-social-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: #1A1918;
    transition: color 0.2s, transform 0.15s;
    text-decoration: none;
  }
  .zema-footer-social-icon:hover {
    color: #978269;
    transform: translateY(-2px);
  }

  /* ========================================================== */
  /* 💬 FLOATING WHATSAPP BUTTON */
  /* ========================================================== */
  .zema-floating-wa {
    position: fixed;
    bottom: 24px;
    left: 24px;
    z-index: 850;
    display: flex;
    width: 54px;
    height: 54px;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background-color: #25D366;
    color: #ffffff;
    box-shadow: 0 4px 18px rgba(37, 211, 102, 0.4);
    transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s;
    text-decoration: none;
  }
  .zema-floating-wa:hover {
    transform: scale(1.08);
    box-shadow: 0 6px 24px rgba(37, 211, 102, 0.6);
  }
  @media (max-width: 600px) {
    .zema-floating-wa {
      bottom: 76px;
      left: 16px;
      width: 48px;
      height: 48px;
    }
  }
  </style>
</head>
<body>

  <!-- ========================================================== -->
  <!-- 🚚 1. TOP ANNOUNCEMENT BAR (EGP 2,500 THRESHOLD) -->
  <!-- ========================================================== -->
  <div class="ticker-wrap" aria-label="Announcements" style="text-align:center; padding:9px 16px; font-size:12px; font-weight:600; letter-spacing:0.04em; background:var(--zema-espresso); color:#FAF9F6; display:flex; align-items:center; justify-content:center; gap:8px;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
    <span id="ticker-msg-1">شحن مجاني لكافة محافظات مصر للطلبات فوق 2,500 ج.م</span>
  </div>

  <!-- Header -->
  <header class="site-header">
    <div class="utility-row">
      <div class="utility-side utility-left">
        <button class="icon-btn mobile-menu-trigger" aria-label="Open menu" onclick="toggleMobileMenu()">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16"></path><path d="M4 12h16"></path><path d="M4 19h16"></path></svg>
        </button>
        <button class="icon-btn" aria-label="Search" onclick="toggleSearchModal(true)" title="بحث">
          <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.5-3.5"></path></svg>
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
        <button class="icon-btn" aria-label="Account" onclick="toggleAccountModal(true)" title="تسجيل الدخول / حسابي">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        </button>
        <button class="icon-btn" aria-label="Wishlist" onclick="toggleWishlistDrawer(true)" title="المفضلة">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5"></path></svg>
          <span class="counter" id="wishlistCountBadge">0</span>
        </button>
        <button class="icon-btn" aria-label="Shopping bag" onclick="showCartView()" title="سلة المشتريات">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h2l2.4 12.5a2 2 0 002 1.5h7.6a2 2 0 002-1.5L21 7H6"></path><circle cx="9" cy="20" r="1.4"></circle><circle cx="18" cy="20" r="1.4"></circle></svg>
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
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="color:var(--zema-green); flex-shrink:0;"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
              <span>شحن مجاني فوق 2,500 ج.م</span>
            </div>
            <div class="pdp-perk-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="color:var(--zema-green); flex-shrink:0;"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg>
              <span>الدفع عند الاستلام متاح</span>
            </div>
            <div class="pdp-perk-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="color:var(--zema-green); flex-shrink:0;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              <span>توصيل لكافة محافظات مصر</span>
            </div>
            <div class="pdp-perk-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="color:var(--zema-green); flex-shrink:0;"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><polyline points="3 3 3 8 8 8"></polyline></svg>
              <span>استبدال واسترجاع خلال 14 يوماً</span>
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

  <!-- ========================================================== -->
  <!-- 📩 1. JOIN OUR CIRCLE (NEWSLETTER) -->
  <!-- ========================================================== -->
  <section id="newsletter" class="zema-newsletter-section" dir="rtl">
    <div class="zema-newsletter-container">
      <p class="zema-circle-eyebrow">JOIN OUR CIRCLE</p>
      <h2 class="zema-newsletter-title">انضم إلى دائرتنا</h2>
      <p class="zema-newsletter-desc">كُن أول من يكتشف العينات الجديدة، العروض الحصرية، والمجموعات الخاصة.</p>
      <form class="zema-newsletter-form" onsubmit="event.preventDefault(); handleNewsletterSubmit(this);">
        <input type="email" placeholder="بريدك الإلكتروني" aria-label="بريدك الإلكتروني" class="zema-newsletter-input" required />
        <button type="submit" class="zema-newsletter-btn">اشترك</button>
      </form>
      <div id="newsletterSuccess" style="display:none; margin-top:16px; color:#1B7D3F; font-size:14px; font-weight:700;">✓ شكراً لاشتراكك في دائرة زِيما! ستصلك أحدث المجموعات والعروض الحصرية أولاً بأول.</div>
    </div>
  </section>

  <!-- ========================================================== -->
  <!-- ❓ 2. FAQ (الأسئلة الشائعة) -->
  <!-- ========================================================== -->
  <section id="faq" class="zema-faq-section" dir="rtl">
    <div class="zema-faq-container">
      <div style="text-align:center; margin-bottom: 40px;">
        <p class="zema-faq-eyebrow">FAQ</p>
        <h2 class="zema-faq-title">الأسئلة الشائعة</h2>
      </div>
      <div class="zema-faq-accordion">
        <details class="zema-faq-item">
          <summary class="zema-faq-summary">
            <span>هل الدفع عند الاستلام متاح؟</span>
            <span class="zema-faq-icon">+</span>
          </summary>
          <div class="zema-faq-body">
            نعم، الدفع عند الاستلام متاح لجميع المحافظات داخل مصر.
          </div>
        </details>
        <details class="zema-faq-item">
          <summary class="zema-faq-summary">
            <span>كم تستغرق مدة الشحن؟</span>
            <span class="zema-faq-icon">+</span>
          </summary>
          <div class="zema-faq-body">
            من 2 إلى 5 أيام عمل حسب المحافظة. القاهرة والجيزة عادةً خلال 48 ساعة.
          </div>
        </details>
        <details class="zema-faq-item">
          <summary class="zema-faq-summary">
            <span>هل يمكنني فتح الشحنة قبل الدفع؟</span>
            <span class="zema-faq-icon">+</span>
          </summary>
          <div class="zema-faq-body">
            لحماية المنتجات الفاخرة لا يُسمح بفتح الشحنة قبل الدفع، ولكن لديك حق الاستبدال خلال 14 يوماً.
          </div>
        </details>
        <details class="zema-faq-item">
          <summary class="zema-faq-summary">
            <span>هل المنتجات أصلية ومضمونة؟</span>
            <span class="zema-faq-icon">+</span>
          </summary>
          <div class="zema-faq-body">
            جميع منتجات ZEMA مختارة بعناية ومضمونة الجودة، مع إمكانية الاستبدال أو الاسترجاع.
          </div>
        </details>
      </div>
    </div>
  </section>

  <!-- ========================================================== -->
  <!-- 🏛️ 3. FOOTER (المشروع القديم مع الأقسام: حقائب، محافظ، أحزمة) -->
  <!-- ========================================================== -->
  <footer class="zema-footer" dir="rtl">
    <div class="zema-footer-grid">
      <!-- Right Column: Logo & Arabic Bio -->
      <div class="zema-footer-col">
        <a href="#top" onclick="showHomePage()" style="display:inline-block; margin-bottom:16px;">
          <img src="__LOGO_B64__" alt="ZEMA" style="height:auto; width:110px; max-width:110px; display:block;" />
        </a>
        <p style="font-size:13.5px; color:#67625d; line-height:1.75; max-width:320px; margin:0;">
          زِيما — مجموعة مختارة من الحقائب الجلدية الفاخرة والمحافظ والإكسسوارات، صُنعت لمن يدرك تفاصيل الأناقة.
        </p>
      </div>

      <!-- Center Column: روابط (Links) with requested categories -->
      <div class="zema-footer-col">
        <p class="zema-footer-eyebrow">روابط</p>
        <ul class="zema-footer-list">
          <li><a href="#bags-section" onclick="showHomePage()">المتجر</a></li>
          <li><a href="#bags-section" onclick="showHomePage()">حقائب</a></li>
          <li><a href="#bags-section" onclick="showHomePage()">محافظ</a></li>
          <li><a href="#bags-section" onclick="showHomePage()">أحزمة</a></li>
          <li><a href="#bags-section" onclick="showHomePage()">العروض</a></li>
          <li><a href="#faq">الأسئلة الشائعة</a></li>
          <li><a href="javascript:void(0)" onclick="toggleAccountModal(true)">تتبع شحنتك</a></li>
        </ul>
      </div>

      <!-- Left Column: تواصل معنا & حقوق النشر -->
      <div class="zema-footer-col">
        <p class="zema-footer-eyebrow">تواصل معنا</p>
        <div style="display:flex; align-items:center; gap:14px; margin-bottom:18px;">
          <a href="https://www.facebook.com/zema.luxury/" target="_blank" rel="noopener noreferrer" aria-label="Facebook" class="zema-footer-social-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 22v-8h2.7l.4-3.1h-3.1V8.9c0-.9.3-1.5 1.6-1.5h1.7V4.6c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.1V11H7.7v3.1h2.7V22h3.1z"></path></svg>
          </a>
          <a href="https://www.instagram.com/zema.luxury/" target="_blank" rel="noopener noreferrer" aria-label="Instagram" class="zema-footer-social-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="3" width="18" height="18" rx="5"></rect><circle cx="12" cy="12" r="4"></circle><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"></circle></svg>
          </a>
        </div>
        <p style="font-size:12px; color:#67625d; margin:0; line-height:1.6;">
          © 2026 ZEMA Maison — أناقة خالدة، فخامة عصرية
        </p>
      </div>
    </div>
  </footer>

  <!-- ========================================================== -->
  <!-- 💬 4. FLOATING WHATSAPP BUTTON (من المشروع القديم) -->
  <!-- ========================================================== -->
  <a href="https://wa.me/201032117373?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D9%8B%D8%8C%20%D8%A3%D8%B1%D8%BA%D8%A8%20%D8%A8%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%81%D8%B3%D8%A7%D8%B1%20%D8%B9%D9%86%20%D9%85%D9%86%D8%AA%D8%AC%D8%A7%D8%AA%20%D8%B2%D9%90%D9%8A%D9%85%D8%A7" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp" class="zema-floating-wa">
    <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 018.413 3.488 11.82 11.82 0 013.48 8.414c-.003 6.555-5.338 11.89-11.893 11.89a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"></path></svg>
  </a>

  <!-- ========================================================== -->
  <!-- 🛍️ 3. UNIFIED SLIDE-OVER DRAWER (CART -> CHECKOUT -> THANK YOU) -->
  <!-- ========================================================== -->
  <div class="modal-overlay" id="unifiedOverlay" onclick="closeUnifiedDrawer()"></div>
  <aside class="drawer-panel" id="unifiedDrawer" aria-label="Shopping Cart & Checkout">

    <!-- ==================== STEP 1: CART VIEW ==================== -->
    <div id="drawerStepCart" style="display:flex; flex-direction:column; height:100%;">
      <div class="drawer-header">
        <div>
          <p class="drawer-eyebrow" id="cart-drawer-eyebrow">YOUR CART</p>
          <h3 id="cart-drawer-title">حقيبة التسوق (<span id="cartTotalItems">0</span>)</h3>
        </div>
        <button class="drawer-close-btn" onclick="closeUnifiedDrawer()" aria-label="Close cart"><i data-lucide="x"></i></button>
      </div>

      <div class="drawer-body">
        <!-- ⏱ Reservation Timer Banner (Previous Project) -->
        <div class="drawer-timer-box">
          <i data-lucide="clock" style="width:16px;height:16px;"></i>
          <span id="cartTimerText">⏱ القطع محجوزة في سلتك لمدة 15:00 دقيقة</span>
        </div>

        <!-- 🚚 2,500 EGP Free Shipping Progress Bar -->
        <div class="drawer-shipping-meter" id="drawerShippingMeter">
          <div id="drawerShippingStatusText">🚚 تبقى لك <strong>2,500 ج.م</strong> للحصول على شحن مجاني!</div>
          <div class="drawer-meter-track">
            <div class="drawer-meter-fill" id="drawerMeterFill" style="width: 0%;"></div>
          </div>
        </div>

        <!-- Items Container -->
        <div id="drawerCartItemsList">
          <!-- Rendered dynamically -->
        </div>
      </div>

      <div class="drawer-footer">
        <div class="drawer-summary-row">
          <span id="lbl-cart-subtotal">المجموع الفرعي:</span>
          <span id="drawerCartSubtotal">0.00 ج.م</span>
        </div>
        <div class="drawer-summary-row total">
          <span id="lbl-cart-total">الإجمالي:</span>
          <span id="drawerCartTotal">0.00 ج.م</span>
        </div>

        <button class="btn-drawer-primary" id="btnProceedToCheckout" onclick="goToCheckoutStep()">
          <i data-lucide="check-circle-2"></i>
          <span id="btn-proceed-co-text">متابعة إتمام الطلب</span>
        </button>

        <p class="guarantee-note-box" id="cart-guarantee-note">
          🛡️ الدفع عند الاستلام متاح — حقك في الاستبدال أو الاسترجاع مكفول خلال ١٤ يوماً.
        </p>
      </div>
    </div>

    <!-- ==================== STEP 2: CHECKOUT VIEW ==================== -->
    <div id="drawerStepCheckout" style="display:none; flex-direction:column; height:100%;">
      <div class="drawer-header">
        <button class="drawer-back-btn" onclick="goToCartStep()" aria-label="Back to cart">
          <i data-lucide="arrow-right" id="coBackIcon" style="width:16px;height:16px;"></i>
          <span id="co-back-text">العودة للسلة</span>
        </button>
        <div>
          <p class="drawer-eyebrow" id="co-header-eyebrow">CHECKOUT</p>
          <h3 id="co-header-title">إتمام الطلب</h3>
        </div>
        <button class="drawer-close-btn" onclick="closeUnifiedDrawer()" aria-label="Close checkout"><i data-lucide="x"></i></button>
      </div>

      <div class="drawer-body">
        <!-- Ordered Items Summary at Top -->
        <div class="co-summary-box">
          <div style="font-size:12px; font-weight:800; color:#888; text-transform:uppercase; margin-bottom:8px;" id="lbl-co-summary-title">ملخص المنتجات:</div>
          <ul class="co-products-summary-list" id="coDrawerProductsSummary">
            <!-- Dynamically populated: Name × Qty ... Line Price -->
          </ul>

          <div class="co-summary-line">
            <span id="co-sum-subtotal-lbl">المجموع الفرعي:</span>
            <span id="coDrawerSubtotal">0 ج.م</span>
          </div>
          <div class="co-summary-line highlight" id="coDrawerDiscountRow" style="display:none;">
            <span id="coDrawerDiscountLabel">خصم (ZEMA10):</span>
            <span id="coDrawerDiscountAmount">-0 ج.م</span>
          </div>
          <div class="co-summary-line">
            <span id="co-sum-shipping-lbl">الشحن:</span>
            <span id="coDrawerShipping">اختر المحافظة لحساب الشحن</span>
          </div>
          <div class="co-summary-total">
            <span id="co-sum-total-lbl">الإجمالي:</span>
            <span id="coDrawerTotal">0 ج.م</span>
          </div>

          <!-- Promo Code Input -->
          <div class="coupon-row">
            <input type="text" id="coDrawerCouponInput" class="coupon-input" placeholder="كود الخصم (مثال: ZEMA10)" />
            <button type="button" class="coupon-btn" onclick="applyDrawerCoupon()">تطبيق</button>
          </div>
          <div id="coDrawerCouponFeedback" class="coupon-feedback" style="display:none;"></div>
        </div>

        <!-- Form Fields -->
        <form id="drawerCheckoutForm" onsubmit="handleDrawerCheckoutSubmit(event)">
          <div style="margin-bottom:14px;">
            <p class="drawer-eyebrow" id="co-fields-eyebrow">بيانات التوصيل</p>
            <h4 style="font-size:15px; font-weight:800; margin:0;" id="co-fields-title">اطلب الآن — الدفع عند الاستلام</h4>
          </div>

          <!-- 1. Full Name -->
          <div class="form-group">
            <label id="lbl-name">الاسم بالكامل *</label>
            <input type="text" id="custName" class="form-control" placeholder="مثال: ياسمين أحمد" required minlength="3" maxlength="80" />
          </div>

          <!-- 2. Egyptian Phone with Regex -->
          <div class="form-group">
            <label id="lbl-phone">رقم الهاتف (مثال: 01012345678) *</label>
            <input type="tel" id="custPhone" class="form-control" placeholder="01012345678" dir="ltr" inputmode="numeric" required oninput="validatePhoneLive()" />
            <div id="phoneErrorMsg" class="field-error-msg" style="display:none;">رقم غير صحيح. يبدأ بـ 01 و11 رقم.</div>
          </div>

          <!-- 3. Governorate -->
          <div class="form-group">
            <label id="lbl-gov">المحافظة *</label>
            <select id="custGov" class="form-control" required onchange="onDrawerGovChange()">
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

          <!-- 4. City / Area -->
          <div class="form-group">
            <label id="lbl-city">المدينة / المنطقة (اختياري)</label>
            <input type="text" id="custCity" class="form-control" placeholder="مثال: مدينة نصر / التجمع / سموحة" maxlength="80" />
          </div>

          <!-- 5. Detailed Address -->
          <div class="form-group">
            <label id="lbl-address">العنوان بالتفصيل *</label>
            <textarea id="custAddress" class="form-control" rows="2" placeholder="المنطقة، الشارع، رقم العقار، الشقة أو علامة مميزة" required minlength="8" maxlength="300"></textarea>
          </div>

          <!-- 6. Email -->
          <div class="form-group">
            <label id="lbl-email">البريد الإلكتروني (اختياري)</label>
            <input type="email" id="custEmail" class="form-control" placeholder="name@example.com" dir="ltr" />
          </div>

          <!-- 7. Account Creation Checkbox -->
          <div class="account-toggle-box">
            <label style="display:flex; align-items:center; gap:8px; font-size:12px; cursor:pointer; font-weight:700;">
              <input type="checkbox" id="drawerAccountChk" onchange="toggleDrawerPasswordInput()" />
              <span id="lbl-create-acc">أنشئ حساباً لحفظ طلبي (اختياري)</span>
            </label>
            <div id="drawerPasswordContainer" style="display:none; margin-top:8px;">
              <input type="password" id="drawerPassword" class="form-control" placeholder="كلمة المرور (٦ أحرف على الأقل)" minlength="6" />
            </div>
            <p style="font-size:11px; color:#888; margin:4px 0 0 0;" id="lbl-guest-note">يمكنك إتمام الطلب كضيف بدون تسجيل.</p>
          </div>

          <!-- 8. Payment Methods Fieldset -->
          <div class="payment-methods-fieldset">
            <div class="payment-legend" id="lbl-pay-title">طريقة الدفع</div>
            
            <!-- COD: Active -->
            <label class="payment-option-card active">
              <input type="radio" name="payOption" value="cod" checked />
              <i data-lucide="banknote" style="width:20px;height:20px;color:#16a34a;"></i>
              <div>
                <strong style="display:block; font-size:13px;" id="lbl-pay-cod">الدفع عند الاستلام</strong>
                <span style="font-size:11px; color:#666;" id="lbl-pay-cod-desc">ادفع نقداً للمندوب عند وصول طلبك</span>
              </div>
            </label>

            <!-- Card: Coming soon -->
            <div class="payment-option-card disabled">
              <input type="radio" disabled />
              <i data-lucide="credit-card" style="width:20px;height:20px;color:#999;"></i>
              <span style="font-size:13px; color:#666;" id="lbl-pay-card">فيزا / ماستركارد</span>
              <span class="payment-badge-soon" id="lbl-pay-soon-1">قريباً</span>
            </div>

            <!-- Apple Pay: Coming soon -->
            <div class="payment-option-card disabled">
              <input type="radio" disabled />
              <i data-lucide="smartphone" style="width:20px;height:20px;color:#999;"></i>
              <span style="font-size:13px; color:#666;">Apple Pay</span>
              <span class="payment-badge-soon" id="lbl-pay-soon-2">قريباً</span>
            </div>

            <!-- InstaPay: Coming soon -->
            <div class="payment-option-card disabled">
              <input type="radio" disabled />
              <i data-lucide="send" style="width:20px;height:20px;color:#999;"></i>
              <span style="font-size:13px; color:#666;" id="lbl-pay-instapay">إنستاباي</span>
              <span class="payment-badge-soon" id="lbl-pay-soon-3">قريباً</span>
            </div>

            <p style="font-size:11px; color:#888; margin-top:8px; line-height:1.4;" id="lbl-pay-note">
              الدفع عند الاستلام هو الطريقة المتاحة حالياً. باقي الطرق قيد التفعيل.
            </p>
          </div>

          <!-- Submit Order Button (NO WHATSAPP BUTTON!) -->
          <button type="submit" class="btn-drawer-primary" id="btnSubmitDrawerOrder" style="padding:16px; font-size:16px;">
            <i data-lucide="check"></i>
            <span id="btnSubmitDrawerOrderText">تأكيد الطلب</span>
          </button>

          <p style="font-size:11px; color:#777; text-align:center; margin:10px 0 6px 0;" id="lbl-delivery-note">
            توصيل سريع خلال ٢ - ٤ أيام عمل لجميع المحافظات
          </p>

          <p class="guarantee-note-box" id="lbl-co-guarantee">
            🛡️ الدفع عند الاستلام متاح — حقك في الاستبدال أو الاسترجاع مكفول خلال ١٤ يوماً.
          </p>
        </form>
      </div>
    </div>

    <!-- ==================== STEP 3: THANK YOU VIEW ==================== -->
    <div id="drawerStepThankYou" style="display:none; flex-direction:column; height:100%;">
      <div class="drawer-header">
        <div>
          <p class="drawer-eyebrow" id="ty-drawer-eyebrow">ORDER CONFIRMED</p>
          <h3 id="ty-drawer-title">تم تأكيد طلبك بنجاح!</h3>
        </div>
        <button class="drawer-close-btn" onclick="closeUnifiedDrawer()" aria-label="Close dialog"><i data-lucide="x"></i></button>
      </div>

      <div class="drawer-body order-success-view">
        <div class="success-check-icon">
          <i data-lucide="check" style="width:38px;height:38px;"></i>
        </div>
        <h2 style="font-size:22px; font-weight:800; margin:0;" id="ty-main-title">شكراً لثقتك في زِيما</h2>
        <p style="font-size:13px; color:#666; margin:8px 0 14px 0;" id="ty-body-msg">
          تم تسجيل طلبك بنجاح! سيقوم فريق خدمة العملاء بالتواصل معك عبر الهاتف خلال ٢٤ ساعة لتأكيد تفاصيل الشحن والتسليم.
        </p>

        <div class="order-number-badge" id="drawerOrderNumberDisplay">رقم الطلب: #ZM260925-1001</div>

        <div style="background:#faf9f6; border:1px solid #eee; border-radius:10px; padding:16px; text-align:start; font-size:13px; line-height:1.8; margin-bottom:18px;">
          <div><strong id="ty-lbl-name">الاسم:</strong> <span id="tyDrawerName">--</span></div>
          <div><strong id="ty-lbl-phone">الهاتف:</strong> <span id="tyDrawerPhone">--</span></div>
          <div><strong id="ty-lbl-addr">العنوان:</strong> <span id="tyDrawerAddress">--</span></div>
          <div><strong id="ty-lbl-pay">طريقة الدفع:</strong> <span id="tyDrawerPayment">الدفع عند الاستلام</span></div>
          <div><strong id="ty-lbl-total">الإجمالي المطلوب:</strong> <strong style="color:var(--zema-espresso);" id="tyDrawerTotal">--</strong></div>
          <div><strong id="ty-lbl-time">موعد التوصيل:</strong> <span style="color:#1b7d3f; font-weight:700;">خلال 24 - 48 ساعة</span></div>
        </div>

        <div style="display:flex; gap:10px;">
          <button class="btn-drawer-primary" style="flex:1; margin-top:0;" onclick="closeUnifiedDrawer(); toggleAccountModal(true);">
            <i data-lucide="truck" style="width:14px;height:14px;"></i>
            <span id="ty-btn-track">تتبع شحنتك</span>
          </button>
          <button class="btn-drawer-primary" style="flex:1; margin-top:0; background:#f4f2ee; color:var(--zema-espresso); border:1px solid #dcd7ce;" onclick="closeUnifiedDrawer()">
            <span id="ty-btn-back">متابعة التسوق</span>
          </button>
        </div>
      </div>
    </div>
  </aside>

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
    // 🛍️ 3. UNIFIED SLIDE-OVER DRAWER (CART -> CHECKOUT -> THANK YOU)
    // ==========================================
    let activePromo = null; // { code: 'ZEMA10', rate: 0.1 }

    function openUnifiedDrawer(step = 'cart') {
      const overlay = document.getElementById('unifiedOverlay');
      const drawer = document.getElementById('unifiedDrawer');
      if (overlay && drawer) {
        overlay.classList.add('open');
        drawer.classList.add('open');
      }

      if (step === 'checkout') {
        goToCheckoutStep();
      } else if (step === 'thankyou') {
        goToThankYouStep();
      } else {
        goToCartStep();
      }
    }

    function closeUnifiedDrawer() {
      const overlay = document.getElementById('unifiedOverlay');
      const drawer = document.getElementById('unifiedDrawer');
      if (overlay && drawer) {
        overlay.classList.remove('open');
        drawer.classList.remove('open');
      }
      if (window.location.hash === '#cart' || window.location.hash === '#checkout') {
        window.location.hash = '';
      }
    }

    function goToCartStep() {
      const stepCart = document.getElementById('drawerStepCart');
      const stepCo = document.getElementById('drawerStepCheckout');
      const stepTy = document.getElementById('drawerStepThankYou');
      if (stepCart) stepCart.style.display = 'flex';
      if (stepCo) stepCo.style.display = 'none';
      if (stepTy) stepTy.style.display = 'none';
      window.location.hash = 'cart';
      renderDrawerCart();
    }

    function goToCheckoutStep() {
      if (cart.length === 0) {
        goToCartStep();
        return;
      }
      const stepCart = document.getElementById('drawerStepCart');
      const stepCo = document.getElementById('drawerStepCheckout');
      const stepTy = document.getElementById('drawerStepThankYou');
      if (stepCart) stepCart.style.display = 'none';
      if (stepCo) stepCo.style.display = 'flex';
      if (stepTy) stepTy.style.display = 'none';
      window.location.hash = 'checkout';
      renderDrawerCheckout();
    }

    function goToThankYouStep(orderData) {
      const stepCart = document.getElementById('drawerStepCart');
      const stepCo = document.getElementById('drawerStepCheckout');
      const stepTy = document.getElementById('drawerStepThankYou');
      if (stepCart) stepCart.style.display = 'none';
      if (stepCo) stepCo.style.display = 'none';
      if (stepTy) stepTy.style.display = 'flex';
      window.location.hash = 'thank-you';

      if (orderData) {
        const isAr = currentLang === 'ar';
        const numEl = document.getElementById('drawerOrderNumberDisplay');
        if (numEl) numEl.textContent = '#' + orderData.order_number;
        const nameEl = document.getElementById('tyDrawerName');
        if (nameEl) nameEl.textContent = orderData.customer_name;
        const phoneEl = document.getElementById('tyDrawerPhone');
        if (phoneEl) phoneEl.textContent = orderData.customer_phone;
        const addrEl = document.getElementById('tyDrawerAddress');
        if (addrEl) addrEl.textContent = orderData.governorate + (orderData.city ? ' - ' + orderData.city : '') + ' - ' + orderData.address;
        const totEl = document.getElementById('tyDrawerTotal');
        if (totEl) totEl.textContent = orderData.total.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      }
      lucide.createIcons();
    }

    function showCartView() {
      openUnifiedDrawer('cart');
    }

    function showCheckoutView() {
      openUnifiedDrawer('checkout');
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
      openUnifiedDrawer('cart');
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
      renderDrawerCart();
    }

    function saveCart() {
      localStorage.setItem('zema_cart', JSON.stringify(cart));
    }

    function updateCartBadge() {
      const countBadge = document.getElementById('cartCountBadge');
      const totalItemsSpan = document.getElementById('cartTotalItems');
      const totalItems = cart.reduce((sum, i) => sum + i.qty, 0);
      if (countBadge) countBadge.textContent = totalItems;
      if (totalItemsSpan) totalItemsSpan.textContent = totalItems;
    }

    function renderDrawerCart() {
      updateCartBadge();
      const listContainer = document.getElementById('drawerCartItemsList');
      const subtotalEl = document.getElementById('drawerCartSubtotal');
      const totalEl = document.getElementById('drawerCartTotal');
      const meterFill = document.getElementById('drawerMeterFill');
      const meterText = document.getElementById('drawerShippingStatusText');
      const btnCo = document.getElementById('btnProceedToCheckout');

      const isAr = currentLang === 'ar';
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const threshold = 2500;
      const progress = Math.min(100, Math.round((subtotal / threshold) * 100));

      if (meterFill && meterText) {
        meterFill.style.width = progress + '%';
        if (subtotal >= threshold) {
          meterText.innerHTML = '🎉 <strong>' + (isAr ? 'مبروك! طلبك مؤهل للشحن المجاني لكافة المحافظات!' : "Congrats! You've unlocked FREE shipping nationwide!") + '</strong>';
          meterFill.style.background = '#1b7d3f';
        } else {
          const remaining = threshold - subtotal;
          meterText.innerHTML = '🚚 ' + (isAr ? 'أضف منتجات بقيمة <strong>' + remaining.toLocaleString() + ' ج.م</strong> للحصول على شحن مجاني!' : 'Add products worth <strong>' + remaining.toLocaleString() + ' EGP</strong> more for free shipping!');
          meterFill.style.background = '#C5A059';
        }
      }

      if (subtotalEl) subtotalEl.textContent = subtotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      if (totalEl) totalEl.textContent = subtotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      if (!listContainer) return;

      if (cart.length === 0) {
        listContainer.innerHTML = `
          <div class="cart-empty-inner">
            <i data-lucide="shopping-bag" style="width:48px;height:48px;margin:0 auto 12px auto; opacity:0.35;"></i>
            <h4 style="font-size:16px; margin:0 0 6px 0;">${isAr ? 'سلتك فارغة حالياً.' : 'Your cart is empty.'}</h4>
            <p style="color:#777; font-size:13px; margin:0 0 16px 0;">${isAr ? 'استكشف تشكيلاتنا الفاخرة واختر ما يناسب أناقتك' : 'Explore our luxury collections'}</p>
            <button class="btn-drawer-primary" style="width:auto; padding:10px 24px; margin:0 auto;" onclick="closeUnifiedDrawer()">
              ${isAr ? 'ابدأ التسوق' : 'Start Shopping'}
            </button>
          </div>
        `;
        if (btnCo) btnCo.disabled = true;
      } else {
        if (btnCo) btnCo.disabled = false;
        let html = '';
        cart.forEach(item => {
          const title = isAr ? item.nameAr : item.nameEn;
          const lineTotal = item.price * item.qty;
          html += `
            <div class="cart-item-row">
              <img src="${item.img}" class="cart-item-img" alt="${title}" />
              <div class="cart-item-info">
                <div>
                  <h4 class="cart-item-title">${title}</h4>
                  <div class="cart-item-sku">${item.sku}</div>
                  <div class="cart-item-price">${lineTotal.toLocaleString()} ${isAr ? 'ج.م' : 'EGP'}</div>
                </div>
                <div class="cart-qty-row">
                  <div class="qty-box">
                    <button class="qty-btn" onclick="changeCartItemQty('${item.id}', -1)" aria-label="-">−</button>
                    <span class="qty-num">${item.qty}</span>
                    <button class="qty-btn" onclick="changeCartItemQty('${item.id}', 1)" aria-label="+">+</button>
                  </div>
                  <button class="cart-delete-btn" onclick="changeCartItemQty('${item.id}', -999)">
                    <i data-lucide="trash-2" style="width:14px;height:14px;"></i>
                    <span>${isAr ? 'حذف' : 'Remove'}</span>
                  </button>
                </div>
              </div>
            </div>
          `;
        });
        listContainer.innerHTML = html;
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

    function renderDrawerCheckout() {
      const isAr = currentLang === 'ar';
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const govEl = document.getElementById('custGov');
      const gov = govEl ? govEl.value : '';
      const shipping = calculateShipping(subtotal, gov);

      // 1. Render Ordered Items Summary List
      const summaryList = document.getElementById('coDrawerProductsSummary');
      if (summaryList) {
        let itemsHtml = '';
        cart.forEach(item => {
          const title = isAr ? item.nameAr : item.nameEn;
          const lineTotal = item.price * item.qty;
          itemsHtml += `
            <li class="co-prod-item-line">
              <div>
                <span>${title}</span>
                <span class="co-prod-qty-badge"> × ${item.qty}</span>
              </div>
              <span class="co-prod-price-badge">${lineTotal.toLocaleString()} ${isAr ? 'ج.م' : 'EGP'}</span>
            </li>
          `;
        });
        summaryList.innerHTML = itemsHtml;
      }

      // 2. Calculations
      let discountAmount = 0;
      if (activePromo) {
        discountAmount = Math.round(subtotal * activePromo.rate);
      }

      const subtotalEl = document.getElementById('coDrawerSubtotal');
      if (subtotalEl) subtotalEl.textContent = subtotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      const discRow = document.getElementById('coDrawerDiscountRow');
      if (discRow) {
        if (discountAmount > 0) {
          discRow.style.display = 'flex';
          document.getElementById('coDrawerDiscountLabel').textContent = (isAr ? 'خصم ' : 'Discount ') + `(${activePromo.code}):`;
          document.getElementById('coDrawerDiscountAmount').textContent = '- ' + discountAmount.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
        } else {
          discRow.style.display = 'none';
        }
      }

      const shippingEl = document.getElementById('coDrawerShipping');
      if (shippingEl) {
        if (shipping === 0) {
          shippingEl.innerHTML = '<span style="color:#16a34a; font-weight:bold;">' + (isAr ? 'مجاني 🎉' : 'Free 🎉') + '</span>';
        } else if (shipping !== null) {
          shippingEl.textContent = shipping + (isAr ? ' ج.م' : ' EGP');
        } else {
          shippingEl.textContent = isAr ? 'اختر المحافظة لحساب الشحن' : 'Select governorate to calculate shipping';
        }
      }

      const activeShipping = shipping !== null ? shipping : 0;
      const finalTotal = Math.max(0, subtotal - discountAmount + activeShipping);
      const finalTotalEl = document.getElementById('coDrawerTotal');
      if (finalTotalEl) finalTotalEl.textContent = finalTotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      const btnText = document.getElementById('btnSubmitDrawerOrderText');
      if (btnText) btnText.textContent = (isAr ? 'تأكيد الطلب — ' : 'Confirm Order — ') + finalTotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
    }

    function onDrawerGovChange() {
      renderDrawerCheckout();
    }

    function validatePhoneLive() {
      const phoneInput = document.getElementById('custPhone');
      const errBox = document.getElementById('phoneErrorMsg');
      if (!phoneInput) return true;
      const cleanPhone = phoneInput.value.replace(/\\D/g, '');
      phoneInput.value = cleanPhone;

      const isEgyptian = /^01[0125][0-9]{8}$/.test(cleanPhone);
      if (cleanPhone.length > 0 && !isEgyptian) {
        phoneInput.classList.add('input-error');
        if (errBox) errBox.style.display = 'block';
        return false;
      } else {
        phoneInput.classList.remove('input-error');
        if (errBox) errBox.style.display = 'none';
        return isEgyptian;
      }
    }

    function applyDrawerCoupon() {
      const input = document.getElementById('coDrawerCouponInput');
      const feedback = document.getElementById('coDrawerCouponFeedback');
      const phoneEl = document.getElementById('custPhone');
      const phone = phoneEl ? phoneEl.value.trim() : '';
      const code = input ? input.value.trim().toUpperCase() : '';
      const isAr = currentLang === 'ar';

      if (!code) return;

      if (!phone) {
        if (feedback) {
          feedback.className = 'coupon-feedback err';
          feedback.textContent = isAr ? 'أدخل رقم هاتفك أولاً للتحقق من أهلية الخصم' : 'Enter your phone first to verify code eligibility';
          feedback.style.display = 'block';
        }
        return;
      }

      if (code === 'ZEMA10') {
        activePromo = { code: 'ZEMA10', rate: 0.1 };
        if (feedback) {
          feedback.className = 'coupon-feedback ok';
          feedback.textContent = isAr ? '✓ تم تطبيق خصم 10%' : '✓ Applied 10% discount';
          feedback.style.display = 'block';
        }
        renderDrawerCheckout();
      } else {
        activePromo = null;
        if (feedback) {
          feedback.className = 'coupon-feedback err';
          feedback.textContent = isAr ? 'كود الخصم غير صالح' : 'Invalid discount code';
          feedback.style.display = 'block';
        }
        renderDrawerCheckout();
      }
    }

    function toggleDrawerPasswordInput() {
      const chk = document.getElementById('drawerAccountChk');
      const box = document.getElementById('drawerPasswordContainer');
      if (box && chk) box.style.display = chk.checked ? 'block' : 'none';
    }

    function handleDrawerCheckoutSubmit(e) {
      e.preventDefault();
      const isAr = currentLang === 'ar';
      const name = document.getElementById('custName').value.trim();
      const phone = document.getElementById('custPhone').value.trim();
      const gov = document.getElementById('custGov').value;
      const city = document.getElementById('custCity').value.trim();
      const address = document.getElementById('custAddress').value.trim();
      const email = document.getElementById('custEmail').value.trim();

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

      // Show Thank You Step
      goToThankYouStep(orderData);
    }

    // Hash router handler
    window.addEventListener('hashchange', () => {
      const h = window.location.hash;
      if (h === '#cart') {
        openUnifiedDrawer('cart');
      } else if (h === '#checkout') {
        openUnifiedDrawer('checkout');
      } else if (h === '#thank-you') {
        openUnifiedDrawer('thankyou');
      } else if (h.startsWith('#product-')) {
        const id = h.replace('#product-', '');
        openPDP(id);
      } else if (!h || h === '#' || h === '#top' || h === '#story' || h === '#contact' || h === '#faq') {
        if (!h || h === '#' || h === '#top') showHomePage();
      }
    });

    // Check initial hash on load
    window.addEventListener('DOMContentLoaded', () => {
      const h = window.location.hash;
      if (h === '#cart') openUnifiedDrawer('cart');
      else if (h === '#checkout') openUnifiedDrawer('checkout');
      else if (h === '#thank-you') openUnifiedDrawer('thankyou');
      else if (h.startsWith('#product-')) openPDP(h.replace('#product-', ''));
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
      const tickerMsg = document.getElementById('ticker-msg-1');
      if (tickerMsg) {
        tickerMsg.textContent = isAr ? 'شحن مجاني لكافة محافظات مصر للطلبات فوق 2,500 ج.م' : 'FREE SHIPPING OVER EGP 2,500 ACROSS EGYPT';
      }

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

    // Newsletter Form Submission Handler
    function handleNewsletterSubmit(form) {
      const input = form.querySelector('input[type="email"]');
      const successBox = document.getElementById('newsletterSuccess');
      if (input && input.value) {
        if (successBox) successBox.style.display = 'block';
        form.style.display = 'none';
      }
    }

    // Init
    updateCartUI();
    updateWishlistBadge();
    try {
      if (window.lucide && typeof lucide.createIcons === 'function') {
        lucide.createIcons();
      }
    } catch (e) {
      console.warn('Lucide icon init note:', e);
    }
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
