import { defineConfig } from 'astro/config';

export default defineConfig({
  // The combined /about-contact experience is retired in favor of separate
  // /about and /contact pages (HEOS_About_Contact_Governing_Specification,
  // PRE-IMPLEMENTATION FROZEN). Astro's built-in redirects config preserves
  // backward compatibility with a static-generated redirect page, with no
  // additional routing infrastructure.
  redirects: {
    '/about-contact': '/about',
  },
});
