# Accessibility Audit

**Website:** https://mi349portfolioweigle.netlify.app/  
**Source repository:** https://github.com/weiglebe/Portfolio  
**Audit date:** November 5, 2026  
**Tool:** Google PageSpeed Insights (Lighthouse)

## Audit findings

I ran my published portfolio website through Google PageSpeed Insights. The accessibility score was **100/100 on the first audit**, so no Lighthouse accessibility fixes were required. The screenshot also shows scores of **100/100 for Performance, Best Practices, and SEO**.

| Category | Reported score |
| --- | ---: |
| Accessibility | 100 |
| Performance | 100 |
| Best Practices | 100 |
| SEO | 100 |

![PageSpeed Insights audit results showing a 100 accessibility score](images/pagespeed-audit.png)

## Review of existing accessibility features

After the audit, I reviewed the HTML and CSS in my portfolio repository. Several accessibility features were already built into the site:

- **Skip link:** A "Skip to main content" link appears at the beginning of the page's HTML and becomes visible when it receives keyboard focus.
- **Semantic structure:** The page uses `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>` to organize content.
- **Descriptive headings and navigation:** The page has a clear heading hierarchy, and the navigation is labeled "Main navigation."
- **Image alternative text:** The image in the About section includes an `alt` description and a caption.
- **Native links:** Navigation, project, and contact links use standard HTML anchor elements, which are normally keyboard accessible.

## Fixes and improvements

**Required accessibility bug fixes:** None were identified by the supplied Lighthouse audit. The website achieved 100/100 without changes.

The site already includes an important keyboard accessibility feature: a focus-revealed skip link. Lighthouse's automated score does not establish complete accessibility, so keyboard-only testing is still necessary. One optional improvement to consider is a custom, high-contrast `:focus-visible` indicator for all links, after checking the site's existing browser focus styling. I have not counted that as an implemented change.

## Conclusion

My portfolio received a perfect **100/100 Lighthouse Accessibility score on its initial PageSpeed Insights audit**. This showed that no accessibility issues were flagged by the automated test. Reviewing the code also showed that the site already uses semantic HTML, a skip link, and standard navigation links. The required keyboard-only demonstration will provide a separate manual assessment of navigation without a mouse.

