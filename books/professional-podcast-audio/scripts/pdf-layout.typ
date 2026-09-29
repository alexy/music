#set page(width: 7in, height: 10in, margin: (x: 0.62in, y: 0.65in))
#set par(justify: false, leading: 0.55em)
#set text(size: 11pt, fill: rgb("#172b3a"))
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  block(above: 0.5em, below: 1em)[
    #text(size: 23pt, weight: "bold", fill: rgb("#087f8c"))[#it.body]
  ]
}
#show heading.where(level: 2): set text(size: 15pt, fill: rgb("#b24a31"))
#show heading.where(level: 3): it => {
  pagebreak(weak: true)
  block(above: 0.3em, below: 0.7em)[#text(size: 15pt, weight: "bold", fill: rgb("#172b3a"))[#it.body]]
}
#show figure.caption: set text(size: 9pt, fill: rgb("#526372"))
#show table: set text(size: 9pt)
#set table(stroke: (bottom: 0.35pt + rgb("#cbdadf")), inset: (x: 5pt, y: 3pt))
#show raw: set text(size: 9pt)

#show link: set text(fill: rgb("#087f8c"))
