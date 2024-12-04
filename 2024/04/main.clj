; TODO - does not work - write out using python as example
(ns lv.kristapsbe.adventofcode)
(def data (mapv #(clojure.string/split % #"") (clojure.string/split-lines (slurp "test.txt"))))

(def xmas ["X", "M", "A", "S"])
(def dirs [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]])
(def h (count data))
(def w (count (first data)))

(defn find-xmas [i, j, xmas, dir]
    (if (some? xmas)
        (if (and (>= i 0) (< i h) (>= j 0) (< j w) (= (get-in data [i j]) (first xmas))
            (find-xmas (+ i (first dir)) (+ j (second dir)) (next xmas) dir)
            (0))
        (1))))

(println data)
(println (for [i (range h)  j (range w)] (vector i j))) ; this doesn't seem right
