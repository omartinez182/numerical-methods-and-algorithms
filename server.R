
library(shiny)
library(reticulate)

source_python("algoritmos.py")

#tableOut, soluc = newtonSolverX(-5, "2x^5 - 3", 0.0001)

shinyServer(function(input, output) {
    
    #Evento y evaluación de metodo de newton para ceros
    newtonCalculate<-eventReactive(input$nwtSolver, {
        inputEcStr<-input$ecuacion[1]
        print(inputEcStr)
        initVal<-input$initVal[1]
        error<-input$Error[1]
        #outs<-add(initVal, error)
        outs<-newtonSolverX(initVal, inputEcStr, error)
        outs
    })
    
    #Evento y evaluación de diferencias finitas
    diferFinitCalculate<-eventReactive(input$diferFinEval, {
        inputEcStr<-input$difFinEcu[1]
        valX<-input$valorX[1]
        h<-input$valorH[1]
        outs<-evaluate_derivate_fx(inputEcStr, valX, h)
        as.character(outs)
    })
    
    #Evento y evaluación de diferencias finitas 2
    diferFinitCalculate2<-eventReactive(input$diferFinEval2, {
        inputEcStr2<-input$difFinEcu2[1]
        valX2<-input$valorX2[1]
        h2<-input$valorH2[1]
        print(inputEcStr2)
        outs2<-dif_fin_dos_puntos(inputEcStr2, valX2, h2)
        outs2
    })
    
    #Evento y evaluación de diferencias finitas 3
    diferFinitCalculate3<-eventReactive(input$diferFinEval3, {
        inputEcStr3<-input$difFinEcu3[1]
        valX3<-input$valorX3[1]
        h3<-input$valorH3[1]
        print(inputEcStr3)
        outs3<-dif_fin_tres_puntos(inputEcStr3, valX3, h3)
        outs3
    })
    
    #Evento integracion metodo trapezoide
    integTrap<-eventReactive(input$diferFinEval4, {
        inputEcStr4<-input$difFinEcu4[1]
        valA<-input$valorA[1]
        valB<-input$valorB[1]
        valN<-input$valorN[1]
        print(inputEcStr4)
        outs4<-trapezoide(inputEcStr4, valA, valB, valN)
        outs4
    })

    #Evento integracion metodo simpson
    integSimp<-eventReactive(input$diferFinEval5, {
        inputEcStr5<-input$difFinEcu5[1]
        valA2<-input$valorA2[1]
        valB2<-input$valorB2[1]
        valN2<-input$valorN2[1]
        print(inputEcStr5)
        outs5<-simpson(inputEcStr5, valA2, valB2, valN2)
        outs5
    })
    
    #Evento raiz de funcion por metodo Incremental Search
    raizISM<-eventReactive(input$diferFinEval6, {
        inputEcStr6<-input$difFinEcu6[1]
        valA3<-input$valorA3[1]
        valB3<-input$valorB3[1]
        print(inputEcStr6)
        outs6<-ISM(inputEcStr6, valA3, valB3)
        outs6
    })

    #Evento raiz de funcion por metodo de Biseccion
    raizBisection<-eventReactive(input$diferFinEval7, {
        inputEcStr7<-input$difFinEcu7[1]
        valA4<-input$valorA4[1]
        valB4<-input$valorB4[1]
        valC4<-input$valorC4[1]
        print(inputEcStr7)
        outs7<-bisection(inputEcStr7, valA4, valB4, valC4)
        outs7
    })
    
    #Evento raiz de funcion por metodo de Newton-Raphson
    raizNR<-eventReactive(input$diferFinEval8, {
        inputEcStr8<-input$difFinEcu8[1]
        valA5<-input$valorA5[1]
        valB5<-input$valorB5[1]
        print(inputEcStr8)
        outs8<-NR(inputEcStr8, valA5, valB5)
        outs8
    })
    
    
    #Evento FONC, SONC y SOSC
    condiciones<-eventReactive(input$diferFinEval9, {
        inputEcStr9<-input$difFinEcu9[1]
        valA6<-input$valorA6[1]
        valB6<-input$valorB6[1]
        valC6<-input$valorC6[1]
        valD6<-input$valorD6[1]
        print(inputEcStr9)
        outs9<-conditions(inputEcStr9, valA6, valB6, valC6, valD6)
        outs9
    })
    
    
    #Evento Steepest Descent
    steepest<-eventReactive(input$diferFinEval10, {
        inputEcStr10<-input$difFinEcu10[1]
        valA7<-input$valorA7[1]
        valB7<-input$valorB7[1]
        print(inputEcStr10)
        outs10<-sd(inputEcStr10, valA7, valB7)
        outs10
    })    

    #REnder metodo de Newton
    output$salidaTabla<-renderTable({
        newtonCalculate()
    })
    
    #Render Diferncias Finitas
    output$difFinitOut<-renderText({
        diferFinitCalculate()
    })
    
    #Render Diferncias Finitas 2
    output$difFinitOut2<-renderTable({
        diferFinitCalculate2()
    })
    
    #Render Diferncias Finitas 3
    output$difFinitOut3<-renderTable({
        diferFinitCalculate3()
    })
    
    #Render Integracion Trapezoide
    output$difFinitOut4<-renderText({
        integTrap()
    })
    
    #Render Integracion Trapezoide
    output$difFinitOut5<-renderText({
        integSimp()
    })

    #Render Raiz Incremental Search Method
    output$difFinitOut6<-renderText({
        raizISM()
    })

    #Render Raiz Bisection Method
    output$difFinitOut7<-renderText({
        raizBisection()
    })  
    
    #Render Raiz Newton-Raphson
    output$difFinitOut8<-renderText({
        raizNR()
    })
    
    #Render FONC, SONC y SOSC
    output$difFinitOut9<-renderText({
        condiciones()
    })
    
    #Render Steepest Descent
    output$difFinitOut10<-renderText({
        steepest()
    })
        
})
