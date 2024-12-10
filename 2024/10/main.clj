(ns lv.kristapsbe.adventofcode)

(defn cast-values [f coll]
    (mapv (fn [s] (if (vector? s) (cast-values f s) (f s))) coll))

(def data (mapv #(clojure.string/split % #"") (clojure.string/split-lines (slurp "test.txt"))))
(def idata (cast-values Integer/parseInt data))

(defn find-trails [coll i j c r do-check]
    (let [nc (inc c)] (println nc)))

(println (find-trails idata 0 0 0 [] true))
(println (vec (map-indexed (fn [i x] (println i x)) idata)))
