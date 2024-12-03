(use '[clojure.string :only (split)])

(def data (slurp "input.txt"))

(defn do-mul [s]
    (* (Integer/parseInt (first (split (second (split s #"\(")) #","))) (Integer/parseInt (second (split (first (split s #"\)")) #",")))))

(defn solve-first [data s]
    (if (some? data) (solve-first (next data) (+ s (do-mul (first data)))) s))

(println (solve-first (re-seq #"mul\([0-9]+\,[0-9]+\)" data) 0))
