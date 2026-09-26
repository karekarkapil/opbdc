# Design system (template and example)

*Companion to Chapter 8, "Design Without a Designer", of* 1 Person, Billion Dollar Conglomerate *(2026 edition). Last reviewed: September 2026.*

## What this is

The set of rules and parts that every screen, page, email and image in your company is built from, in one file. Every agent that produces anything visual reads it: coding agents, design agents, marketing agents. The payoff is consistency: dozens of agents producing work that looks and sounds like one company.

It has six parts: **Foundations, Components, Layout rules, Imagery, Interface words, Accessibility.**

## How to use it

1. Copy the template into your context kit. Fill in every part, even if some are only a line long at first.
2. Point every design, coding and marketing brief at this file.
3. When you reject a design, write the reason into the right part. "Too corporate" teaches an agent nothing; "Too many elements competing for attention on the first screen; one action only" does.
4. Keep your customers' real devices and conditions in it, and test on them.
5. For a second company, keep the structure and change the contents: new colors, new type, new imagery (Chapter 16).

---

## Template

```markdown
# Design system: [Company name]

Last checked: [YYYY-MM-DD]

## Our customers' real conditions
- Device: [the phone or computer they actually use]
- Connection: [typical speed and reliability]
- Where and when: [standing where, doing what, at what hour]
- Design rule that follows: [ ]

## 1. Foundations
### Colors (name them so agents can use the names)
| Token | Value | Purpose | Never use for |
|---|---|---|---|
| color-action | [#hex] | [buttons, links] | [ ] |
| color-warning | [#hex] | [ ] | [ ] |
| color-error | [#hex] | [something failed and needs action] | [anything that is not an error] |
| color-success | [#hex] | [ ] | [ ] |
| color-text | [#hex] | [ ] | [ ] |
| color-background | [#hex] | [ ] | [ ] |

### Type
| Token | Font | Size | Use |
|---|---|---|---|
| text-body | [ ] | [ ] | [ ] |
| text-heading | [ ] | [ ] | [ ] |

### Spacing, corners, shadows
- Spacing scale: [e.g. 4, 8, 16, 24, 32]
- Corner radius: [ ]
- Shadows: [ ]

## 2. Components
| Component | How it looks | When to use | When not to use |
|---|---|---|---|
| Primary button | [ ] | [one per screen] | [ ] |
| Form field | [ ] | [ ] | [ ] |
| Card | [ ] | [ ] | [ ] |
| Navigation | [ ] | [ ] | [ ] |
| Table or list | [ ] | [ ] | [ ] |
| Message (success, warning, error) | [ ] | [ ] | [ ] |

## 3. Layout rules
- The [two or three] things customers come for: [ ]. Always one tap away, never hidden in a menu.
- On a phone: [ ]
- On a computer: [ ]
- One primary action per screen.

## 4. Imagery
- Photographs: [light, backgrounds, framing, people and places shown]
- Illustrations: [style, or "none"]
- Examples we love: [links, with why]
- Examples we would never use: [links, with why]
- Rules: [e.g. product images show the real product; no generated customers or experts]

## 5. Interface words
- Errors say what happened and what to do next, without blame.
- Truthful: [e.g. "packed" is not "shipped"].
- Kind, brief, useful.
- No tricks: no pre-ticked boxes, no charges revealed at the last step, no hard-to-find cancellation.
- Examples: [error, confirmation, empty screen]

## 6. Accessibility
- Minimum text size: [ ]
- Contrast: [ ]
- Touch targets: [ ]
- Screen readers: [labels, alt text]
- Slow connections: [ ]
- Review routine: [who checks, when]
```

---

## Example: Copper Pot Mixers

*Illustration: Copper Pot Mixers is a fictional company, a small Bengaluru business selling craft cocktail mixers to independent bars and cafes.*

