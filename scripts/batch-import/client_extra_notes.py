# Hand-checked overrides and notes for the batch import.
OVR = {'allegiant-tree-care': {'city': 'Lancaster, PA'},
 'als-outdoor-needs': {'city': 'Greensboro, GA'},
 'bladis-tree-service': {'city': 'Grand Prairie, TX (about.md target: Dallas Fort Worth area)'},
 'bonzo-septic-repair-and-installation': {'city': 'UNCONFIRMED (service areas are Pittsburgh-area suburbs)'},
 'borders-tree-service': {'areas': ['Big Lake',
                                    'San Angelo',
                                    'Ozona',
                                    'Eldorado',
                                    'Eden',
                                    'Rocksprings',
                                    'Christoval',
                                    'Mertzon',
                                    'Carlsbad',
                                    'Barnhart',
                                    'Menard',
                                    'Junction',
                                    'Comstock'],
                          'city': 'Sonora, TX'},
 'clean-green-tree-service': {'city': 'Champaign, IL'},
 'david-kennedy-tree-and-landscaping': {'city': 'Culpeper, VA'},
 'hawk-tree-service': {'city': 'Colorado Springs, CO'},
 'keystone-tree-techs': {'city': 'Rochester, PA'},
 'lone-pine-tree-service': {'city': 'Valley Springs, CA'},
 'midwest-tree': {'city': 'Lenexa, KS'},
 'oathkeepers-tree-care': {'city': 'York, PA'},
 'priority-property-services-fl': {'city': 'Webster, FL',
                                  'services': ['Tree Removal',
                                               'Tree Trimming & Pruning',
                                               'Stump Grinding',
                                               'Emergency Tree Service (24/7)',
                                               'Also listed in the current GBP description: land clearing, forestry mulching, lawn care, '
                                               'debris removal, pressure washing, trailer rental']},
 'rikin-tree-service': {'areas': ['Spencer, TN', 'Sparta, TN', 'Cookeville, TN', 'Monterey, TN'],
                        'city': 'UNCONFIRMED (customer-persona.md says Smithville, TN)'},
 'robison-tree-service': {'city': 'Lexington, KY'},
 'rooted-in-texas-tree-care': {'city': 'Cedar Park, TX'},
 'rugged-tree-service': {'city': 'UNCONFIRMED (about.md says Southwest Minnesota; address is Porter, MN)'},
 'solid-oak-tree-service': {'city': 'Pittsburgh, PA'},
 'tree-fellas': {'city': 'Concord, NH'},
 'zs-outdoor-services': {'city': 'UNCONFIRMED (first service area listed: Greensboro, GA)'}}

