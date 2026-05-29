# Spring Boot基础学习

## Spring Boot概述

Spring Boot是Spring提供的一个子项目，用于快速构建Spring应用程序。

Spring Boot的特性：

+ 起步依赖：本质上是一个Maven坐标，整合了完成一个功能需要的所有坐标，如`spring-boot-starter-web`
+ 自动配置：遵循约定大于配置的原则，在boot程序启动后，一些bean对象会自动注入到IOC容器，不需要手动声明，简化开发
+ 其他特性：如内嵌Tomcat、Jetty（无需部署war文件），外部化配置，不需要xml配置（使用properties/yml文件）

## Spring Boot入门

实现一个简单的web应用：在浏览器输入“localhost:8080/hello”返回字符串“hello”。

1. 创建一个Maven工程
2. 导入spring-boot-starter-web起步依赖
3. 编写Controller
4. 提供启动类

*注：Spring Boot工程都需要直接或间接继承父工程“spring-boot-starter-parent”，用于管理起步依赖的版本号。当然有的依赖版本需要自己指定。*

## 配置文件

Spring Boot提供两种形式的配置文件：properties和yaml

Spring Boot官方关于应用配置的文档：[Common Application Properties (spring.io)](https://docs.spring.io/spring-boot/docs/current/reference/html/application-properties.html#appendix.application-properties.core)

### properties配置文件

```properties
server.port=8080
```



### yaml配置文件

```yaml
server:
  port: 8080
```



## Bean管理

### Bean扫描

+ @ComponentScan：默认扫描使用该注解的类所在的包及其子包。如需扫描其他包，需指明要扫描的包，如:`@ComponentScan(basePackage = 'com.xxx.xxx')`

  *@SpringBootApplication由@SpringBootConfiguration、@EnableAutoConfiguration、@ComponentScan这三个注解修饰，所以SpringBoot工程默认扫描启动类所在的包及其子包。*

### Bean注册

一般使用如下注解将Bean注入到IOC容器：

+ @Component：这是声明bean的基础注解，通常是当Bean不属于其他类型时，用此注解。
+ @Controller：是@Component的衍生注解，用于标注在控制器类上。
+ @Service：也是@Component的衍生注解，用于标注在业务类上。
+ @Repository：同样是@Component的衍生注解，用于标注在数据访问类上（由于与mybatis整合，用的少）

***如果要注册的Bean对象来自于第三方（不是自定义的），是无法使用@Component及衍生注解声明Bean的。***需要使用这两个注解：@Bean和@Import。

+ @Bean
  + 用于启动类内部的方法上（不推荐，因为不建议在启动类内部做过多操作）：将方法返回值（一般是某个类的对象）注入IOC容器。获取的bean对象名默认为方法名。
  + 用于配置类内部的方法上（该类用@Configuration注解声明为配置类，并且位于启动类的包或子包下）：将方法返回值（一般是某个类的对象）注入IOC容器。获取的bean对象名默认为方法名。
+ @Import用在启动类上，使用方式：`@Import(Xxx.class)`，Xxx为类名，即此注解的属性是字节码。如果要导入多个类，则使用数组形式：`@Import({Xxx1.class,Xxx2.class})`。
  + 导入配置类（此时配置类不在启动类所在的包及子包下）。
  + 导入ImportSelector接口实现类：实现的selectImports方法中，返回以要导入类的全限定名（如com.example.Xxx)为元素的String数组。
  + 自定义注解，如@EableXxxx注解，其本质上是对@Import注解的封装，再在启动类上使用自定义注解@EnableXxxx。

### 注册条件

Spring Boot提供了设置注册生效条件的注解@Conditional

三个常用的条件注解：

+ @ConditionalOnProperty：判断配置文件中是否有对应属性和值才初始化Bean
+ @ConditionalOnClass：判断环境中是否有对应字节码文件（类）才初始化Bean
+ @  ConditionalOnMissingBean：判断环境中没有对应Bean才初始化Bean

## 自动配置原理

自动配置：遵循“约定大于配置”的原则，在boot程序启动后，起步依赖中的一些bean对象会自动注入到Ioc容器。

### 源码分析

@SpringBootApplication注解使用了@EnableAutoConfiguration注解，而@EnableAutoConfiguration注解内部使用`@Import({AutoConfigurationImportSelector.class})`来加载配置类。在AutoConfigurationImportSelector中实现了selectImports方法，该方法通过层层调用，读取了位于"META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports"的配置文件（Spring Boot 2.7版本之前读取的是spring.factories文件），该配置文件中编写了大量类的全限定名，这些类都是定义好的配置类（这些配置类还通过@Conditional及其衍生注解实现Bean的条件注册），当SpringBoot应用启动时，会自动加载这些配置类，初始化Bean，注入到IOC容器中。

## 自定义starter

1. 创建一个自定义的项目模块，如xxxx-spring-boot-autoconfigure，该模块提供自动配置功能，并自定义配置文件`META-INF/spring/xxxxx.imports`。
2. 创建一个自定义的项目模块，如xxxx-spring-boot-starter模块，在该starter模块中引入自动配置模块，即1中的模块。此模块提供依赖管理的功能。