```markdown
# Design system: Copper Pot Mixers

Last checked: 2026-09-01

## Our customers' real conditions
- Device: mid-range Android phones, often two or three years old, sometimes with a cracked screen.
- Connection: patchy mobile data in back rooms and basements.
- Where and when: a tired bar manager reordering at one in the morning after closing, one-handed, in a dim back room, often holding a crate or a phone torch in the other hand.
- Design rule that follows: large targets, high contrast, very few steps, pages that work on a slow connection.

## 1. Foundations
### Colors
| Token | Value | Purpose | Never use for |
|---|---|---|---|
| color-copper | #B5652B | Brand accent: logo, section headers, the bottle band | Body text (too light on cream) |
| color-action | #1F5C4A | Buttons and links: the only color that means "tap here" | Decoration |
| color-warning | #9A5B00 | Cut-off passed, stock low | Errors |
| color-error | #B3261E | Something failed and needs action | Anything that is not an error |
| color-success | #2E7D32 | Order confirmed, payment received | Marketing |
| color-text | #1C1A17 | All body text | |
| color-background | #FBF6EE | Cream page background | |
| color-surface-dark | #1C1A17 | Dark mode background for night use | |

### Type
| Token | Font | Size | Use |
|---|---|---|---|
| text-body | A common free sans-serif with clear numerals (for example Inter or Noto Sans) | 18 px minimum on phones | Everything customers read |
| text-heading | Same family, bold | 24 to 32 px | Page and section titles |
| text-numbers | Same family, tabular numerals | 20 px | Quantities, prices, dates |
| text-display | A warm free serif (for example Fraunces) | 36 px and up | Marketing headlines only, never inside the ordering flow |

### Spacing, corners, shadows
- Spacing scale: 8, 16, 24, 32, 48 px.
- Corner radius: 8 px on buttons and cards. No pill shapes.
- Shadows: none inside the app; a single soft shadow on marketing cards.

## 2. Components
| Component | How it looks | When to use | When not to use |
|---|---|---|---|
| Primary button | color-action, full width on phones, 56 px tall, white bold label | The one main action on a screen ("Repeat this order", "Confirm") | Twice on one screen |
| Secondary button | Outline in color-action | Cancel, go back, change quantity | For the main action |
| Quantity stepper | Minus and plus buttons 48 px square around a 20 px number | Changing the number of cases of each flavor | Free-text quantity entry |
| Order card | Date, total, list of flavors and cases, "Repeat" button | Past orders, newest first | Marketing content |
| Message banner | Colored left bar, icon, one sentence, one action | Confirmations, warnings, errors | Promotions |
| Navigation | Bottom bar with three items: Reorder, Orders, Help | Every signed-in screen | Hidden menus |

## 3. Layout rules
- The three things bar managers come for are always one tap away, never hidden in a menu: **reorder, see my orders, get help.**
- One primary action per screen.
- Phone first. The ordering flow is designed for a phone held in one hand; the thumb must reach every button in the lower two-thirds of the screen.
- The delivery day is shown on every order screen, next to the confirm button, because it is the question managers ask most.
- On a computer: the same flow, centered, no wider than 640 px. No extra features on desktop.

## 4. Imagery
- Photographs: our real bottles and real drinks in real bars we supply, with permission. Warm, low light, as in a bar at night; copper and wood tones; hands pouring, not posed models.
- Illustrations: simple line drawings for the staff recipe cards only.
- Examples we love: a phone photo of a bar manager pouring the pineapple on a busy Friday (because it is true and it is ours).
- Examples we would never use: studio shots on white backgrounds with fruit splashes (every mixer brand has one); stock photos of cocktail parties.
- Rules: product images show the real product and the real label. We never use generated images of customers, bartenders or experts. Generated images may be used for backgrounds and concepts only, and never to show what a customer will receive.

## 5. Interface words
- Words that do not cause distress: "We couldn't place your order because the connection dropped. Nothing was ordered. Tap Repeat to try again." Not "Error 502". (Copper Pot is paid on delivery, so no card is ever charged in the app.)
- Truthful: "Packed" when packed, "Out for delivery" when it has left. Never "limited stock" unless stock is limited.
- Pleasant and beneficial: short, kind, and every sentence helps the customer finish the order.
- No tricks: no pre-ticked add-ons, no delivery charge revealed at the last step (it is shown on the order card), cancellation within the 30-minute window is one tap.
- Examples:
  - Confirmation: "Done. 4 cases arriving Tuesday. You can cancel until 1:42 am."
  - After cut-off: "It's past Sunday's 8 pm cut-off, so this order will arrive next Tuesday."
  - Empty screen: "No orders yet. Your first order will show here so you can repeat it in one tap."
  - Discontinued item: "[Flavor] is no longer available, so we left it out of this order." (Every current flavor is in the facts sheet; this message appears only when one is retired.)

## 6. Accessibility
- Minimum text size: 18 px body, 16 px for secondary labels, never smaller.
- Contrast: at least 4.5 to 1 for all text, checked in both light and dark mode (the back room is dark).
- Touch targets: at least 48 by 48 px, with 8 px between targets, so a tired thumb does not hit the wrong one.
- Screen readers: every button has a text label; every product image has alt text naming the flavor and pack.
- Slow connections: order history loads first as text; images load last and are optional. Every page under 500 KB.
- No task needs precise tapping, swiping or a long press.
- Review routine: an agent checks every changed screen for text size, contrast and labels as part of the ship checklist; the founder tests on the cheapest phone in the drawer, on mobile data, once a month.
```

---

## Related files

- [`voice-guide.md`](voice-guide.md): how the brand sounds; interface words should follow it.
- [`specifications.md`](specifications.md): acceptance tests used to test designs with five real people.
- [`../playbooks/five-person-test.md`](../playbooks/five-person-test.md): the five-person test itself.
- [`../playbooks/ship-checklist.md`](../playbooks/ship-checklist.md): where the accessibility check runs on every change.
