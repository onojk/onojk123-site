# onojk123.com: TODO

This file is excluded from Firebase Hosting (see `firebase.json` → `ignore`), so it is never served.

Books live in `books.json`. Fill in a field, then deploy. No layout changes needed.
An `asin` must be the exact 10-character Amazon ID. Cards with no `asin` and no `youtube` show "Coming soon".

## Book ASINs needed (`books.json` → `asin`)
- [ ] The Big Book of Prime Secrets: How Numbers Keep Secrets, and Why No One Has Cracked Them
- [ ] The Free Machine, Book One
- [ ] The Free Machine, Book Two
- [ ] Light Through the Holes: Sieves, Strikes, and the Price of Seeing Primes
- [ ] The Garden That Computes: Computers Grown, Not Built
- [ ] The Real Gatekeeper (if it gets a Kindle edition)
- [ ] The Number Country, Arc One (`series[0].books[n].asin`):
  - [ ] 1 Forward Only
  - [ ] 2 The Ceiling
  - [ ] 3 The Mirror Abacus
  - [ ] 4 The Sideways Country
  - [ ] 5 The Ring of N
  - [ ] 6 The Wander
  - [ ] 7 The Dial
  - [ ] 8 The Log Bridge
  - [ ] 9 The Hoard
  - [ ] 10 The Tower Nobody Built
- [ ] The Number Country KDP series page URL (could link the series heading)

## YouTube URLs needed (`books.json` → `youtube`)
- [ ] The Real Gatekeeper audiobook (card currently says "Audiobook on YouTube · link coming soon")
- [ ] Optional: The Rooms That Hold Us read-along (~/roomstape/out has a YouTube description, so a video seems to exist)
- [ ] Optional: read-alongs for any other book with a *tape folder (Wall at Two, Horizons, Light Through the Holes, Garden, Number Country books)

## Music & Art links needed (index.html, "Music & Art" section)
- [ ] YouTube channel URL
- [ ] Etsy shop URL

## Covers
All covers were found and copied to `img/books/` (375–451 × 600 px JPG). Notes:
- [ ] The Ceiling: no ebook cover JPG was found. `nc-02-the-ceiling.jpg` was cropped from the
      front panel of the paperback wrap (`~/ceilingtape/build/kdp/cover-check.png`). Replace it with the real ebook cover when you have one.
- The Garden That Computes uses `~/livingcomputer/cover/cover.jpg` (3:4, so it shows letterboxed on its card).

## Copy to review (written by Claude, please check)
- [ ] Blurbs for The Wall at Two, Preservation and Horizons and The Real Gatekeeper were written from the
      covers and chapter titles. The others come from your blurb/metadata files.
- [ ] The Number Country has no series blurb (`series[0].blurb` is empty, so nothing shows). Add one if you like.
- [ ] The Mirror Abacus tagline is empty (none was legible on the cover).
