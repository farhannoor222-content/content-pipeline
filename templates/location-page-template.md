# Location Page Template

Use this template for every city or town location page. Pull client details from the matching client profile file and local details from the matching location research file. Apply all rules in `tone-and-qa-rules.md` to every section.

Before writing, check the client's profile file for the "Pattern and Angle Tracker" table. It logs which opening pattern or content angle was used on this client's last several pages. Choose a different one for this page wherever a rule below says to rotate. After finishing the page, add a row to that tracker.

## Population Tiers

Check the city's population and set the tier. Use it to set sentence and word counts in sections marked "(tiered)" below.

- **Tier 1 (under 5,000 people):** 1 sentence for tiered descriptions
- **Tier 2 (5,000 to 20,000 people):** 2 sentences for tiered descriptions
- **Tier 3 (over 20,000 people):** 3 sentences for tiered descriptions

## Page Structure

### Meta Description
24 words. Must include "tree service in [City, State]."

### H1: Tree Service in [City, State]
40 words. Must include the exact phrase "tree service in [City, State]."

Opening pattern: choose one category not used in this client's last 3 to 4 pages.

- **Local problem first**: Research 2 to 3 tree-related problems genuinely common in this city or region (storm damage, a specific pest, soil conditions, drought stress, etc.), not just one. Mentioning only one problem narrows the page to readers who have that exact issue; covering 2 to 3 makes more readers feel the page speaks to them. Open with these problems, grounded in real local research, not generic lines.
- **Business and experience first**: Open with what the business does and how long it has served the area, then connect to the local context.
- **Local detail first**: Open with a specific researched local detail (climate, tree species, landmark) and tie it naturally into the need for tree service.
- **Benefit first**: Open with the outcome or benefit the homeowner gets, then explain briefly how.
- **Scenario first**: Open with a short, realistic scenario a local homeowner might face, built from real research about this location, not a stock image.

After the opening (regardless of pattern chosen), the H1 must:
- Introduce the business and its core services
- End with a benefit or result
- Include "tree service in [City, State]" naturally within the 40 words

Transition rule: the sentence introducing the business must connect directly to what the opening said, not jump to a generic service pitch. If the opening named problems, the business sentence should say how the business addresses those specific problems (e.g., stopping their spread, fixing them before they worsen), not just list services. The reader should feel one continuous thought, not two disconnected sentences stitched together.

Rule: never reuse the same opening pattern as the client's immediately preceding page. Never reuse specific phrasing, facts, or sentence structure from a previous page, even within the same pattern category.

### Trust Badges
Immediately after the H1 intro, add 4 short bullet points, 3 to 4 words each, conversion-focused trust signals. Not a sentence, just the phrase.

Pull from the client's USPs, certifications, or guarantees (from the client profile files). Examples of the type: "ISA-Certified Arborists," "Licensed and Insured," "24/7 Emergency Service," "X Years in Business."

Review count badge: check `data/review-counts.csv` (a shared, monthly-updated file covering all clients) for this client's current review count. If the file has an entry and the count is 30 or higher, include it as one of the 4 badges (e.g., "47 5-Star Reviews"). If there is no entry, the count is below 30, or the file does not exist yet, skip the review badge and use another USP or certification instead. Never invent a review count.

These 4 can stay the same across a client's pages or vary, either is fine, no rotation tracking needed for this section.

### H2: Customized Local Heading
Pull from the client's heading pool if an unused or recently-unused option exists. Otherwise write a new one using local details.

Body: 120 to 150 words.

Angle: choose one focus not used in this client's last 3 to 4 pages.

- **Crew/team-based**: Lead with who does the work, their experience, how they operate locally.
- **Terrain/risk-based**: Lead with a specific local challenge (tight lots, flood-prone soil, specific storm pattern, specific pest) and how the business handles it.
- **Tree-species-based**: Lead with the local tree species themselves, what makes them tricky or common here, and how the business's approach fits.
- **Community-based**: Lead with how long or how often the business works in this specific area, ties to local neighborhoods or landmarks.
- **Regulatory/practical-based**: Lead with local permit rules, insurance requirements, or practical constraints specific to this city, and how the business navigates them.

Content rule: do not cover every category (tree species, weather, soil, neighborhoods, equipment, regulations) every time. Pick 2 to 3 that fit the chosen angle naturally.

Expertise framing rule: this section is a landing page, not a blog or a manual. Never state a local fact (a city rule, a regulation, a tree risk) as a standalone fact. Always tie it back to what the business does about it: who the business works with, how the business handles it, what the business confirms or arranges for the customer. A sentence that only explains a fact without connecting it to the business's role is not allowed.

Depth rule: do not let one topic (e.g., one specific regulation or one specific pest program) take up more than about a third of this section's word count. Cover 2 to 3 distinct local factors instead of elaborating heavily on just one. Say each point directly and move on, don't pad a single idea across multiple sentences.

Local-reference rule: this section must name at least one real local neighborhood, street, or landmark from the location research, in any natural way that fits the chosen angle. Never skip this.

Order rule: vary the order details appear in from page to page.

Rule: never reuse the same angle as the client's immediately preceding page. Never reuse the same researched facts (same landmark, same species example) across pages for the same client unless the location genuinely requires it.

### H2: Our Services
Intro: 20 to 30 words, 2 sentences. Vary the angle (comprehensive care, convenience, local tree variety, range of expertise, etc.) page to page.

