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
  /* 🛍️ 3. SLIDE-OVER CART & PREVIOUS PROJECT CHECKOUT WORKFLOW */
  /* ========================================================== */
  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.55);
    backdrop-filter: blur(4px);
    z-index: 99998;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
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
    max-width: 440px;
    background: #ffffff;
    z-index: 99999;
    box-shadow: -4px 0 28px rgba(0, 0, 0, 0.18);
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

  .drawer-header {
    padding: 18px 22px;
    border-bottom: 1px solid #f0eee9;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #ffffff;
  }
  .drawer-header h3 {
    margin: 0;
    font-size: 17px;
    font-weight: 800;
  }
  .drawer-close-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 6px;
    color: #777;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .drawer-close-btn:hover {
    background: #f4f2ee;
    color: #000;
  }

  .drawer-body {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  /* Reservation Timer Banner (Previous Project) */
  .cart-timer-box {
    background: #fff8eb;
    border: 1px solid #fde68a;
    color: #92400e;
    padding: 10px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* Free Shipping Meter: EGP 2,500 Target */
  .shipping-progress-box {
    background: #f8f6f0;
    padding: 14px 16px;
    border-radius: 8px;
    font-size: 13px;
    color: #444;
  }
  .shipping-bar-bg {
    width: 100%;
    height: 7px;
    background: #e5e0d4;
    border-radius: 4px;
    margin-top: 8px;
    overflow: hidden;
  }
  .shipping-bar-fill {
    height: 100%;
    background: var(--zema-green);
    border-radius: 4px;
    transition: width 0.35s ease;
  }

  /* Cart Item Row */
  .cart-item-row {
    display: flex;
    gap: 14px;
    padding-bottom: 14px;
    border-bottom: 1px solid #f2efe9;
  }
  .cart-item-img {
    width: 76px;
    height: 94px;
    object-fit: cover;
    border-radius: 6px;
    background: #f4f2ee;
  }
  .cart-item-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .cart-item-title {
    font-size: 14px;
    font-weight: 700;
    margin: 0 0 2px 0;
  }
  .cart-item-sku {
    font-size: 11px;
    color: #888;
    margin-bottom: 4px;
    font-family: monospace;
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
    border: 1px solid #e2ded5;
    border-radius: 4px;
    background: #faf9f6;
  }
  .qty-btn {
    background: none;
    border: none;
    width: 28px;
    height: 28px;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .qty-btn:hover { background: #eeebe3; }
  .qty-num {
    padding: 0 8px;
    font-size: 13px;
    font-weight: 700;
  }

  .drawer-footer {
    padding: 18px 22px;
    border-top: 1px solid #f0eee9;
    background: #faf9f6;
  }
  .summary-row {
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    margin-bottom: 8px;
    color: #666;
  }
  .summary-row.total {
    font-size: 17px;
    font-weight: 800;
    color: var(--zema-espresso);
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px dashed #dedbd4;
  }

  .btn-checkout-primary {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    padding: 14px;
    background: var(--zema-espresso);
    color: #ffffff;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 800;
    cursor: pointer;
    border: none;
    margin-bottom: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    transition: background 0.2s, transform 0.15s;
  }
  .btn-checkout-primary:hover {
    background: #383533;
    transform: translateY(-1px);
  }

  .btn-wa-checkout {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    padding: 12px;
    background: #25D366;
    color: #ffffff;
    text-decoration: none;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    border: none;
    transition: background 0.2s;
  }
  .btn-wa-checkout:hover {
    background: #20ba59;
  }

  /* ========================================================== */
  /* 🇪🇬 CHECKOUT MODAL & EXACT PREVIOUS WORKFLOW */
  /* ========================================================== */
  .checkout-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.95);
    width: 94%;
    max-width: 580px;
    max-height: 92vh;
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 16px 48px rgba(0,0,0,0.28);
    z-index: 100000;
    overflow-y: auto;
    opacity: 0;
    pointer-events: none;
    transition: all 0.25s ease;
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
    position: sticky;
    top: 0;
    background: #ffffff;
    z-index: 10;
  }
  .checkout-eyebrow {
    font-size: 10px;
    letter-spacing: 0.1em;
    color: var(--zema-gold);
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 2px;
  }
  .checkout-header h3 {
    margin: 0;
    font-size: 18px;
    font-weight: 800;
  }
  .checkout-body {
    padding: 22px 24px;
  }

  /* Live Checkout Order Summary Box (Previous Project) */
  .co-summary-box {
    background: #faf9f6;
    border: 1px solid #eae6de;
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 20px;
  }
  .co-summary-line {
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: #555;
    margin-bottom: 6px;
  }
  .co-summary-line.highlight {
    color: #1b7d3f;
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

  /* Coupon Code Section (Previous Project) */
  .coupon-row {
    display: flex;
    gap: 8px;
    margin-top: 12px;
    padding-top: 12px;
    border-top: 1px solid #eae6de;
  }
  .coupon-input {
    flex: 1;
    padding: 8px 12px;
    border: 1px solid #dcd7ce;
    border-radius: 6px;
    font-size: 13px;
    background: #ffffff;
  }
  .coupon-btn {
    padding: 8px 16px;
    background: #222;
    color: #fff;
    border: none;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
  }
  .coupon-btn:hover {
    background: #444;
  }
  .coupon-feedback {
    font-size: 11px;
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
  .form-control.input-error {
    border-color: #dc2626;
  }
  .field-error-msg {
    color: #dc2626;
    font-size: 11px;
    margin-top: 4px;
  }

  /* Payment Methods Selection (Previous Project) */
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
    color: #777;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0 6px;
  }
  .payment-option-card {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 12px;
    border: 1px solid #e5e0d4;
    border-radius: 8px;
    margin-top: 8px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .payment-option-card.active {
    border: 2px solid #b45309;
    background: #fef3c7;
    box-shadow: 0 2px 8px rgba(180, 83, 9, 0.15);
  }
  .payment-option-card.disabled {
    opacity: 0.55;
    cursor: not-allowed;
    background: #faf9f6;
  }
  .payment-badge-soon {
    font-size: 10px;
    background: #eee;
    color: #666;
    padding: 2px 6px;
    border-radius: 4px;
    margin-left: auto;
  }
  [dir="rtl"] .payment-badge-soon {
    margin-left: 0;
    margin-right: auto;
  }

  /* Account Creation Option Box */
  .account-toggle-box {
    background: #faf9f6;
    border: 1px solid #eae6de;
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 16px;
  }

  /* Guarantee / Note Badge */
  .guarantee-note-box {
    font-size: 11px;
    color: #666;
    text-align: center;
    line-height: 1.5;
    padding-top: 10px;
    border-top: 1px solid #f0eee9;
    margin-top: 12px;
  }

  /* Order Success View (Previous Project) */
  .order-success-card {
    text-align: center;
    padding: 28px 16px;
  }
  .success-check-icon {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: #dcfce7;
    color: #16a34a;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 14px auto;
  }
  .order-number-badge {
    display: inline-block;
    padding: 6px 18px;
    background: #f4f2ee;
    border: 1px dashed #c5a059;
    border-radius: 20px;
    font-weight: 800;
    font-size: 15px;
    color: var(--zema-espresso);
    margin: 12px 0 16px 0;
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
        <button class="icon-btn" aria-label="Shopping bag" onclick="toggleCartDrawer(true)">
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
      <a href="#contact" onclick="toggleCartDrawer(true)">سلة المشتريات</a>
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
  <!-- 🛍️ 3. SLIDE-OVER CART (EXACT PREVIOUS PROJECT WORKFLOW) -->
  <!-- ========================================================== -->
  <div class="modal-overlay" id="cartOverlay" onclick="toggleCartDrawer(false)"></div>
  <aside class="drawer-panel" id="cartDrawer" aria-label="Shopping Cart">
    <div class="drawer-header">
      <div>
        <p class="checkout-eyebrow" id="cart-eyebrow-text">YOUR CART</p>
        <h3 id="cart-drawer-title">حقيبة التسوق (<span id="cartTotalItems">0</span>)</h3>
      </div>
      <button class="drawer-close-btn" onclick="toggleCartDrawer(false)" aria-label="Close cart"><i data-lucide="x"></i></button>
    </div>
    
    <div class="drawer-body" id="cartItemsContainer">
      <!-- ⏱ Reservation Timer Banner (Previous Project) -->
      <div class="cart-timer-box" id="cartTimerBox">
        <i data-lucide="clock" style="width:16px;height:16px;"></i>
        <span id="cartTimerText">⏱ القطع محجوزة في سلتك لمدة 15:00 دقيقة</span>
      </div>

      <!-- 🚚 2,500 EGP Shipping Progress Bar -->
      <div class="shipping-progress-box" id="freeShippingNotice">
        <div id="shippingStatusText">🚚 تبقى لك <strong>2,500 ج.م</strong> للحصول على شحن مجاني!</div>
        <div class="shipping-bar-bg">
          <div class="shipping-bar-fill" id="shippingBarFill" style="width: 0%;"></div>
        </div>
      </div>

      <div id="cartItemsList">
        <!-- Rendered dynamically -->
      </div>
    </div>

    <div class="drawer-footer">
      <div class="summary-row">
        <span id="label-cart-subtotal">المجموع الفرعي:</span>
        <span id="cartSubtotal">0.00 ج.م</span>
      </div>
      <div class="summary-row total">
        <span id="label-cart-total">الإجمالي:</span>
        <span id="cartTotalPrice">0.00 ج.م</span>
      </div>
      
      <!-- Primary Action: Proceed to Checkout (Previous Project) -->
      <button class="btn-checkout-primary" onclick="openCheckoutModal()">
        <i data-lucide="check-circle-2"></i>
        <span id="btn-proceed-checkout-text">إتمام الطلب (الدفع عند الاستلام)</span>
      </button>

      <!-- Secondary Action: WhatsApp Direct Order (Previous Project) -->
      <a id="checkoutWhatsappBtn" href="#" target="_blank" class="btn-wa-checkout">
        <i data-lucide="message-circle"></i>
        <span id="btn-wa-quick-text">اطلب سريعاً عبر واتساب</span>
      </a>

      <p class="guarantee-note-box" id="cart-guarantee-note">
        🛡️ الدفع عند الاستلام متاح — حقك في الاستبدال أو الاسترجاع مكفول خلال ١٤ يوماً.
      </p>
    </div>
  </aside>

  <!-- ========================================================== -->
  <!-- 🇪🇬 4. CHECKOUT MODAL & WORKFLOW (EXACT PREVIOUS PROJECT) -->
  <!-- ========================================================== -->
  <div class="modal-overlay" id="checkoutOverlay" onclick="toggleCheckoutModal(false)"></div>
  <div class="checkout-modal" id="checkoutModal" aria-label="Checkout Dialog">
    <div class="checkout-header">
      <div>
        <p class="checkout-eyebrow" id="co-header-eyebrow">CHECKOUT</p>
        <h3 id="checkoutModalTitle">اطلب الآن — الدفع عند الاستلام</h3>
      </div>
      <button class="drawer-close-btn" onclick="toggleCheckoutModal(false)" aria-label="Close checkout"><i data-lucide="x"></i></button>
    </div>

    <!-- Form State -->
    <div class="checkout-body" id="checkoutFormState">
      <!-- Order Summary Card (Previous Project) -->
      <div class="co-summary-box">
        <div class="co-summary-line">
          <span id="co-sum-subtotal-lbl">المجموع الفرعي:</span>
          <span id="coSumSubtotal">0 ج.م</span>
        </div>
        <div class="co-summary-line highlight" id="coDiscountRow" style="display:none;">
          <span id="coDiscountLabel">خصم (ZEMA10):</span>
          <span id="coDiscountAmount">-0 ج.م</span>
        </div>
        <div class="co-summary-line">
          <span id="co-sum-shipping-lbl">الشحن:</span>
          <span id="coSumShipping">اختر المحافظة لحساب الشحن</span>
        </div>
        <div class="co-summary-total">
          <span id="co-sum-total-lbl">الإجمالي:</span>
          <span id="coSumTotal">0 ج.م</span>
        </div>

        <!-- Promo Code Input (Previous Project) -->
        <div class="coupon-row">
          <input type="text" id="couponCodeInput" class="coupon-input" placeholder="كود الخصم (مثال: ZEMA10)" />
          <button type="button" class="coupon-btn" onclick="applyPromoCode()">تطبيق</button>
        </div>
        <div id="couponFeedback" class="coupon-feedback" style="display:none;"></div>
      </div>

      <!-- Checkout Form with previous project fields & validation -->
      <form id="egyptCheckoutForm" onsubmit="handleCheckoutSubmit(event)">
        <!-- 1. Full Name -->
        <div class="form-group">
          <label id="lbl-co-name">الاسم بالكامل *</label>
          <input type="text" id="custName" class="form-control" placeholder="مثال: ياسمين أحمد" required minlength="3" maxlength="80" />
        </div>

        <!-- 2. Egyptian Phone with Regex -->
        <div class="form-group">
          <label id="lbl-co-phone">رقم الهاتف (مثال: 01012345678) *</label>
          <input type="tel" id="custPhone" class="form-control" placeholder="01012345678" dir="ltr" inputmode="numeric" required oninput="validatePhoneLive()" />
          <div id="phoneErrorMsg" class="field-error-msg" style="display:none;">رقم غير صحيح. يبدأ بـ 01 و11 رقم.</div>
        </div>

        <!-- 3. Governorate with Dynamic Shipping -->
        <div class="form-group">
          <label id="lbl-co-gov">المحافظة *</label>
          <select id="custGov" class="form-control" required onchange="onGovernorateChange()">
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

        <!-- 4. City / Area (Optional) -->
        <div class="form-group">
          <label id="lbl-co-city">المدينة / المنطقة (اختياري)</label>
          <input type="text" id="custCity" class="form-control" placeholder="مثال: مدينة نصر / التجمع / سموحة" maxlength="80" />
        </div>

        <!-- 5. Detailed Address -->
        <div class="form-group">
          <label id="lbl-co-address">العنوان بالتفصيل *</label>
          <textarea id="custAddress" class="form-control" rows="2" placeholder="المنطقة، الشارع، رقم العقار، الشقة أو العلامة المميزة" required minlength="8" maxlength="300"></textarea>
        </div>

        <!-- 6. Email (Optional) -->
        <div class="form-group">
          <label id="lbl-co-email">البريد الإلكتروني (اختياري)</label>
          <input type="email" id="custEmail" class="form-control" placeholder="name@example.com" dir="ltr" />
        </div>

        <!-- 7. Optional Account Creation (Previous Project) -->
        <div class="account-toggle-box">
          <label style="display:flex; align-items:center; gap:8px; font-size:12px; cursor:pointer; font-weight:600;">
            <input type="checkbox" id="createAccountCheckbox" onchange="toggleAccountPasswordInput()" />
            <span id="lbl-create-account">أنشئ حساباً لحفظ طلبي (اختياري)</span>
          </label>
          <div id="passwordInputContainer" style="display:none; margin-top:8px;">
            <input type="password" id="accountPassword" class="form-control" placeholder="كلمة المرور (٦ أحرف على الأقل)" minlength="6" />
          </div>
          <p style="font-size:11px; color:#888; margin:4px 0 0 0;" id="lbl-guest-note">يمكنك إتمام الطلب كضيف بدون تسجيل.</p>
        </div>

        <!-- 8. Payment Method Selection Fieldset (Previous Project) -->
        <div class="payment-methods-fieldset">
          <div class="payment-legend" id="lbl-pay-title">طريقة الدفع</div>
          
          <!-- COD: Active -->
          <label class="payment-option-card active" id="payOptCod">
            <input type="radio" name="payMethod" value="cod" checked />
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

        <!-- Submit Button -->
        <button type="submit" class="btn-checkout-primary" id="btnSubmitOrder" style="padding:15px; font-size:15px; margin-bottom:6px;">
          <i data-lucide="check"></i>
          <span id="btnSubmitOrderText">تأكيد الطلب</span>
        </button>

        <p style="font-size:11px; color:#777; text-align:center; margin-bottom:12px;" id="lbl-delivery-note">
          توصيل سريع خلال ٢ - ٤ أيام عمل لجميع المحافظات
        </p>

        <!-- Quick WhatsApp Order (Previous Project) -->
        <a id="checkoutModalWaBtn" href="#" target="_blank" class="btn-wa-checkout" style="margin-bottom:12px;">
          <i data-lucide="message-circle"></i>
          <span id="lbl-co-wa-quick">اطلب سريعاً عبر واتساب</span>
        </a>

        <!-- Guarantee Note -->
        <p class="guarantee-note-box" id="lbl-co-guarantee">
          🛡️ الدفع عند الاستلام متاح — حقك في الاستبدال أو الاسترجاع مكفول خلال ١٤ يوماً.
        </p>
      </form>
    </div>

    <!-- Thank You / Order Confirmed State (Exact Previous Project) -->
    <div class="checkout-body" id="checkoutSuccessState" style="display:none;">
      <div class="order-success-card">
        <div class="success-check-icon">
          <i data-lucide="check" style="width:36px;height:36px;"></i>
        </div>
        <p class="checkout-eyebrow" id="ty-eyebrow-text">ORDER CONFIRMED</p>
        <h2 style="font-size:22px; font-weight:800; margin:0;" id="ty-title-text">شكراً لثقتك في زِيما</h2>
        <p style="font-size:13px; color:#666; margin:8px 0 14px 0;" id="ty-body-text">
          تم تسجيل طلبك بنجاح! سيقوم فريق خدمة العملاء بالتواصل معك عبر الهاتف خلال ٢٤ ساعة لتأكيد تفاصيل الشحن والتسليم.
        </p>
        
        <div class="order-number-badge" id="successOrderNumber">رقم الطلب: #ZM260925-1001</div>

        <div style="background:#faf9f6; border:1px solid #eee; border-radius:10px; padding:16px; text-align:start; font-size:13px; line-height:1.8; margin-bottom:18px;">
          <div><strong id="ty-lbl-name">الاسم:</strong> <span id="successCustName">--</span></div>
          <div><strong id="ty-lbl-phone">الهاتف:</strong> <span id="successCustPhone">--</span></div>
          <div><strong id="ty-lbl-addr">العنوان:</strong> <span id="successCustAddress">--</span></div>
          <div><strong id="ty-lbl-pay">طريقة الدفع:</strong> <span id="successCustPayment">الدفع عند الاستلام</span></div>
          <div><strong id="ty-lbl-total">الإجمالي المطلوب:</strong> <strong style="color:var(--zema-espresso);" id="successCustTotal">--</strong></div>
          <div><strong id="ty-lbl-time">موعد التوصيل:</strong> <span style="color:#1b7d3f; font-weight:700;">خلال 24 - 48 ساعة</span></div>
        </div>

        <a id="successWaNotifyBtn" href="#" target="_blank" class="btn-wa-checkout" style="margin-bottom:10px;">
          <i data-lucide="message-circle"></i>
          <span>إرسال تفاصيل الطلب عبر واتساب للتأكيد الفوري</span>
        </a>

        <div style="display:flex; gap:8px;">
          <button class="card-quick-add-btn" style="flex:1;" onclick="toggleCheckoutModal(false); toggleAccountModal(true);">
            <i data-lucide="truck" style="width:14px;height:14px;display:inline;margin-right:4px;"></i>
            <span id="ty-btn-track">تتبع شحنتك</span>
          </button>
          <button class="card-quick-add-btn" style="flex:1;" onclick="toggleCheckoutModal(false); showHomePage();">
            <span id="ty-btn-back">العودة للمتجر</span>
          </button>
        </div>
      </div>
    </div>
  </div>

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
    // 🛍️ 3. CART COMPONENT (PREVIOUS PROJECT LOGIC)
    // ==========================================
    let activeCoupon = null; // { code: 'ZEMA10', rate: 0.1 }

    function toggleCartDrawer(open) {
      const overlay = document.getElementById('cartOverlay');
      const drawer = document.getElementById('cartDrawer');
      if (open) {
        overlay.classList.add('open');
        drawer.classList.add('open');
        updateCartUI();
      } else {
        overlay.classList.remove('open');
        drawer.classList.remove('open');
      }
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
      updateCartUI();
      toggleCartDrawer(true);
    }

    function changeCartItemQty(id, delta) {
      const item = cart.find(i => i.id === id);
      if (!item) return;
      item.qty += delta;
      if (item.qty <= 0) {
        cart = cart.filter(i => i.id !== id);
      }
      saveCart();
      updateCartUI();
    }

    function saveCart() {
      localStorage.setItem('zema_cart', JSON.stringify(cart));
    }

    function updateCartUI() {
      const countBadge = document.getElementById('cartCountBadge');
      const totalItemsSpan = document.getElementById('cartTotalItems');
      const listContainer = document.getElementById('cartItemsList');
      const subtotalEl = document.getElementById('cartSubtotal');
      const totalPriceEl = document.getElementById('cartTotalPrice');
      const checkoutWaBtn = document.getElementById('checkoutWhatsappBtn');
      const shippingNotice = document.getElementById('shippingStatusText');
      const barFill = document.getElementById('shippingBarFill');

      const isAr = currentLang === 'ar';
      const totalItems = cart.reduce((sum, i) => sum + i.qty, 0);
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);

      countBadge.textContent = totalItems;
      totalItemsSpan.textContent = totalItems;
      subtotalEl.textContent = subtotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      totalPriceEl.textContent = subtotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      // 🚚 2,500 EGP Free Shipping Threshold Meter
      const threshold = 2500;
      const progress = Math.min(100, Math.round((subtotal / threshold) * 100));
      barFill.style.width = progress + '%';
      
      if (subtotal >= threshold) {
        shippingNotice.innerHTML = '🎉 <strong>' + (isAr ? 'مبروك! طلبك مؤهل للشحن المجاني لكافة المحافظات!' : 'Congratulations! You unlocked FREE shipping across Egypt!') + '</strong>';
        barFill.style.background = '#1b7d3f';
      } else {
        const remaining = threshold - subtotal;
        shippingNotice.innerHTML = '🚚 ' + (isAr ? 'أضف منتجات بقيمة <strong>' + remaining.toLocaleString() + ' ج.م</strong> للحصول على شحن مجاني!' : 'Add products worth <strong>' + remaining.toLocaleString() + ' EGP</strong> more for FREE shipping!');
        barFill.style.background = '#C5A059';
      }

      // Empty Cart View (Previous Project style)
      if (cart.length === 0) {
        listContainer.innerHTML = `
          <div style="text-align:center; padding: 45px 10px; color:#888;">
            <i data-lucide="shopping-bag" style="width:48px;height:48px;margin: 0 auto 12px auto; opacity:0.3;"></i>
            <p style="margin-bottom:14px;">${isAr ? 'سلتك فارغة حالياً.' : 'Your cart is empty.'}</p>
            <button class="card-quick-add-btn" style="width:auto; padding:10px 22px; margin:0 auto;" onclick="toggleCartDrawer(false);">
              ${isAr ? 'ابدأ التسوق' : 'Start Shopping'}
            </button>
          </div>
        `;
      } else {
        let html = '';
        let waText = (isAr ? 'مرحباً ZEMA، أرغب في طلب المنتجات التالية:%0A' : 'Hello ZEMA, I want to place this order:%0A');

        cart.forEach(item => {
          const title = isAr ? item.nameAr : item.nameEn;
          const lineTotal = item.price * item.qty;
          waText += `• ${title} (${item.qty}x) = ${lineTotal} EGP%0A`;
          html += `
            <div class="cart-item-row">
              <img src="${item.img}" class="cart-item-img" alt="${title}" />
              <div class="cart-item-info">
                <div>
                  <h4 class="cart-item-title">${title}</h4>
                  <div class="cart-item-sku">${item.sku || 'ZM-BAG'}</div>
                  <div class="cart-item-price">${lineTotal.toLocaleString()} ${isAr ? 'ج.م' : 'EGP'}</div>
                </div>
                <div class="cart-qty-row">
                  <div class="qty-box">
                    <button class="qty-btn" onclick="changeCartItemQty('${item.id}', -1)" aria-label="-">-</button>
                    <span class="qty-num">${item.qty}</span>
                    <button class="qty-btn" onclick="changeCartItemQty('${item.id}', 1)" aria-label="+">+</button>
                  </div>
                  <button onclick="changeCartItemQty('${item.id}', -999)" style="background:none; border:none; cursor:pointer; color:#dc2626; font-size:12px; display:flex; align-items:center; gap:3px;" title="${isAr ? 'حذف' : 'Remove'}">
                    <i data-lucide="trash-2" style="width:14px;height:14px;"></i>
                    <span>${isAr ? 'حذف' : 'Remove'}</span>
                  </button>
                </div>
              </div>
            </div>
          `;
        });

        waText += `%0A*الإجمالي المطلوب:* ${subtotal} EGP%0A*طريقة الدفع:* الدفع عند الاستلام`;
        checkoutWaBtn.href = 'https://wa.me/201032117373?text=' + waText;
        listContainer.innerHTML = html;
      }
      lucide.createIcons();
    }

    // ==========================================
    // 🇪🇬 4. CHECKOUT WORKFLOW & EXACT BEHAVIOR
    // ==========================================
    function openCheckoutModal() {
      if (cart.length === 0) {
        alert(currentLang === 'ar' ? 'سلتك فارغة حالياً.' : 'Your cart is empty.');
        return;
      }
      toggleCartDrawer(false);
      document.getElementById('checkoutFormState').style.display = 'block';
      document.getElementById('checkoutSuccessState').style.display = 'none';
      updateCheckoutSummary();
      toggleCheckoutModal(true);
    }

    function toggleCheckoutModal(open) {
      const overlay = document.getElementById('checkoutOverlay');
      const modal = document.getElementById('checkoutModal');
      if (open) {
        overlay.classList.add('open');
        modal.classList.add('open');
      } else {
        overlay.classList.remove('open');
        modal.classList.remove('open');
      }
    }

    function calculateShippingFee(subtotal, gov) {
      if (subtotal >= 2500) return 0; // Free shipping threshold
      if (!gov) return null;
      if (gov === 'القاهرة' || gov === 'الجيزة') return 50;
      return 65; // Nationwide delivery
    }

    function updateCheckoutSummary() {
      const isAr = currentLang === 'ar';
      const subtotal = cart.reduce((sum, i) => sum + (i.price * i.qty), 0);
      const gov = document.getElementById('custGov').value;
      const shippingFee = calculateShippingFee(subtotal, gov);

      // Discount
      let discountAmount = 0;
      if (activeCoupon) {
        discountAmount = Math.round(subtotal * activeCoupon.rate);
      }

      // Display Subtotal
      document.getElementById('coSumSubtotal').textContent = subtotal.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      // Display Discount Row
      const discRow = document.getElementById('coDiscountRow');
      if (discountAmount > 0) {
        discRow.style.display = 'flex';
        document.getElementById('coDiscountLabel').textContent = (isAr ? 'خصم ' : 'Discount ') + `(${activeCoupon.code}):`;
        document.getElementById('coDiscountAmount').textContent = '- ' + discountAmount.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      } else {
        discRow.style.display = 'none';
      }

      // Display Shipping
      const shippingEl = document.getElementById('coSumShipping');
      if (shippingFee === 0) {
        shippingEl.innerHTML = '<span style="color:#16a34a; font-weight:bold;">' + (isAr ? 'مجاني 🎉' : 'Free 🎉') + '</span>';
      } else if (shippingFee !== null) {
        shippingEl.textContent = shippingFee + (isAr ? ' ج.م' : ' EGP');
      } else {
        shippingEl.textContent = isAr ? 'اختر المحافظة لحساب الشحن' : 'Select governorate to calculate shipping';
      }

      // Total
      const activeShipping = shippingFee !== null ? shippingFee : 0;
      const total = Math.max(0, subtotal - discountAmount + activeShipping);
      document.getElementById('coSumTotal').textContent = total.toLocaleString() + (isAr ? ' ج.م' : ' EGP');
      document.getElementById('btnSubmitOrderText').textContent = (isAr ? 'تأكيد الطلب — ' : 'Confirm Order — ') + total.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      // Quick WhatsApp link in checkout modal
      let waText = (isAr ? 'أهلاً زِيما، أريد استكمال طلبي.. تفاصيلي هي:%0A' : 'Hi ZEMA, I want to place this order:%0A');
      cart.forEach(i => {
        waText += `• ${isAr ? i.nameAr : i.nameEn} × ${i.qty} = ${i.price * i.qty} EGP%0A`;
      });
      waText += `%0Aالإجمالي: ${total} EGP%0Aطريقة الدفع: الدفع عند الاستلام`;
      document.getElementById('checkoutModalWaBtn').href = 'https://wa.me/201032117373?text=' + waText;
    }

    function onGovernorateChange() {
      updateCheckoutSummary();
    }

    function validatePhoneLive() {
      const phoneInput = document.getElementById('custPhone');
      const errBox = document.getElementById('phoneErrorMsg');
      const cleanPhone = phoneInput.value.replace(/\\D/g, '');
      phoneInput.value = cleanPhone;
      
      const isEgyptianPhone = /^01[0125][0-9]{8}$/.test(cleanPhone);
      if (cleanPhone.length > 0 && !isEgyptianPhone) {
        phoneInput.classList.add('input-error');
        errBox.style.display = 'block';
        return false;
      } else {
        phoneInput.classList.remove('input-error');
        errBox.style.display = 'none';
        return isEgyptianPhone;
      }
    }

    function applyPromoCode() {
      const codeInput = document.getElementById('couponCodeInput');
      const feedback = document.getElementById('couponFeedback');
      const phoneInput = document.getElementById('custPhone').value.trim();
      const code = codeInput.value.trim().toUpperCase();
      const isAr = currentLang === 'ar';

      if (!code) return;

      if (!phoneInput) {
        feedback.className = 'coupon-feedback err';
        feedback.textContent = isAr ? 'أدخل رقم هاتفك أولاً للتحقق من أهلية الخصم' : 'Enter your phone first to verify code eligibility';
        feedback.style.display = 'block';
        return;
      }

      if (code === 'ZEMA10') {
        activeCoupon = { code: 'ZEMA10', rate: 0.1 };
        feedback.className = 'coupon-feedback ok';
        feedback.textContent = isAr ? '✓ تم تطبيق خصم 10%' : '✓ Applied 10% discount';
        feedback.style.display = 'block';
        updateCheckoutSummary();
      } else {
        activeCoupon = null;
        feedback.className = 'coupon-feedback err';
        feedback.textContent = isAr ? 'كود الخصم غير صالح' : 'Invalid discount code';
        feedback.style.display = 'block';
        updateCheckoutSummary();
      }
    }

    function toggleAccountPasswordInput() {
      const chk = document.getElementById('createAccountCheckbox');
      const container = document.getElementById('passwordInputContainer');
      container.style.display = chk.checked ? 'block' : 'none';
    }

    function handleCheckoutSubmit(e) {
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
      const shippingFee = calculateShippingFee(subtotal, gov) || 0;
      let discountAmount = 0;
      if (activeCoupon) discountAmount = Math.round(subtotal * activeCoupon.rate);
      const totalAmount = Math.max(0, subtotal - discountAmount + shippingFee);

      // Generate exact Order Number format from previous project: ZM + YYMMDD + '-' + 4 digits
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
        shipping: shippingFee,
        total: totalAmount,
        payment_method: 'Cash on Delivery',
        created_at: new Date().toISOString()
      };

      // Save to localStorage (previous project requirement)
      try {
        const storedOrders = JSON.parse(localStorage.getItem('zema_orders') || '[]');
        storedOrders.unshift(orderData);
        localStorage.setItem('zema_orders', JSON.stringify(storedOrders));
      } catch (err) {
        console.warn('Could not save order locally:', err);
      }

      // Populate Success State
      document.getElementById('successOrderNumber').textContent = (isAr ? 'رقم الطلب: #' : 'Order ID: #') + orderNumber;
      document.getElementById('successCustName').textContent = name;
      document.getElementById('successCustPhone').textContent = phone;
      document.getElementById('successCustAddress').textContent = gov + (city ? ' - ' + city : '') + ' - ' + address;
      document.getElementById('successCustTotal').textContent = totalAmount.toLocaleString() + (isAr ? ' ج.م' : ' EGP');

      // WhatsApp Notification Link
      let waConfirmText = (isAr ? '🔔 *طلب جديد في متجر ZEMA!*%0A━━━━━━━━━━━━━━━%0A' : '🔔 *New Order at ZEMA!*%0A━━━━━━━━━━━━━━━%0A');
      waConfirmText += `📋 *${isAr ? 'رقم الطلب' : 'Order ID'}:* ${orderNumber}%0A`;
      waConfirmText += `👤 *${isAr ? 'العميل' : 'Customer'}:* ${name}%0A`;
      waConfirmText += `📱 *${isAr ? 'الهاتف' : 'Phone'}:* ${phone}%0A`;
      waConfirmText += `📍 *${isAr ? 'المحافظة' : 'Governorate'}:* ${gov}%0A`;
      waConfirmText += `🏠 *${isAr ? 'العنوان' : 'Address'}:* ${city ? city + ' - ' : ''}${address}%0A`;
      waConfirmText += `📦 *${isAr ? 'المنتجات' : 'Items'}:*%0A`;
      cart.forEach(i => {
        waConfirmText += `• ${isAr ? i.nameAr : i.nameEn} (${i.qty}x) - ${(i.price * i.qty).toLocaleString()} EGP%0A`;
      });
      waConfirmText += `━━━━━━━━━━━━━━━%0A💰 *${isAr ? 'الإجمالي المطلوب' : 'Total'}:* ${totalAmount.toLocaleString()} EGP (${isAr ? 'شامل الشحن' : 'incl. shipping'})%0A`;
      waConfirmText += `💳 *${isAr ? 'طريقة الدفع' : 'Payment'}:* ${isAr ? 'الدفع عند الاستلام' : 'Cash on Delivery'}`;

      document.getElementById('successWaNotifyBtn').href = 'https://wa.me/201032117373?text=' + waConfirmText;

      // Clear Cart
      cart = [];
      saveCart();
      updateCartUI();

      // Show Success State
      document.getElementById('checkoutFormState').style.display = 'none';
      document.getElementById('checkoutSuccessState').style.display = 'block';
      lucide.createIcons();
    }

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
      toggleCartDrawer(true);
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
