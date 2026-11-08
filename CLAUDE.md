# Content Pipeline Instructions

This repo generates location pages for tree service clients. When the person gives just a city, state, and business name (nothing else), follow this process automatically without asking for more detail.

## Standing Rules (apply to every page, override template defaults)
- **Meta description:** always start with an action verb (Get, Call, Trust, etc.) and keep it 150 to 160 characters (count characters, not words). This replaces the word counts in the templates. Still include the exact service or location phrase each template requires.
- **Localization:** use only real, checkable local details: weather patterns, roads and streets, house types, tree species, terrain. Never use or imply specific storm dates, named weather events, or incidents (e.g., "the August 2018 storm"). Tie each detail to how the client works.
- **"Crew" overuse:** do not lean on the word "crew" or "crews." Use it sparingly (about 2 to 3 times per page at most) and vary with the business name, "our team," "our arborists," "our tree surgeons," or "our climbers." Never use it in back-to-back sentences.
- **Deliverable:** always send the finished .docx to the person as a downloadable attachment (SendUserFile). A file path in text is not a download link.
- **Banned phrase:** never write "three crew," "three crews," or any count of crews (e.g., "3 crews") in any page, for any client. Say "our crews" or "our team" instead.

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
8. Run the full QA checklist before finishing, including the 1% keyword density check (`python3 scripts/keyword_density.py <page.md>`) for "tree service," "arborist," "tree care," "expert," and the location name (city, township, or neighborhood)
9. Save the final page to `clients/[business-slug]/pages/[city-slug]-[state].md`. For a service-specific page, use `clients/[business-slug]/pages/[service-slug]-[city-slug]-[state].md` (e.g., `tree-trimming-ponca-city-ok.md`)
10. Convert that same page into a Word document (.docx) with `python3 scripts/md_to_docx.py <page.md>`. It applies proper Heading 1, 2, 3 styles at the house sizes (H1 18 pt, H2 16 pt, H3 14 pt), matching the markdown headings exactly. These sizes apply to every location, service, neighborhood, and arborist page. Save it next to the markdown file, same name, .docx extension. Give the person a download link.
11. Update the Pattern and Angle Tracker (including the Page Type column: "General" or the service name) and Pages Written table in `pipeline-notes.md`

Do all of this without asking for confirmation at each step. Only ask a question if something genuinely blocks progress (city population can't be found, client folder doesn't exist, page type is ambiguous for a Main Targeted City).

## When the Request Has More Detail
If the person gives extra instructions beyond city and business name (e.g., "make the H1 lead with weather," or "skip the FAQ section"), follow those instructions for that page instead of the defaults above.

## Project Manager Preferences
Some requests come from a specific project manager. When the person says a page is for one of these managers, apply that manager's rules on top of the normal template. Where they conflict, the manager's rules win.

### Rakib
- Leave out the landmark or area H2 ("We Serve Every Corner of [City]", "Our Arborist Service Is Available Throughout [City]", or similar).
- Make up for it with stronger localization in the other sections, especially Why Choose Us and Our Services. Use local species, terrain, weather, housing, and streets only where they fit naturally. Never force a local detail into a sentence just to have one.
- Rakib reviews strictly, so choose words carefully. Use plain, precise wording, make no claim the client files or research don't support, avoid filler, and do an extra pass for banned words and awkward phrasing before finishing.

## Neighborhood Pages
Until a dedicated neighborhood template exists, write a neighborhood page (e.g., "Hillcrest, Jacksonville, FL (neighborhood page)") with `templates/location-page-template.md`, treating the neighborhood as the place. Use "[Neighborhood], [City], [ST]" in the H1 and meta phrase (e.g., "tree service in Hillcrest, Jacksonville, FL"). Neighborhood populations are rarely published, so use Tier 2 counts unless a population is found. Save to `clients/[business-slug]/pages/[neighborhood-slug]-[city-slug]-[state].md`. In the trackers, log Page Type as "Neighborhood".

## Arborist Page Requests
Separate page type from the location pages above. Recognize it when the person asks for an "arborist page," "arborist service page," or "arborist service in [City, ST]" for a client. This takes priority over the Default Request Format, so don't ask which page type, even for the Main Targeted City. One request may name 2 to 3 locations. Write one page per location.

1. Find the client folder and read `about.md`, `customer-persona.md`, and `pipeline-notes.md` (USPs, services, service page URLs, pricing, claims the profile supports).
2. Research each city for localization (species, climate, soil, tree risks, real tight and wide-lot neighborhoods). Research competitors for "arborist [City, ST]" when they exist, applying the Thin-Content Filter. Skip listing and directory sites (Yelp, Angi, HomeAdvisor, Thumbtack, BBB, "top 10" roundups). If no usable competitor exists, which is common in this niche, proceed without one and note it in the tracker.
3. Follow `templates/arborist-page-template.md` exactly, including its wording rules (no study, training, or train) and H2 variation rules. Check the client's Arborist Page Tracker first. On multi-location requests, vary H2s, the H1 angle, and USP H3s across the pages.
4. Apply `templates/tone-and-qa-rules.md` and run both QA checklists.
5. Save to `clients/[business-slug]/pages/arborist-[city-slug]-[state].md`, convert to .docx next to it (Heading 1, 2, 3 styles, live H3 links), and give the person download links.
6. Update the client's Arborist Page Tracker (create it if missing) and Pages Written table (Page Type "Arborist").

