(ns lv.kristapsbe.advent)

(defn get-input [file-path]
    (let [lines (slurp file-path)
          columns (mapv #(clojure.string/split % #"\s+") (clojure.string/split-lines lines))
        ] columns))

(defn solve-first [col1 col2]
    (apply + (map #(Math/abs (- %1 %2)) col1 col2)))

(defn solve-second [col1 col2]
    (apply + (map #(* % (get col2 % 0)) col1)))

(def columns (get-input "input.txt"))
(def col1 (map #(Integer/parseInt %) (map first columns)))
(def col2 (map #(Integer/parseInt %) (map second columns)))
(println (solve-first (sort col1) (sort col2)))
(println (solve-second (distinct col1) (frequencies col2)))
