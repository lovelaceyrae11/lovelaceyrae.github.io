<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Castleberry Geometric Framework | Consciousness-Matter Interface</title>
    <meta name="description" content="Novel mathematical structures for consciousness-matter interfaces using golden ratio geometry. Open science, premium implementation.">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1d3e 50%, #2a2d4e 100%);
            color: #e0e0e0;
            line-height: 1.6;
            overflow-x: hidden;
        }

        .phi-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.1;
        }

        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(10, 14, 39, 0.95);
            backdrop-filter: blur(10px);
            padding: 1rem 5%;
            z-index: 1000;
            box-shadow: 0 2px 20px rgba(255, 215, 0, 0.1);
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 3rem;
            flex-wrap: wrap;
        }

        nav a {
            color: #ffd700;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
            position: relative;
        }

        nav a:hover {
            color: #fff;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.8);
        }

        nav a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, #ffd700, #fff);
            transition: width 0.3s;
        }

        nav a:hover::after {
            width: 100%;
        }

        .pricing-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2.5rem;
            margin-top: 3rem;
            max-width: 1300px;
            margin-left: auto;
            margin-right: auto;
        }

        .pricing-card {
            background: rgba(255, 255, 255, 0.03);
            border: 2px solid rgba(255, 215, 0, 0.2);
            border-radius: 20px;
            padding: 2.5rem;
            position: relative;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
        }

        .pricing-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(255, 215, 0, 0.2);
        }

        .builder-tier {
            border-color: #ffd700;
            border-width: 3px;
            background: rgba(255, 215, 0, 0.08);
            transform: scale(1.05);
        }

        .builder-tier:hover {
            transform: scale(1.05) translateY(-10px);
            box-shadow: 0 25px 70px rgba(255, 215, 0, 0.4);
        }

        .tier-badge {
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.1);
            color: #ffd700;
            padding: 0.5rem 1.5rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 1px;
            border: 1px solid rgba(255, 215, 0, 0.3);
        }

        .tier-badge.popular {
            background: linear-gradient(135deg, #ffd700, #ffed4e);
            color: #0a0e27;
            border: none;
            box-shadow: 0 5px 20px rgba(255, 215, 0, 0.4);
        }

        .pricing-card h3 {
            color: #fff;
            font-size: 2rem;
            margin: 1.5rem 0 1rem;
            text-align: center;
        }

        .price {
            font-size: 3.5rem;
            font-weight: 300;
            color: #ffd700;
            text-align: center;
            margin: 1rem 0;
            font-family: 'Courier New', monospace;
        }

        .period {
            font-size: 1.2rem;
            color: #a0a0a0;
            font-weight: 400;
        }

        .tier-description {
            text-align: center;
            color: #a0a0a0;
            margin-bottom: 2rem;
            font-size: 1.1rem;
            min-height: 50px;
        }

        .features-list {
            list-style: none;
            margin: 2rem 0;
            flex-grow: 1;
        }

        .features-list li {
            padding: 0.7rem 0;
            border-bottom: 1px solid rgba(255, 215, 0, 0.1);
            color: #e0e0e0;
            font-size: 1rem;
        }

        .features-list li:last-child {
            border-bottom: none;
        }

        .features-list strong {
            color: #ffd700;
            font-size: 1.1rem;
            display: block;
            margin-bottom: 0.5rem;
        }

        .tier-button {
            width: 100%;
            padding: 1.2rem;
            border: none;
            border-radius: 50px;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: auto;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-decoration: none;
            display: block;
            text-align: center;
        }

        .free-button {
            background: rgba(255, 255, 255, 0.1);
            color: #ffd700;
            border: 2px solid rgba(255, 215, 0, 0.5);
        }

        .free-button:hover {
            background: rgba(255, 215, 0, 0.1);
            border-color: #ffd700;
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(255, 215, 0, 0.2);
        }

        .builder-button {
            background: linear-gradient(135deg, #ffd700, #ffed4e);
            color: #0a0e27;
            box-shadow: 0 5px 25px rgba(255, 215, 0, 0.4);
        }

        .builder-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 35px rgba(255, 215, 0, 0.6);
        }

        .pro-button {
            background: linear-gradient(135deg, #8b7355, #d4af37);
            color: #fff;
            box-shadow: 0 5px 25px rgba(212, 175, 55, 0.3);
        }

        .pro-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 35px rgba(212, 175, 55, 0.5);
        }

        .tier-note {
            text-align: center;
            color: #a0a0a0;
            font-size: 0.9rem;
            margin-top: 1rem;
            font-style: italic;
        }

        .floating-donate {
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 9999;
            animation: pulse 2s ease-in-out infinite;
        }

        .donate-button {
            background: linear-gradient(135deg, #ff6b6b, #ee5a6f);
            color: white;
            padding: 1.2rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.1rem;
            box-shadow: 0 8px 30px rgba(255, 107, 107, 0.4);
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s;
        }

        .donate-button:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 12px 40px rgba(255, 107, 107, 0.6);
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .comparison-table {
            max-width: 1200px;
            margin: 3rem auto;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 15px;
            overflow-x: auto;
        }

        .comparison-table table {
            width: 100%;
            border-collapse: collapse;
        }

        .comparison-table th {
            background: rgba(255, 215, 0, 0.15);
            padding: 1.5rem 1rem;
            font-size: 1.2rem;
            color: #ffd700;
            text-align: center;
        }

        .comparison-table td {
            padding: 1rem;
            text-align: center;
            border-bottom: 1px solid rgba(255, 215, 0, 0.1);
        }

        .comparison-table td:first-child {
            text-align: left;
            font-weight: 600;
            color: #fff;
        }

        .checkmark {
            color: #4ade80;
            font-size: 1.5rem;
        }

        .xmark {
            color: #666;
            font-size: 1.2rem;
        }

        .faq-container {
            max-width: 900px;
            margin: 3rem auto;
        }

        .faq-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 10px;
            margin-bottom: 1rem;
            overflow: hidden;
            transition: all 0.3s;
        }

        .faq-item:hover {
            border-color: #ffd700;
        }

        .faq-question {
            padding: 1.5rem;
            font-size: 1.2rem;
            font-weight: 600;
            color: #ffd700;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            user-select: none;
        }

        .faq-question:hover {
            background: rgba(255, 215, 0, 0.05);
        }

        .faq-answer {
            padding: 0 1.5rem 1.5rem;
            color: #e0e0e0;
            line-height: 1.8;
            font-size: 1.05rem;
        }

        .faq-toggle {
            font-size: 1.5rem;
            transition: transform 0.3s;
        }

        .faq-item.active .faq-toggle {
            transform: rotate(180deg);
        }

        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem auto;
            max-width: 1200px;
        }

        .testimonial-card {
            background: rgba(255, 255, 255, 0.05);
            border-left: 4px solid #ffd700;
            border-radius: 10px;
            padding: 2rem;
            position: relative;
        }

        .testimonial-quote {
            font-size: 3rem;
            color: rgba(255, 215, 0, 0.3);
            position: absolute;
            top: 10px;
            left: 15px;
        }

        .testimonial-text {
            font-style: italic;
            margin: 1rem 0;
            padding-left: 1rem;
            line-height: 1.6;
        }

        .testimonial-author {
            font-weight: 600;
            color: #ffd700;
            margin-top: 1rem;
        }

        .testimonial-role {
            color: #a0a0a0;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .floating-donate {
                bottom: 20px;
                right: 20px;
            }
            .donate-button {
                padding: 1rem 1.5rem;
                font-size: 1rem;
            }
        }

        .pdf-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            z-index: 10000;
            overflow-y: auto;
            padding: 2rem;
        }

        .pdf-modal-content {
            max-width: 1000px;
            margin: 0 auto;
            background: #1a1d3e;
            border-radius: 15px;
            box-shadow: 0 10px 50px rgba(255, 215, 0, 0.3);
        }

        .pdf-modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 2rem;
            border-bottom: 2px solid rgba(255, 215, 0, 0.3);
        }

        .pdf-modal-header h3 {
            color: #ffd700;
            margin: 0;
            font-size: 1.5rem;
        }

        .pdf-close-btn {
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid #ffd700;
            color: #ffd700;
            font-size: 1.5rem;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .pdf-close-btn:hover {
            background: #ffd700;
            color: #0a0e27;
            transform: rotate(90deg);
        }

        .pdf-modal-body {
            padding: 2rem;
            max-height: 80vh;
            overflow-y: auto;
        }

        .pdf-content-viewer {
            background: #f5f5f5;
            border-radius: 10px;
            padding: 1rem;
        }

        .hero {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 2rem;
            position: relative;
        }

        .hero h1 {
            font-size: clamp(2.5rem, 6vw, 5rem);
            background: linear-gradient(135deg, #ffd700 0%, #fff 50%, #ffd700 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
            animation: glow 3s ease-in-out infinite;
        }

        @keyframes glow {
            0%, 100% { filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.3)); }
            50% { filter: drop-shadow(0 0 40px rgba(255, 215, 0, 0.6)); }
        }

        .hero .subtitle {
            font-size: clamp(1.2rem, 2.5vw, 1.8rem);
            color: #a0a0a0;
            margin-bottom: 2rem;
        }

        .phi-value {
            font-size: 4rem;
            color: #ffd700;
            font-weight: 300;
            margin: 2rem 0;
            font-family: 'Courier New', monospace;
        }

        section {
            padding: 6rem 5%;
            max-width: 1400px;
            margin: 0 auto;
        }

        h2 {
            font-size: clamp(2rem, 4vw, 3rem);
            color: #ffd700;
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
        }

        h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 3px;
            background: linear-gradient(90deg, transparent, #ffd700, transparent);
        }

        .framework-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .framework-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 15px;
            padding: 2rem;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .framework-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 215, 0, 0.1), transparent);
            transition: left 0.5s;
        }

        .framework-card:hover::before {
            left: 100%;
        }

        .framework-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 40px rgba(255, 215, 0, 0.3);
            border-color: #ffd700;
        }

        .framework-card h3 {
            color: #ffd700;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .hexagon-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 3rem 0;
            gap: 2rem;
            flex-wrap: wrap;
        }

        .hexagon {
            width: 120px;
            height: 138px;
            position: relative;
            animation: float 3s ease-in-out infinite;
        }

        .hexagon:nth-child(2) { animation-delay: 0.5s; }
        .hexagon:nth-child(3) { animation-delay: 1s; }
        .hexagon:nth-child(4) { animation-delay: 1.5s; }
        .hexagon:nth-child(5) { animation-delay: 2s; }

        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(5deg); }
        }

        .hexagon svg {
            width: 100%;
            height: 100%;
            filter: drop-shadow(0 0 10px rgba(255, 215, 0, 0.5));
        }

        .data-table {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            overflow: hidden;
            margin: 2rem 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid rgba(255, 215, 0, 0.1);
        }

        th {
            background: rgba(255, 215, 0, 0.1);
            color: #ffd700;
            font-weight: 600;
        }

        tr:hover {
            background: rgba(255, 215, 0, 0.05);
        }

        .highlight {
            color: #ffd700;
            font-weight: 600;
        }

        .cta-button {
            display: inline-block;
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #ffd700, #ffed4e);
            color: #0a0e27;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 700;
            transition: all 0.3s;
            box-shadow: 0 5px 20px rgba(255, 215, 0, 0.3);
            margin: 1rem;
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(255, 215, 0, 0.5);
        }

        .formula {
            background: rgba(0, 0, 0, 0.3);
            padding: 1.5rem;
            border-left: 3px solid #ffd700;
            margin: 2rem 0;
            font-family: 'Courier New', monospace;
            border-radius: 5px;
        }

        footer {
            background: rgba(10, 14, 39, 0.95);
            text-align: center;
            padding: 3rem 5%;
            margin-top: 4rem;
            border-top: 1px solid rgba(255, 215, 0, 0.2);
        }

        .spiral-canvas {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            opacity: 0.15;
            pointer-events: none;
        }

        @media (max-width: 768px) {
            nav ul {
                gap: 1rem;
            }
            section {
                padding: 4rem 5%;
            }
        }
    </style>
