// github.com guidance:
//    gradle/kotlin-dsl/blob/master/samples/hello-kotlin/build.gradle.kts
plugins {
  application
  kotlin("jvm") version "1.2.50"
}

application {
  mainClassName = "HelloKt"
}

dependencies {
  compile(kotlin("stdlib"))
}

repositories {
  jcenter()
}

// github.com guidance:
//    sureshg/kotlin-starter/blob/master/build.gradle.kts
defaultTasks("run")

