(use '[clojure.string :only (split)])

(def data (slurp "input.txt"))

(defn do-mul [s]
    (* (Integer/parseInt (first (split (second (split s #"\(")) #","))) (Integer/parseInt (second (split (first (split s #"\)")) #",")))))

(defn solve-first [data s]
    (if (some? data) (solve-first (next data) (+ s (do-mul (first data)))) s))

(defn solve-second [data s do-add]
    (let [curr-data (first data)
          is-do (= curr-data "do()")
          is-dont (= curr-data "don't()")]
        (if (some? data)
            (solve-second
                (next data)
                (if (and do-add (not is-do) (not is-dont)) (+ s (do-mul (first data))) s)
                (if is-do true (if is-dont false do-add)))
            s)))

(println (solve-first (re-seq #"mul\([0-9]+\,[0-9]+\)" data) 0))
(println (solve-second (map #(first %) (re-seq #"(mul\([0-9]+\,[0-9]+\)|do\(\)|don\'t\(\))" data)) 0 true)) ; I'm getting vectors instead of string for some reason - hence the map
