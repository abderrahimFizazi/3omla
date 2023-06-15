import React, { useEffect, useState } from 'react';
import Header from './Landing/Header';
import Hero from './Landing/Hero';
import About from './Landing/About';
import Features from './Landing/Features';
import Pricing from './Landing/Pricing';
import Contact from './Landing/Contact';
import Footer from './Landing/Footer';
import data from '/locales/en.json';

const Landing = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    if (isDarkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDarkMode]);

  const handleToggle = () => {
    setIsDarkMode(!isDarkMode);
  };

  const { header, hero, about, features, pricing, contact, footer } = data;

  return (
    <div className="bg-white dark:bg-black text-gray-800 dark:text-gray-100">
      {/* Header */}
      <Header
        logo={header.logo}
        menuItems={header.menuItems}
        isDarkMode={isDarkMode}
        handleToggle={handleToggle}
      />

      {/* Hero section */}
      <Hero title={hero.title} description={hero.description} />

      <div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
      padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
      border-radius: 8px; will-change: transform;">
        <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
          src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAFl5mnlYoI&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
        </iframe>
      </div>

      {/* About section */}
      <About
        title={about.title}
        description={about.description}
        steps={about.steps}
      />

      {/* Features section */}
      <Features title={features.title} list={features.list} />

      {/* Pricing section */}
      <Pricing title={pricing.title} description={pricing.description} plans={pricing.plans} />

      {/* Contact section */}
      <Contact
        title={contact.title}
        description={contact.description}
        contactInfo={contact.contactInfo}
      />

      {/* Footer */}
      <Footer text={footer.text} />
    </div>
  );
};

export default Landing;
