(ns lv.kristapsbe.adventofcode)
(use '[clojure.string :only (split)])

(defn get-inputs [file-path]
    (let [lines (clojure.string/split-lines (slurp file-path))
        rule_strings (filter #(.contains % "|") lines)
        update_strings (filter #(.contains % ",") lines)
        rules (map #(split % #"\|") rule_strings)
        updates (map #(split % #",") update_strings)
        ] [rules, updates]))

(defn solve-first [rules updates]
    (println rules))

(def inputs (get-inputs "test.txt"))
(solve-first (first inputs) (second inputs))
