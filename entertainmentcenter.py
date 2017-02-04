import media
import fresh_tomatoes

#class instance code

lalaland= media.Movie("La La Land", "A story of an aspiring actress and"
                      " jazz musician who fall in love",
                      "http://www.impawards.com/2016/posters/la_la_land_ver4_xlg.jpg",
                      "128 minute run time","https://www.youtube.com/watch?v=0pdqf4P9M"
                      "B8", "Emma Stone and Ryan Gosling")


whiplash= media.Movie("Whiplash", "An aspiring drummer attends an elite music academy",
                      "http://www.flickeringmyth.com/wp-content/uploads/2015"
                      "/01/WHIPLASH_1SHEET.jpg", "107 minute run time", "https://www.you"
                      "tube.com/watch?v=7d_jQycdQGo", "Miles Teller and J.K."
                      " Simmons")

lion= media.Movie("Lion", "An Indian boy adopted by an Australian family returns"
                  " to India years later to find his birth family", "https://geek"
                  "ycheekyalwayssneaky.files.wordpress.com/2017/01/lion-movie-po"
                  "ster-dev-patel.jpg", "120 minute run time", "https://www.youtube.com"
                  "/watch?v=-RNI9o06vqo", " Dev Patel and Nicole Kidman")

swiss_army_man= media.Movie("Swiss Army Man", "A man stranded on a desert island"
                            " discovers and befriends a corpse and together they"
                            " embark on a journey to get home.", "http://cdn3-www"
                            ".comingsoon.net/assets/uploads/gallery/swiss-army-m"
                            "an/swa_86_online.jpg", "97 minute runtime", "https://www.yo"
                            "utube.com/watch?v=4v92gXetGqA", "Paul Dano and"
                            " Daniel Radcliffe")

les_mis=media.Movie("Les Miserables", "The classic broadway story of Jean val Jean"
                    " is brought to the big screen.", "http://static2.hypable.com/wp"
                    "-content/uploads/2012/09/les-miserables-movie-poster.jpg",
                    "Run time: 180 minutes", "https://www.youtube.com/watch?v=nQ10"
                    "YRA3VKI", "Hugh Jackman, Russell Crowe, Amanda Seyfried, Anne Hathaway"
                    "and Eddie Redmayne")

atonement=media.Movie("Atonement", "Ian McEwan's book is brought to the silver screen"
                      "in a story about the lasting ramifications of a single lie.",
                      "https://thoughttester.files.wordpress.com/2010/09/atonement11."
                      "jpg", "190 minute runtime", "https://www.youtube.com/watch?v=rk"
                      "VQwwPrr4c", "Kiera Knightley, James McAvoy, and Saiorse"
                      " Ronan")
                    

movies= [lalaland, whiplash, lion, swiss_army_man, les_mis, atonement]

fresh_tomatoes.open_movies_page(movies)


