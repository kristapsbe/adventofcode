(use '[clojure.string :only (split)])

(def data (slurp "input.txt"))

(defn do-mul [s]
    (* (Integer/parseInt (first (split (second (split s #"\(")) #","))) (Integer/parseInt (second (split (first (split s #"\)")) #",")))))

(defn solve-first [coll s]
    (if (some? coll) (solve-first (next coll) (+ s (do-mul (first coll)))) s))

(defn solve-second [coll s do-add]
    (let [curr-data (first coll)
          is-do (= curr-data "do()")
          is-dont (= curr-data "don't()")]
        (if (some? coll)
            (solve-second
                (next coll)
                (if (and do-add (not is-do) (not is-dont)) (+ s (do-mul (first coll))) s)
                (if is-do true (if is-dont false do-add)))
            s)))

(println (solve-first (re-seq #"mul\([0-9]+\,[0-9]+\)" data) 0))
(println (solve-second (map #(first %) (re-seq #"(mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\))" data)) 0 true)) ; I'm getting vectors instead of string for some reason - hence the map
