(ns lv.kristapsbe.advent)

(defn get-input [file-path]
    (let [lines (slurp file-path)
          data (mapv #(clojure.string/split % #"\s+") (clojure.string/split-lines lines))
        ] data))

(defn cast-values [f data]
    (mapv (fn [s] (if (vector? s) (cast-values f s) (f s))) data))

(defn calculate-adj [ct entry v]
    (let [next-ct (inc ct)]
         (if (= next-ct (count entry)) v (calculate-adj next-ct entry (conj v (- (nth entry next-ct) (nth entry ct)))))))

(defn is-safe [entry]
    (if (= (abs (apply + (map #(if (and (> (abs %) 0) (< (abs %) 4)) (max (min % 1) -1) 0) entry))) (count entry)) 1 0))

(defn vec-remove [pos entry]
    (into (subvec entry 0 pos) (subvec entry (inc pos))))

(defn add-part-two-options [ct entry v]
    (let [next-ct (inc ct)]
        (if (= ct (count entry)) v (add-part-two-options next-ct entry (conj v (vec-remove ct entry))))))

(defn any-safe [row]
    (apply max (map #(is-safe (calculate-adj 0 % [])) row)))

(def data (cast-values Integer/parseInt (get-input "input.txt")))
(def adj (map #(calculate-adj 0 % []) data))
(println (apply + (map is-safe adj))) ; part one
(def part-two-data (map #(add-part-two-options 0 % [%]) data))
(println (apply + (map any-safe part-two-data))) ; part two
