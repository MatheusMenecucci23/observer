Deve-se desenvolver um sistema para uma estação de meteorologia (Weather Station) que gerencia a temperatura.<br>
O sistema deve ser modularizado, isto é, deve existir dois módulos independentes que fazem o seguinte:
Módulo 1 - responsável por dar um display na temperatura sempre que ela for alterada
Módulo 2 - responsável por exibir estatísticas da temperatura sempre que ela mudar
O sistema deve ser implementado de forma que outros módulos possam ser facilmente acoplados se necessário
Tratar o problema da seguinte forma: O módulo principal, isto é, o sistema em si é o módulo de meteorologia WeatherStation, o qual gerencia a temperatura. Mudanças de temperatura devem então ser monitoradas e observadas por vários módulos, subsistemas, componentes,etc. Na versão atual, há somente dois módulos interessados.
No Main
Instancie somente uma WeatherStation
Acople dois observadores nessa WeatherStation
Altere a temperatura três vezes para ver se funciona
Segunda versão do Main
Instancie duas WeatherStations
Acople os dois observadores na primeira WeatherStation
Acople somente o observador de Display na segunda WeatherStation
Mude o estado → altere a temperatura para as duas estações meteorológicas