Service H3 links use the URLs the person gives, or the client's own service URLs from its files. If none exist, leave the H3s unlinked and say so. Don't stop to ask.

## GBP Post Requests
Separate workflow from location pages above. Recognize a GBP post request when the person asks for a Google Business Profile post, a GBP post, or uploads a file whose tabs are labeled with business names rather than cities.

### Multi-tab batch request (a .docx or similar file with one tab per business)
1. Read the uploaded file. Each tab's content starts with a plain line naming a business. Match each tab, in order, to a client folder in clients/[business-slug]/ by that name.
2. For each tab, read that client's about.md, customer-persona.md, and pipeline-notes.md.
3. Determine the post type and topic for that tab from whatever the person specified (a topic list, a topic per tab, or a mix of post types). If nothing else is specified beyond the business name, ask which topics or post types to use for that batch before proceeding.
4. Follow templates/gbp-post-templates.md exactly: pick the right post type's structure, apply the shared rules, and rotate structures, openings, and CTAs per that file's rules, checking the client's GBP Post Tracker in pipeline-notes.md first.
5. Write the finished post back into that business's tab, replacing nothing else in the file. Format per the "Document Formatting" section of templates/gbp-post-templates.md: business name 16 pt before the business's first post, post titles bold 14 pt, body text 12 pt.
6. After all tabs are filled, save the file in clients/[business-slug]/gbp-posts/ for each business (or as one combined file if the person uploaded one combined file) and update each client's GBP Post Tracker.
7. Give the person a download link to the completed file.

### Blog promotion posts
When the person gives blog titles with links and excerpts, write GBP blog promotion posts with `templates/gbp-blog-promotion-template.md`. Keep links exactly as given and do not crawl them. Write only from the excerpt.

### Single business, single or multiple posts
1. Find the client folder, same as above.
2. Ask for (or use what's already given): post type(s) and topic(s) if not specified.
3. Follow templates/gbp-post-templates.md and the client's GBP Post Tracker, same as the batch flow.
4. Save to clients/[business-slug]/gbp-posts/ and update the tracker.

Do all of this without asking for confirmation at each step, same as location pages. Only ask when something genuinely blocks progress (topics not given, business name in a tab doesn't match any client folder, review post given with no screenshot or link).

## Location Pages for Non-Tree Clients
A "[Service] in [City, ST]" request for a non-tree client uses that industry's location template instead of the tree templates, with the same steps as tree location pages (research, QA, save to `clients/[business-slug]/pages/[service-slug]-[city-slug]-[state].md`, .docx, tracker update):

| Industry | Template |
|---|---|
| Hood cleaning | `templates/hood-cleaning-location-page-template.md` |
| Painting | `templates/painting-location-page-template.md` |
| Excavation | `templates/excavation-location-page-template.md` |

Apply tone-and-qa-rules.md, but skip the tree-only parts (Service Definitions, tree Required Terms). If the person supplies local information, work it in naturally.

## Entity Page Requests (non-tree clients; tree clients see "Tree Entity Page Requests" below)
Recognize an entity request when the person asks for a "[service] near [Location]" page (or an "entity") for a non-tree client. Pick the template by industry:

| Industry | Template | Clients |
|---|---|---|
| Excavation | `templates/excavation-entity-template.md` | Bonzo Excavating |
| Septic | `templates/septic-entity-template.md` | Bonzo Septic Repair and Installation |
| Painting | `templates/painting-entity-template.md` | In & Outdoor Solution |
| Hood cleaning | `templates/hood-cleaning-entity-template.md` | Advanced Hood Cleaning Solutions |

1. Find the client folder and read `about.md`, `customer-persona.md`, and `pipeline-notes.md` (the base address for driving directions comes from about.md).
2. Research the given landmark or area (SERP, Reddit, Facebook) and use any details the person provides.
3. Follow the matching template exactly. The tree-service templates and tree Required Terms do not apply.
4. If driving directions are not provided, ask the person to paste the Google Maps directions from the client's base to the location before writing the directions section.
5. Save to `clients/[business-slug]/entities/[location-slug].md`, convert to .docx next to it, and give the person a download link.

## Tree Entity Page Requests
Recognize a tree entity request when the person asks for a "tree service near [Location]" page (or an "entity") for a tree client. This is not a GBP post and not a location page. Use `templates/tree-entity-template.md`, which has three variants:

- **Regular:** one page for a client (default).
- **Multi-Page:** a request for several entity pages for the same business. Use the Multi-Page outline for every page in that request.
- **Rakib:** the page is for Rakib. This variant wins over the other two, and the Rakib rules above also apply.

1. Find the client folder and read `about.md`, `customer-persona.md`, and `pipeline-notes.md` (base address, services, equipment, USPs).
2. Research the landmark or area (SERP, Reddit, Facebook) and use every detail the person provides. Focus on the landmark, not the city.
3. Check the client's Entity Page Tracker in `pipeline-notes.md`, then follow the chosen variant exactly. Word limits are hard limits.
4. If driving directions are not provided, ask the person to paste the Google Maps directions from the client's base to the location before writing the directions section. Place any Google Maps iframe they give under the directions H2 unchanged.
5. Run the template's QA checklist.
6. Save to `clients/[business-slug]/entities/[location-slug].md`, convert to .docx next to it with `python3 scripts/md_to_docx.py`, and give the person a download link.
7. Update the client's Entity Page Tracker (create it if missing: Date, Location, Variant, H1 title, H2 headings, Opening pattern) and the Pages Written table (Page Type "Entity").
