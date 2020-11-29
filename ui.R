library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
    dashboardSidebar(
        sidebarMenu(
            menuItem("Ceros", tabName = "Ceros"),
            menuItem("Derivacion", tabName = "Derivacion"),
            menuItem("Diferencias", tabName = "Diferencias"),
            menuItem("DiferenciasExtra", tabName = "DiferenciasExtra"),
            menuItem("IntegracionTrapezoide", tabName = "IntegracionTrapezoide"),
            menuItem("IntegracionSimpson", tabName = "IntegracionSimpson"),
            menuItem("IncrementalSearch", tabName = "IncrementalSearch"),
            menuItem("Bisection", tabName = "Bisection"),
            menuItem("Newton-Raphson", tabName = "Newton-Raphson"),
            menuItem("FONCSON SOSC", tabName = "FONCSONCSOSC"),
            menuItem("Steepest Descent", tabName = "Steepest")
        )
    ),
    dashboardBody(
        tabItems(
            tabItem("Ceros",
                    h1("Metodo de Newton"),
                    box(textInput("ecuacion", "Ingrese la Ecuacion"),
                        textInput("initVal", "X0"),
                        textInput("Error", "Error")),
                    actionButton("nwtSolver", "Newton Solver"),
                    tableOutput("salidaTabla")),
            
            tabItem("Derivacion",
                    h1("Diferencias Finitas"),
                    box(textInput("difFinEcu", "Ingrese la Ecuacion"),
                    textInput("valorX", "x"),
                    textInput("valorH", "h")),
                    actionButton("diferFinEval", "Evaluar Derivada"),
                    textOutput("difFinitOut")),
            
            tabItem("Diferencias",
                    h1("Diferencias Finitas Derivation"),
                    box(textInput("difFinEcu2", "Ingrese la Ecuacion"),
                        textInput("valorX2", "x"),
                        textInput("valorH2", "h")),
                    actionButton("diferFinEval2", "Evaluar Derivada"),
                    tableOutput("difFinitOut2")),
            
            tabItem("DiferenciasExtra",
                    h1("Diferencias Finitas Derivation Extra"),
                    box(textInput("difFinEcu3", "Ingrese la Ecuacion"),
                        textInput("valorX3", "x"),
                        textInput("valorH3", "h")),
                    actionButton("diferFinEval3", "Evaluar Derivada"),
                    tableOutput("difFinitOut3")),
            
            tabItem("IntegracionTrapezoide",
                    h1("Integracion Matematica por Metodo de Trapezoide"),
                    box(textInput("difFinEcu4", "Ingrese la Ecuacion"),
                        textInput("valorA", "a"),
                        textInput("valorB", "b"),
                        textInput("valorN", "n")),
                    actionButton("diferFinEval4", "Evaluar Integral"),
                    textOutput("difFinitOut4")),
            
            tabItem("IntegracionSimpson",
                    h1("Integracion Matematica por Metodo de Simpson"),
                    box(textInput("difFinEcu5", "Ingrese la Ecuacion"),
                        textInput("valorA2", "a"),
                        textInput("valorB2", "b"),
                        textInput("valorN2", "n")),
                    actionButton("diferFinEval5", "Evaluar Integral"),
                    textOutput("difFinitOut5")),
            
            tabItem("IncrementalSearch",
                    h1("Raiz de una Funcion por el Metodo Incremental Search"),
                    box(textInput("difFinEcu6", "Ingrese la Funcion"),
                        textInput("valorA3", "x0"),
                        textInput("valorB3", "Delta x")),
                    actionButton("diferFinEval6", "Evaluar Funcion"),
                    textOutput("difFinitOut6")),
            
            tabItem("Bisection",
                    h1("Raiz de una Funcion por el Metodo Bisection"),
                    box(textInput("difFinEcu7", "Ingrese la Funcion"),
                        textInput("valorA4", "Epsilon"),
                        textInput("valorB4", "Intervalo desde"),
                        textInput("valorC4", "Intervalo hasta")),
                    actionButton("diferFinEval7", "Evaluar Funcion"),
                    textOutput("difFinitOut7")),
            
            tabItem("Newton-Raphson",
                    h1("Raiz de una Funcion por el Metodo Newton-Raphson"),
                    box(textInput("difFinEcu8", "Ingrese la Funcion"),
                        textInput("valorA5", "Epsilon"),
                        textInput("valorB5", "Punto inicial")),
                    actionButton("diferFinEval8", "Evaluar Funcion"),
                    textOutput("difFinitOut8")),
            
            tabItem("FONCSONCSOSC",
                    h1("Condiciones de Optimalidad"),
                    box(textInput("difFinEcu9", "Ingrese la Funcion"),
                        textInput("valorA6", "Ingrese valor de las variables"),
                        textInput("valorB6", "Primer vector del hessiano"),
                        textInput("valorC6", "Segundo vector del hessiano"),
                        textInput("valorD6", "Tercer vector del hessiano")),
                    actionButton("diferFinEval9", "Evaluar Funcion"),
                    textOutput("difFinitOut9")),
            
            tabItem("Steepest",
                    h1("Calcular el minimo de una funcion"),
                    box(textInput("difFinEcu10", "Ingrese la Funcion"),
                        textInput("valorA7", "Ingrese los puntos iniciales"),
                        textInput("valorB7", "Ingrese el valor de epsilon")),
                    actionButton("diferFinEval10", "Evaluar Funcion"),
                    textOutput("difFinitOut10"))
            
        )
    )
)