(ns lv.kristapsbe.advent)

(defn get-input [file-path]
    (let [lines (slurp file-path)
          data (mapv #(clojure.string/split % #"\s+") (clojure.string/split-lines lines))
        ] data))

(defn cast-values [f coll]
    (mapv (fn [s] (if (vector? s) (cast-values f s) (f s))) coll))

(defn calculate-adj [e coll v]
    (if (some? coll) (calculate-adj (first coll) (next coll) (conj v (- (first coll) e))) v))

(defn is-safe [coll]
    (if (= (abs (apply + (map #(if (and (> (abs %) 0) (< (abs %) 4)) (max (min % 1) -1) 0) coll))) (count coll)) 1 0))

(defn vec-remove [pos coll]
    (into (subvec coll 0 pos) (subvec coll (inc pos))))

(defn add-part-two-options [ct coll v]
    (let [next-ct (inc ct)]
        (if (= ct (count coll)) v (add-part-two-options next-ct coll (conj v (vec-remove ct coll))))))

(defn any-safe [row]
    (apply max (map #(is-safe (calculate-adj (first %) (next %) [])) row)))

(def data (cast-values Integer/parseInt (get-input "input.txt")))
(def adj (map #(calculate-adj (first %) (next %) []) data))
(println (apply + (map is-safe adj))) ; part one
(def part-two-data (map #(add-part-two-options 0 % [%]) data))
(println (apply + (map any-safe part-two-data))) ; part two
