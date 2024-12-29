;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname P1-Guimpel) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
; Práctica 1 de Programación 2 - Guimpel realizada
; en Racket adaptada a la materia Programación 1.
; ___________________________________________________
; Ejercicio 1 = Ejercicio 2 = Ejercicio 3:
;
; generar_lista : Natural Natural -> List(Natural)
; Recibe un x natural y un n natural, devuelve una
; lista con los primeros n naturales pares >= a x.
   (check-expect (generar_lista 0 25)
                 (list 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48))

(define (generar_lista x n)
  (cond
    [(zero? n) '()]
    [(even? x) (cons x (generar_lista (add1 x) (sub1 n)))]
    [else (generar_lista (add1 x) n)]))
; ___________________________________________________
; Ejercicio 4 = Ejercicio 5:
;
; sumar_primeros : Natural -> Natural
; Dado un n natural, devuelve la suma de
; los primeros n naturales.
   (check-expect (sumar_primeros 50) 1275)

(define (sumar_primeros n)
  (cond
    [(zero? n) n]
    [else (+ n (sumar_primeros (sub1 n)))]))
; ___________________________________________________
; Ejercicio 6:
;
; sumar_entre : Natural Natural -> Natural
; Dados dos naturales n y m, devuelve la suma
; de los naturales mayores que n y menores que m.
; Ejemplos:
   (check-expect (sumar_entre 5 4) 0) ; Si n > m -> 0
   (check-expect (sumar_entre 5 5) 0) ; Si n = m -> 0
   (check-expect (sumar_entre 5 6) 0) ; Si m-1 = n -> 0
   (check-expect (sumar_entre 5 10) 30) ; Si n < (m-1) -> (m-1) + sumar_entre(n (m-1))

(define (sumar_entre n m)
  (cond
    [(>= n (sub1 m)) 0]
    [else (+ (sub1 m) (sumar_entre n (sub1 m)))]))
; ___________________________________________________
; Ejercicio 7:
;
; duplicar : String -> String
; Dado un String devuelve el resultado
; de concatenarlo consigo mismo.
; Ejemplo:
   (check-expect (duplicar "Tobias") "TobiasTobias")

(define (duplicar s)
  (string-append s s))
; ___________________________________________________
; Ejercicio 8:
; duplicar_veces : String Natural -> List(String)
; Dado un String y un numero n devuelve el una lista
; de n strings s. Ejemplo:
   (check-expect (duplicar_veces "Tobias" 3) (list "Tobias" "Tobias" "Tobias"))

(define (duplicar_veces s n)
  (cond
    [(= n 0) '()]
    [else (cons s (duplicar_veces s (sub1 n)))]))

   (check-expect (concatenar_lista (list "Tobias" "Tobias" "Tobias")) "TobiasTobiasTobias")
(define (concatenar_lista l)
  (cond
    [(empty? l) ""]
    [else (string-append (first l) (concatenar_lista (rest l)))]))

