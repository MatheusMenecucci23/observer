<h1>Deve-se desenvolver um sistema para uma estação de meteorologia (Weather Station) que gerencia a temperatura.</h1><br>
O sistema deve ser modularizado, isto é, deve existir dois módulos independentes que fazem o seguinte:<br>
Módulo 1 - responsável por dar um display na temperatura sempre que ela for alterada<br>
Módulo 2 - responsável por exibir estatísticas da temperatura sempre que ela mudar<br>
O sistema deve ser implementado de forma que outros módulos possam ser facilmente acoplados se necessário<br>
Tratar o problema da seguinte forma: O módulo principal, isto é, o sistema em si é o módulo de meteorologia WeatherStation, o qual gerencia a temperatura. Mudanças de temperatura devem então ser monitoradas e<br> observadas por vários módulos, subsistemas, componentes,etc. Na versão atual, há somente dois módulos interessados.<br>
No Main<br>
Instancie somente uma WeatherStation<br>
Acople dois observadores nessa WeatherStation<br>
Altere a temperatura três vezes para ver se funciona<br>
<h1>Segunda versão do Main</h1><br>
Instancie duas WeatherStations<br>
Acople os dois observadores na primeira WeatherStation<br>
Acople somente o observador de Display na segunda WeatherStation<br>
Mude o estado → altere a temperatura para as duas estações meteorológicas<br>