Content angle for this page: choose ONE angle for all service H3s on this page (from client's service list):

- **Problem it solves**: what issue homeowners run into that this service fixes
- **When it's needed**: signs or situations that call for this service
- **How it's done**: the process or method, briefly
- **Local tree connection**: which local species commonly need this service and why
- **Seasonal angle**: timing, like storm season, dormant season, growth season
- **Risk or consequence angle**: what happens if the problem goes unaddressed
- **Equipment or expertise angle**: what tool or skill makes the business capable of this

Rules:
- All service H3s on one page use the same chosen angle, for consistency
- Track which angle was used on this client's last 5 to 8 pages, and pick an angle not recently used
- Within the shared angle, still vary sentence structure and local details per service (different tree species per service, different specific detail per service)
- (tiered) word count per population tier applies
- No two consecutive H3s may start with the same word
- Action rule: every service description must make clear what the business does, not just state a problem or fact. Even on the "Problem it solves" angle, the description needs an action tied to the business (e.g., "We trim overgrown sycamore limbs before they snap in a storm," not just "Overgrown sycamore limbs can snap in a storm"). A sentence that describes only a risk or situation with no business action in it is incomplete, regardless of which angle is chosen.
- Species rule: when a service description references local tree species, name 2 to 3 species as examples, not just one. Naming only one species makes the service sound limited to that species. This applies at every population tier, including the 1-sentence Tier 1 descriptions, where the species can be listed briefly (e.g., "oak, maple, and sycamore limbs").

### H2: Why Choose [Business Name]
Intro: 20 to 30 words. State business name, what hiring them means for the homeowner.

Content angle for this page: choose ONE for all USP H3s on this page (from client's USP list):

- **Direct benefit**: what the customer gets from each USP, stated plainly
- **Trust/credibility**: why this USP makes the business reliable (experience, licensing, track record)
- **Comparison angle**: what this USP means compared to going without it, or hiring an unqualified crew
- **Peace-of-mind angle**: how this USP removes a specific worry for the homeowner
- **Local-relevance angle**: tie the USP to something specific about operating in this city or climate

Rules:
- All USP H3s on one page use the same chosen angle
- (tiered) word count per population tier applies
- Track angle used on this client's last 5 to 8 pages, avoid repeating
- Vary which USP leads the section from page to page, not always the same order

### H2: Our Working Process
Intro: 20 to 30 words. State business name, that the process is safety-focused.

Content angle for this page: choose ONE for all process-step H3s on this page (from client's process step list):

- **What we do**: a plain description of the action taken in this step
- **Why it matters**: the safety or quality reason behind this step
- **What the customer sees**: describe the step from the homeowner's point of view
- **Technical/expertise angle**: briefly note the skill or equipment involved in this step

Rules:
- Use an EVEN number of steps only: 4 or 6. Never 3 or 5.
- Process steps describe an action taken during the job (assessment, protection, execution, cleanup). A USP (like "Same-Day Response," "Free Estimates," "Licensed and Insured") is not a process step, even if it happens early. Do not pull USP content into this section, even reworded. If the client's process step list has an odd number of genuine process steps, either combine two closely related steps into one, or split a broader step into two, to land on 4 or 6, rather than adding an unrelated USP as a step.
- All process-step H3s on one page use the same chosen angle
- 20 to 24 words per step, 2 sentences
- Track angle used on this client's last 5 to 8 pages, avoid repeating

### H2: We Serve Every Corner of [City]
Intro: 20 words. State that the business serves the whole area.

For each neighborhood or landmark (from location research file):
- 10 to 12 words
- Describe the area without repeating its name in the description
- Do not promote the service in this section

### H2: Frequently Asked Questions
3 to 4 questions.

Question pool:
- **Mandatory**: one cost or pricing question appears on every page (the single most-searched topic)
- **Rotate** (pick 2 to 3, not used in this client's last 4 to 5 pages): timing or signs to call an arborist, permits or regulations, how to get a quote, insurance or liability, what to expect during service, emergency response time

Sources for questions:
- The client's profile file (customer-persona.md or pipeline-notes.md), especially "Concerns" and "Evaluation Criteria" sections, for real customer worries rather than generic questions
- Competitor FAQ sections, if a competitor page has a genuinely useful question not already in the pool above. Run it through the same test as the Thin-Content Filter in tone-and-qa-rules.md (specific, adds something new, not boilerplate) before adding it

Track which FAQ topics were used on this client's last 4 to 5 pages (add an "FAQ Topics" column to the Pattern and Angle Tracker) and avoid repeating the same set.

For each answer:
- 22 to 25 words
- First sentence: a direct answer, using real pricing or details from the client profile where relevant, never invented numbers
- If the client profile has no pricing reference, research a real local or regional average price range for that service via web search instead of skipping the number or leaving it vague. Still never invent a number.
- Second sentence: promote the business by directly naming its own action, using "we" or "our" (e.g., "Our free estimates give you the exact price," "Our arborists can confirm whether you need a permit," "We're available 24/7 for emergency calls"). Never a generic third-person statement ("A free estimate gives you...", "A tree service can confirm..."). Exception: if the question is explicitly about contacting the business, the whole answer can focus on that instead

### Optional: 1 to 2 Additional H2s
Only include if competitor research surfaced a genuinely useful topic the client's competitors cover and this template does not. Skip if no competitor page clears the 300-word thin-content threshold.

## Pattern and Angle Tracker (template for client profile files)

Each client profile file should include a table like this, updated after every page:

| City, State | H1 Pattern | Heading Angle | Services Angle | Why-Choose-Us Angle | Process Angle | FAQ Topics |
|---|---|---|---|---|---|---|
| (example) West Milton, PA | Local problem first | Crew-based | Local tree connection | Trust/credibility | What we do | Cost, Permits, Emergency response |
