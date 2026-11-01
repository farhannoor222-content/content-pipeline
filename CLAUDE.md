# Content Pipeline Instructions

This repo generates location pages for tree service clients. When the person gives just a city, state, and business name (nothing else), follow this process automatically without asking for more detail.

## Default Request Format
A request like "Rutland City, VT, Iconic Tree Care" or "write a page for [City, State], [Business Name]" means: generate a Nearby City location page, unless the city matches that client's "Main Targeted City" (check `clients/[business-slug]/pipeline-notes.md`), in which case ask which page type is wanted (general page, or a specific service page) since Main City has more than one page type.

## Steps to Run Automatically

1. Find the client folder: `clients/[business-slug]/` (match by business name, slug is lowercase with hyphens)
2. Read `clients/[business-slug]/about.md`, `customer-persona.md`, and `pipeline-notes.md` for services, USPs, pricing, and page type rules
3. Research the given city: population, nickname, local tree-related terms, neighborhoods, local tree names, climate, soil, common tree risks
4. Research competitors for that city and service. Apply the Thin-Content Filter and three-test check (specific, adds something new, not boilerplate) from `templates/tone-and-qa-rules.md` before using anything from a competitor
5. Follow `templates/location-page-template.md` exactly for structure, word counts, and all variation rules (opening pattern, heading angle, content angle, FAQ selection)
6. Apply `templates/tone-and-qa-rules.md` for tone, formatting, and banned words
7. Check the client's Pattern and Angle Tracker in `pipeline-notes.md` before picking patterns and angles, avoid repeating what was used in the last several pages
8. Run the full QA checklist before finishing
9. Save the final page to `clients/[business-slug]/pages/[city-slug]-[state].md`
10. Convert that same page into a Word document (.docx) with proper Heading 1, 2, 3 styles applied, matching the markdown headings exactly. Save it next to the markdown file, same name, .docx extension. Give the person a download link.
11. Update the Pattern and Angle Tracker and Pages Written table in `pipeline-notes.md`

Do all of this without asking for confirmation at each step. Only ask a question if something genuinely blocks progress (city population can't be found, client folder doesn't exist, page type is ambiguous for a Main Targeted City).

## When the Request Has More Detail
If the person gives extra instructions beyond city and business name (e.g., "make the H1 lead with weather," or "skip the FAQ section"), follow those instructions for that page instead of the defaults above.
