<h1>Bus Route Villavicencio</h1>
<p>Author: Jorge A. Abella Betancourt - 160004300</p>
<p>Bus Route Villavicencio es un proyecto de sistemas distribuidos donde busca implementar una arquitectura de microservicios en k8s(minikube)</p>
</br>
<h2>Instalacion</h2>
<p>Para la instalacion de la aplicacion se debe correr el script de bash <strong>busroute.sh</strong></p>. Se debe de contar con <strong>minikube</strong> y <strong>kubectl</strong> para su correcta instalacion.</p>
</br>
<h2>Sobre la app</h2>
<p>La app actualmente se encuentra en un entorno de pruebas, utilizar una base de datos de pruebas <strong>sqlite3</strong>. Cuenta con datos quemados de prueba. Para el administrador de la app se utiliza el admin de django que se encuentra en el backend user: admin, password: 123</p>
<h3>Datos tecnicos</h3>
<p>Para el disenno de la app se opto por usar <strong>Django</strong> como tecnologia para el front y back. Aunque django no es un framework especializado para el front se soporto gran parte de la funcionalidad en <strong>Js</strong>.</p>

</br>
<h2>Repositorios de imagenes docker</h2>
<h3>Repositorio Front</h3>
<p><strong>back-image</strong> = jorgegorrito/busroutevillavicencioback:2.0</p>
<h3>Repositorio Back</h3>
<p><strong>front-image</strong>=jorgegorrito/busroutevillavicenciofront:3.0</p>