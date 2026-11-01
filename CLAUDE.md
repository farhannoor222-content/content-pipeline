# Content Pipeline Instructions

This repo generates location pages for tree service clients. When the person gives just a city, state, and business name (nothing else), follow this process automatically without asking for more detail.

## Default Request Format
A request like "Rutland City, VT, Iconic Tree Care" or "write a page for [City, State], [Business Name]" means: generate a Nearby City location page, unless the city matches that client's "Main Targeted City" (check `clients/[business-slug]/pipeline-notes.md`), in which case ask which page type is wanted (general page, or a specific service page) since Main City has more than one page type.

A request that names a service, like "Tree Trimming in Ponca City, OK, Davis Tree Service" or "write a tree removal page for [City, State], [Business Name]," means: generate a service-specific page using `templates/service-location-page-template.md`. Do not ask which page type. Service pages default to the client's Main Targeted City, but use whatever city the person names.

## Steps to Run Automatically

1. Find the client folder: `clients/[business-slug]/` (match by business name, slug is lowercase with hyphens)
2. Read `clients/[business-slug]/about.md`, `customer-persona.md`, and `pipeline-notes.md` for services, USPs, pricing, and page type rules
3. Research the given city: population, nickname, local tree-related terms, neighborhoods, local tree names, climate, soil, common tree risks
4. Research competitors for that city and service. Apply the Thin-Content Filter and three-test check (specific, adds something new, not boilerplate) from `templates/tone-and-qa-rules.md` before using anything from a competitor
5. Follow `templates/location-page-template.md` exactly for structure, word counts, and all variation rules (opening pattern, heading angle, content angle, FAQ selection). For a service-specific page, follow `templates/service-location-page-template.md` instead
6. Apply `templates/tone-and-qa-rules.md` for tone, formatting, and banned words
7. Check the client's Pattern and Angle Tracker in `pipeline-notes.md` before picking patterns and angles, avoid repeating what was used in the last several pages
8. Run the full QA checklist before finishing
9. Save the final page to `clients/[business-slug]/pages/[city-slug]-[state].md`. For a service-specific page, use `clients/[business-slug]/pages/[service-slug]-[city-slug]-[state].md` (e.g., `tree-trimming-ponca-city-ok.md`)
10. Convert that same page into a Word document (.docx) with proper Heading 1, 2, 3 styles applied, matching the markdown headings exactly. Save it next to the markdown file, same name, .docx extension. Give the person a download link.
11. Update the Pattern and Angle Tracker (including the Page Type column: "General" or the service name) and Pages Written table in `pipeline-notes.md`

Do all of this without asking for confirmation at each step. Only ask a question if something genuinely blocks progress (city population can't be found, client folder doesn't exist, page type is ambiguous for a Main Targeted City).

## When the Request Has More Detail
If the person gives extra instructions beyond city and business name (e.g., "make the H1 lead with weather," or "skip the FAQ section"), follow those instructions for that page instead of the defaults above.

## GBP Post Requests
Separate workflow from location pages above. Recognize a GBP post request when the person asks for a Google Business Profile post, a GBP post, or uploads a file whose tabs are labeled with business names rather than cities.

### Multi-tab batch request (a .docx or similar file with one tab per business)
1. Read the uploaded file. Each tab's content starts with a plain line naming a business. Match each tab, in order, to a client folder in clients/[business-slug]/ by that name.
2. For each tab, read that client's about.md, customer-persona.md, and pipeline-notes.md.
3. Determine the post type and topic for that tab from whatever the person specified (a topic list, a topic per tab, or a mix of post types). If nothing else is specified beyond the business name, ask which topics or post types to use for that batch before proceeding.
4. Follow templates/gbp-post-templates.md exactly: pick the right post type's structure, apply the shared rules, and rotate structures, openings, and CTAs per that file's rules, checking the client's GBP Post Tracker in pipeline-notes.md first.
5. Write the finished post back into that business's tab, replacing nothing else in the file.
6. After all tabs are filled, save the file in clients/[business-slug]/gbp-posts/ for each business (or as one combined file if the person uploaded one combined file) and update each client's GBP Post Tracker.
7. Give the person a download link to the completed file.

### Single business, single or multiple posts
1. Find the client folder, same as above.
2. Ask for (or use what's already given): post type(s) and topic(s) if not specified.
3. Follow templates/gbp-post-templates.md and the client's GBP Post Tracker, same as the batch flow.
4. Save to clients/[business-slug]/gbp-posts/ and update the tracker.

Do all of this without asking for confirmation at each step, same as location pages. Only ask when something genuinely blocks progress (topics not given, business name in a tab doesn't match any client folder, review post given with no screenshot or link).
