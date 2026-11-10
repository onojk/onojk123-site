# onojk123.com: TODO

This file is excluded from Firebase Hosting (see `firebase.json` → `ignore`), so it is never served.

Books live in `books.json`. Fill in a field, then deploy. No layout changes needed.
An `asin` must be the exact 10-character Amazon ID. Cards with no `asin` and no `youtube` show "Coming soon".

## Book ASINs needed (`books.json` → `asin`)
- [x] The Big Book of Prime Secrets (B0HPZXW944; possible paperback B0HPZY5HM9 unverified)
- [ ] The Free Machine: CONFIRM the mapping, which may be swapped. Currently Book One = B0HP77MHLW and Book Two = B0HP7MM9DG (Kindle). Other candidates B0HP76ZYBR and B0HP79LB5G are unconfirmed and unused.
- [ ] Light Through the Holes: Sieves, Strikes, and the Price of Seeing Primes
- [x] The Garden That Computes (B0HPZL5FX8; second edition B0HPZXF6ZH not shown)
- [x] The Real Gatekeeper (B0HNG5RMF7)
- [ ] The Number Country, Arc One (`series[0].books[n].asin`):
  - [x] 1 Forward Only (B0HQVZMFGW; second edition B0HQW6VBVY not shown)
  - [x] 2 The Ceiling (B0HQVS799C; second edition B0HQWW4LPN not shown)
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
- [x] The Real Gatekeeper audiobook (QYf_ayng_wY, labelled "Watch the free audiobook")
- [x] Read-alongs linked: The Wall at Two, Rooms, Preservation and Horizons, Light Through the Holes, Garden
- [x] Multi-part read-alongs linked, every part on the card: Big Book, Number Country 1–8
- [ ] The Free Machine Books One and Two: YouTube playlist URLs (will replace the 5 + 4 part links with one link each)
- [ ] The Dial: Vol. 1 video ID (only Vol. 2 is linked)
- [ ] Optional: read-alongs for any other book with a *tape folder (Number Country books 9, 10)

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
