[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Huaminyo/news-image-20261120-huaminyo/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Huaminyo/news-image-20261120-huaminyo/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# Friday 20 November 2026 — The World in One Day

make.fun entry for `news-image-20261120` (entrant: @huaminyo).

One-page newspaper summing up the world news of Friday 20 November 2026:
**37 stories, 7 regions, 13 illustrated**, drawn entirely as original vector
art with PIL — no photographs, no copied artwork.

- Masthead is the date; subhead names the four biggest stories.
- "The day in numbers" strip (110+ missiles, 300,000+ evacuated, Nikkei
  −5.1%, Japan core CPI 2.2%, Phillips 118, the $120bn COP31 gap) and a
  proportional region bar.
- One full-width hero (Kyiv missile barrage), 4 illustrated cards, 8 small
  illustrated cards, a dot-grid world map with numbered pins, and 24 numbered
  briefs — every story attributed to its source (Reuters, AP, AFP, BBC, IMD,
  UN News, Al Jazeera, ICC, PBOC, ESA).
- DATE CHECK footer: stories first reported Thursday 19 November (Trump–Xi–
  Putin summit, ICJ Rohingya ruling, Anthropic IPO debut, GTA VI launch,
  Kerch Bridge strike, Senate Iran war-powers vote, Voyager 1) are explicitly
  excluded so the page is only 20 November's news.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. The image is 1024×1024, under 1 MiB, and identical on
every run.

The renderer that drew the image lives outside this repository; the image
itself is the deliverable, as the competition allows ("the simplest program
copies an image the repository holds").

## License

MIT — see LICENSE.