EXTRA = {'allegiant-tree-care': ['Experience: established 2018, but a USP says "25+ Years Of Experience." Refer to the team\'s experience, not the '
                         "company's age.",
                         "Main city: about.md's primary service location is Lancaster, PA; the address is Manheim, PA."],
 'als-outdoor-needs': ["**Two source folders.** The about file came from `Al's Outdoor Needs`, the customer profile from `Al's`.",
                       '**Persona location mismatch.** customer-persona.md opens with "Orange County homeowners," but the business is in '
                       'Greensboro, GA. Check whether the persona was written for a different area before using its local details.',
                       "**Overlap with Z's Outdoor Services:** both list Greensboro, GA and nearby towns (Eatonton, Madison, White Plains, "
                       'Athens, Monroe).',
                       'Experience: about.md says established 2006 but "over 25 years of experience." Use team experience wording, not '
                       'company age.'],
 'andrews-all-around-tree-and-shrub': ["**Main city mismatch.** about.md's primary service location is Boardman, OH, but the business is "
                                       'in New Castle, PA, and the GBP text targets New Castle. Confirm which city gets the main page.'],
 'barto-stumps-and-tree-service': ['USP "150+ Five star Google Reviews": the trust-badge rule uses data/review-counts.csv for review '
                                   'counts. Do not hard-code this number on pages without confirming it is current.'],
 'bladis-tree-service': ['Main target in about.md is "Dallas Fort Worth area, TX," which is a region. Pick a specific city for the main '
                         'page and confirm.'],
 'bonzo-excavating': ['**Related client:** Bonzo Septic Repair and Installation looks like the same owner under a different name. Keep '
                      'their pages separate and avoid duplicate content between them.'],
 'bonzo-septic-repair-and-installation': ['**Related client:** Bonzo Excavating looks like the same owner. Keep pages distinct.',
                                          'about.md has no address, phone, or main city (address and phone are not required).'],
 'borders-tree-service': ['about.md lists only service-area towns and the main target city (Sonora, TX). Address and phone are not '
                          'required; services and USPs come from customer-persona.md.',
                          'Typo in about.md: "San Angel0" should be San Angelo; "Ozona" and "Big Lake" are listed twice.'],
 'david-kennedy-tree-and-landscaping': ["**Overlap with Fant's Tree Service:** both target Culpeper, VA. Avoid reusing the same local "
                                        "facts, landmarks, or headings between the two clients' Culpeper pages.",
                                        'about.md spells the city "Culpepper"; the correct spelling is Culpeper.'],
 'garcia-tree-removal-service': ['The source about file was saved in UTF-16 encoding; it was converted to plain text here.'],
 'gomez-tree-service': ['The GBP text leads with Burns, TN; the primary service location is Dickson, TN.'],
 'good-neighbor-tree-service': ['Main service location is Kannapolis, NC; the address is China Grove, NC.'],
 'in-and-outdoor-solution': ['Painting company (interior, exterior, pressure washing, epoxy). Tree templates do not apply.'],
 'jm-ezzy-tree-service': ["The about.md intro matches Davis Tree Service's word for word. The client owner re-sent it unchanged on "
                          '2026-11-02, so it is treated as correct for JM Ezzy.'],
 'keystone-tree-techs': ['About file added on 2026-11-02 (it was missing from the Turnkey batch).',
                         'Overlap with Leatherneck Tree Service: both center on Rochester, PA and Beaver County. Use different local '
                         'details on their pages.',
                         'The GBP text says "the best tree service in Greater Pittsburgh" (superlative; do not use).'],
 'leatherneck-tree-service': ['Veteran-owned and operated (about.md).',
                              'about.md lists Firewood as a service.',
                              '**Overlap with Keystone Tree Techs:** both center on Rochester, PA.'],
 'midwest-tree': ['about.md lists "ISA- Certified Arborist" as a USP, so the ISA certification may be named.'],
 'oathkeepers-tree-care': ['No labeled main city in about.md; the description says York, PA.'],
 'orellana-tree-service': ['about.md says "Baltimore\'s leading tree care company since 2010" (superlative; do not reuse). Address is '
                           'Joppatowne, MD; primary service area is Baltimore, MD.'],
 'perkins-lawn-care': ['**Dates conflict:** established 10/30/2021, but the GBP text says "since 2014." Confirm before stating years in '
                       'business.'],
 'premier-tree-service': ['about.md mentions "certified arborists."'],
 'priority-property-services-fl': ['about.md has a current and a new business description. The new one is the tree-focused version used '
                                  'here.'],
 'rikin-tree-service': ['about.md has no business name, address, or phone (not required). The name comes from the folder and '
                        'customer-persona.md.'],
 'robison-tree-service': ['USPs "No.1 Local Tree Service Company" and "Best Affordable Tree Services" are superlatives. Do not use them.',
                          'Address is Mt Sterling, KY; primary service location is Lexington, KY.'],
 'rugged-tree-service': ['Main service area is given as a region (Southwest Minnesota), not a city. Pick a main city and confirm.'],
 'solid-oak-tree-service': ['about.md claims "#1 tree service company in Pittsburgh" (superlative; do not use). Address is Freeport, PA; '
                            'main service area is Pittsburgh, PA.',
                            'Two phone numbers are listed: 724-384-7675 and 724-596-0171.'],
 'the-regions-tree-service': ['USP "TOP-RATED TEAM OF ARBORISTS" contains a superlative. Do not use.'],
 'timber-pros-tree-service': ['Services include palm tree skinning, specific to the Inland Empire.'],
 'top-chop-tree-service-and-land-management': ['The GBP text says based in Belgium, WI; the address and primary service area are Cedar '
                                               'Grove, WI.'],
 'tree-and-snow-removal-services': ['Also offers snow removal. Tree templates fit the tree services only.'],
 'united-tree-pro-service': ['USPs "Top Tier tree service" and "Best certified arborists in town" are superlatives. Do not use.'],
 'usa-tree-service': ['The GBP text misspells the name as "Ua tree service." Address is Kennewick, WA; primary service area is Walla '
                      'Walla, WA.'],
 'white-oak-tree-expert': ['The email in about.md looks like a personal address. Do not publish it on pages.'],
 'zs-outdoor-services': ['Services include bush hogging alongside tree work.',
                         "**Overlap with Al's Outdoor Needs:** both serve Greensboro, Eatonton, Madison, White Plains, Athens, and Monroe, "
                         'GA.',
                         'No address in about.md.']}