</head>
<body>
    <canvas class="phi-bg" id="phiCanvas"></canvas>

    <!-- Floating Donate Button -->
    <div class="floating-donate">
        <a href="https://donate.stripe.com/bJebJ32RYaiW5563cu" class="donate-button" target="_blank">
            <span style="font-size: 1.3rem;">❤️</span>
            <span>Support Research</span>
        </a>
    </div>

    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#framework">Framework</a></li>
            <li><a href="#research">Research</a></li>
            <li><a href="#results">Results</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#testimonials">Testimonials</a></li>
            <li><a href="#faq">FAQ</a></li>
            <li><a href="#applications">Applications</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="home" class="hero">
        <canvas class="spiral-canvas" id="spiralCanvas" width="800" height="800"></canvas>
        <h1>The Castleberry Geometric Framework</h1>
        <p class="subtitle">Novel Mathematical Structures for Consciousness-Matter Interfaces</p>
        <div class="phi-value">φ = 1.618034...</div>
        <p style="max-width: 800px; font-size: 1.2rem; margin: 2rem auto;">
            Bridging consciousness and physical matter through the golden ratio's harmonic resonance
        </p>
        <div>
            <a href="#framework" class="cta-button">Explore the Framework</a>
            <a href="#research" class="cta-button">View Research</a>
        </div>
    </section>

    <section id="framework">
        <h2>The Four Pillars of CGF</h2>
        
        <div class="hexagon-container">
            <div class="hexagon">
                <svg viewBox="0 0 100 115">
                    <polygon points="50,0 100,28.75 100,86.25 50,115 0,86.25 0,28.75" 
                             fill="none" stroke="#ffd700" stroke-width="2"/>
                </svg>
            </div>
            <div class="hexagon">
                <svg viewBox="0 0 100 115">
                    <polygon points="50,0 100,28.75 100,86.25 50,115 0,86.25 0,28.75" 
                             fill="none" stroke="#ffd700" stroke-width="2"/>
                </svg>
            </div>
            <div class="hexagon">
                <svg viewBox="0 0 100 115">
                    <polygon points="50,0 100,28.75 100,86.25 50,115 0,86.25 0,28.75" 
                             fill="none" stroke="#ffd700" stroke-width="2"/>
                </svg>
            </div>
            <div class="hexagon">
                <svg viewBox="0 0 100 115">
                    <polygon points="50,0 100,28.75 100,86.25 50,115 0,86.25 0,28.75" 
                             fill="none" stroke="#ffd700" stroke-width="2"/>
                </svg>
            </div>
        </div>

        <div class="framework-grid">
            <div class="framework-card">
                <h3>ΦHRL</h3>
                <h4 style="color: #a0a0a0; margin-bottom: 1rem;">Φ-Scaled Hexagonal Resonance Lattice</h4>
                <p>Hexagonal shells scaled by the golden ratio φ, creating an inverse-φ frequency ladder. Each shell produces harmonic resonances that cascade across multiple scales.</p>
                <div class="formula">
                    s<sub>n</sub> = s<sub>1</sub> · φ<sup>(n-1)</sup><br>
                    f<sub>n</sub> = f<sub>1</sub> · φ<sup>-(n-1)</sup>
                </div>
                <p><span class="highlight">Experimental validation:</span> Resonance peaks within 2-5% tolerance across 5 shells.</p>
            </div>

            <div class="framework-card">
                <h3>CSHBG</h3>
                <h4 style="color: #a0a0a0; margin-bottom: 1rem;">Castleberry Spiral-Hex Bloom Geometry</h4>
                <p>A hybrid structure combining phyllotactic spiral positioning with local hexagonal symmetry, creating living geometric patterns that evolve naturally.</p>
                <div class="formula">
                    θ<sub>n</sub> = n · (2π/φ) ≈ n · 222.5°<br>
                    r<sub>n</sub> = r<sub>0</sub> · φ<sup>(n/8)</sup>
                </div>
                <p><span class="highlight">Key insight:</span> Dual symmetry enables both continuous spiral growth and discrete hexagonal coupling.</p>
            </div>

            <div class="framework-card">
                <h3>MDPG</h3>
                <h4 style="color: #a0a0a0; margin-bottom: 1rem;">Multi-Domain Pathway Geometry</h4>
                <p>A mapping formalism that links geometric coherence across quantum, molecular, biological, and consciousness domains through golden ratio scaling.</p>
                <div class="formula">
                    G<sub>i+1</sub> = T<sub>i</sub>(G<sub>i</sub>, φ, f<sub>ref</sub>, Ψ)<br>
                    ∂G/∂t = φ<sup>n</sup> · ∇²G + f<sub>ref</sub> · F(Ψ, t)
                </div>
                <p><span class="highlight">Innovation:</span> First mathematical framework for consciousness-matter transitions.</p>
            </div>

            <div class="framework-card">
                <h3>SVCDG</h3>
                <h4 style="color: #a0a0a0; margin-bottom: 1rem;">