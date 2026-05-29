# Spring Framework学习笔记

***阅读官网Spring Framework（version：6.2.7）参考文档***

**从Spring Framework6.0开始，Spring需要Java17及以上版本**

**Spring Framework是Spring项目的基础，它被分为许多的模块，应用程序可以选择它们需要的模块。核心是核心容器的模块（包括配置模型、依赖注入机制），Spring Framework还为不同的应用程序架构提供基础支持，包括消息传递、事务数据和持久性以Web。还有基于Servlet的Spring MVC的Web框架，以及并行的Spring WebFlux反应式的Web框架。**

**Spring于2003年出现，是作为早期应对复杂性J2EE规范的“新实践”，它和Java EE以及继任者Jakarta EE早期可能存在竞争，但同时它们也是互补的。Spring编程模型从传统的EE全体中选择单个的规范。**

## 设计思想

> Provide choice at every level. Spring lets you defer design decisions as late as possible. For example, you can switch persistence providers through configuration without changing your code. The same is true for many other infrastructure concerns and integration with third-party APIs.

+ 在各层级提供选择。如持久层框架、其他基础设施关注以及第三方API等。

> Accommodate diverse perspectives. Spring embraces flexibility and is not opinionated about how things should be done. It supports a wide range of application needs with different perspectives.

+ 容纳不同的观点。Spring本身拥抱灵活性，并不会对如何做事固执己见。它以不同角度支持广泛的应用程序需求。

> Maintain strong backward compatibility. Spring’s evolution has been carefully managed to force few breaking changes between versions. Spring supports a carefully chosen range of JDK versions and third-party libraries to facilitate maintenance of applications and libraries that depend on Spring.

+ 保持强大的向后兼容性。Spring的演变经过了精心管理，版本之间几乎没有破环性变化。Spring支持一系列精心挑选的JDK版本和第三方库，以便维护依赖于Spring的应用程序和库。

> Care about API design. The Spring team puts a lot of thought and time into making APIs that are intuitive and that hold up across many versions and many years.

+ 注重API设计。Spring团队投入时间和精力来制作直观的API，这些API可以跨多个版本和多年使用。

> Set high standards for code quality. The Spring Framework puts a strong emphasis on meaningful, current, and accurate javadoc. It is one of very few projects that can claim clean code structure with no circular dependencies between packages.

+ 为代码质量设置高标准。Spring强调有意义、最新和准确的javadoc文档，它有干净的代码结构且包之间没有循环依赖关系。



## 官网文档阅读随记

### 核心技术

#### IOC

##### 概览

> This chapter covers the Spring Framework implementation of the Inversion of Control (IoC) principle. Dependency injection (DI) is a specialized form of IoC, whereby objects define their dependencies (that is, the other objects they work with) only through constructor arguments, arguments to a factory method, or properties that are set on the object instance after it is constructed or returned from a factory method. The IoC container then injects those dependencies when it creates the bean. This process is fundamentally the inverse (hence the name, Inversion of Control) of the bean itself controlling the instantiation or location of its dependencies by using direct construction of classes or a mechanism such as the Service Locator pattern.

总结：依赖注入（Dependency Injection，DI）是IOC的一种特殊形式。对象通过构造函数参数、工厂方法的参数，或者在对象实例被构造或从工厂方法返回对象实例后在对象实例上设置属性来定义其依赖项（即它们使用的其他对象）。IoC容器在创建bean时注入这些依赖。这个过程从根本上说是bean本身的逆向（因此得名，可控制反转），通过使用类的直接构造或诸如Service Locator（服务定位器）模式之类的机制来控制bean的依赖项的实例化或位置。

> The `org.springframework.beans` and `org.springframework.context` packages are the basis for Spring Framework’s IoC container. The [`BeanFactory`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/beans/factory/BeanFactory.html) interface provides an advanced configuration mechanism capable of managing any type of object. [`ApplicationContext`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/context/ApplicationContext.html) is a sub-interface of `BeanFactory`. It adds:
>
> + Easier integration with Spring’s AOP features
> + Message resource handling (for use in internationalization)
> + Event publication
> + Application-layer specific contexts such as the `WebApplicationContext` for use in web applications.
>
> In short, the `BeanFactory` provides the configuration framework and basic functionality, and the `ApplicationContext` adds more enterprise-specific functionality. The `ApplicationContext` is a complete superset of the `BeanFactory` and is used exclusively in this chapter in descriptions of Spring’s IoC container. For more information on using the `BeanFactory` instead of the `ApplicationContext,` see the section covering the [`BeanFactory` API](https://docs.spring.io/spring-framework/reference/core/beans/beanfactory.html).

总结：`org.springframework.beans`和`org.springframework.context`包是Spring Framework的IoC容器的基础，其中的`BeanFactory`接口提供一种高级的配置机制能够管理各种类型的对象，`ApplicationContext`是`BeanFactory`的子接口。`ApplicationContext`接口是`BeanFactory`接口的完整超集，它添加了更多特定于企业所需的功能，而`BeanFactory`仅提供配置框架和基本功能。

> In Spring, the objects that form the backbone of your application and that are managed by the Spring IoC container are called beans. A bean is an object that is instantiated, assembled, and managed by a Spring IoC container. Otherwise, a bean is simply one of many objects in your application. Beans, and the dependencies among them, are reflected in the configuration metadata used by a container.

总结：在Spring中，构成应用程序并由Spring IoC容器管理的对象称为`bean`。`bean`是由Spring IoC容器实例化、组装和管理的对象。一个`bean`仅是应用程序中许多对象中的一个。Beans和它们之间的依赖关系被反映在容器使用的配置元数据中。

> The `org.springframework.context.ApplicationContext` interface represents the Spring IoC container and is responsible for instantiating, configuring, and assembling the beans. The container gets its instructions on the components to instantiate, configure, and assemble by reading configuration metadata. The configuration metadata can be represented as annotated component classes, configuration classes with factory methods, or external XML files or Groovy scripts. With either format, you may compose your application and the rich interdependencies between those components.

总结：`org.springframework.context.ApplicationContext`接口表示Spring IoC容器，负责实例化、管理、和组装beans。容器通过读取配置元数据来获取有关组件实例化、配置和组装的说明。配置元数据可以表示为被注解的类，有工厂方法的配置类、或者外部XML文件或`Groovy`脚本。无论使用哪种格式，都可以编写应用程序以及这些组件之间丰富的相互依赖关系。

> Several implementations of the `ApplicationContext` interface are part of core Spring. In stand-alone applications, it is common to create an instance of [`AnnotationConfigApplicationContext`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/context/annotation/AnnotationConfigApplicationContext.html) or [`ClassPathXmlApplicationContext`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/context/support/ClassPathXmlApplicationContext.html).
>
> In most application scenarios, explicit user code is not required to instantiate one or more instances of a Spring IoC container. For example, in a plain web application scenario, a simple boilerplate web descriptor XML in the `web.xml` file of the application suffices (see [Convenient ApplicationContext Instantiation for Web Applications](https://docs.spring.io/spring-framework/reference/core/beans/context-introduction.html#context-create)). In a Spring Boot scenario, the application context is implicitly bootstrapped for you based on common setup conventions.

总结：`Application`的一些实现是Spring核心的一部分。在独立的应用程序中，通常会创建一个`AnnotationConfigApplicationContext`或`ClassPathXmlApplicationContext`。但是在大多数的应用场景中，并不需要用户代码显式地实例化Spring IoC容器的一个或多个实例。

> The following diagram shows a high-level view of how Spring works. Your application classes are combined with configuration metadata so that, after the `ApplicationContext` is created and initialized, you have a fully configured and executable system or application.
>
> ![Spring IoC容器](.\images\Spring IoC容器01.png)

总结：从高层的角度看Spring IoC容器工作的原理，就是将编写的应用程序类和配置元数据相结合后，在创建并初始化`ApplicationContext`之后，就拥有了一个完全配置且可执行的系统或应用程序。

> As the preceding diagram shows, the Spring IoC container consumes a form of configuration metadata. This configuration metadata represents how you, as an application developer, tell the Spring container to instantiate, configure, and assemble the components in your application.

总结：Spring IoC容器使用一种形式的配置元数据，配置元数据表示作为应用开发者告诉Spring容器如何实例化、配置和组装应用程序中的组件。

> The Spring IoC container itself is totally decoupled from the format in which this configuration metadata is actually written. These days, many developers choose [Java-based configuration](https://docs.spring.io/spring-framework/reference/core/beans/java.html) for their Spring applications:
>
> + [Annotation-based configuration](https://docs.spring.io/spring-framework/reference/core/beans/annotation-config.html): define beans using annotation-based configuration metadata on your application’s component classes.
> + [Java-based configuration](https://docs.spring.io/spring-framework/reference/core/beans/java.html): define beans external to your application classes by using Java-based configuration classes. To use these features, see the [`@Configuration`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/context/annotation/Configuration.html), [`@Bean`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/context/annotation/Bean.html), [`@Import`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/context/annotation/Import.html), and [`@DependsOn`](https://docs.spring.io/spring-framework/docs/6.2.7/javadoc-api/org/springframework/context/annotation/DependsOn.html) annotations.

总结：Spring IoC容器本身和实际写入的配置元数据格式是完全解耦的。今天，许多的开发者在他们的Spring应用程序中选择基于Java的配置：

+ 基于注解的配置：在应用程序的组件类上使用基于注解的配置元数据定义beans。
+ 基于Java的配置：使用基于Java的配置类定义应用程序的外部beans，如`@Configuration`、`@Bean`、`@Import`和`@DependsOn`注解。

> Spring configuration consists of at least one and typically more than one bean definition that the container must manage. Java configuration typically uses `@Bean`-annotated methods within a `@Configuration` class, each corresponding to one bean definition.
>
> These bean definitions correspond to the actual objects that make up your application. Typically, you define service layer objects, persistence layer objects such as repositories or data access objects (DAOs), presentation objects such as Web controllers, infrastructure objects such as a JPA `EntityManagerFactory`, JMS queues, and so forth. Typically, one does not configure fine-grained domain objects in the container, because it is usually the responsibility of repositories and business logic to create and load domain objects.

总结：Spring配置由容器必须管理的至少一个（通常多个）的bean定义组成。Java配置通常在一个`@Configurationn`类中使用带`@Bean`注解的方法，每个方法对应于一个`bean`定义。这些`Bean`定义对应于组成应用程序的实际对象。

通常，可以定义服务层对象、持久层对象（如存储库或数据访问库对象——`DAO`）、表示对象（如Web控制器——`Controller`）、基础架构对象（如JPA `EntityManagerFactory`）、JMS队列等。但是通常不会在容器中配置细粒度的域`domain`对象，因为创建和加载域`domain`对象通常是存储库和业务逻辑的责任。

> XML-based configuration metadata configures these beans as `<bean/>` elements inside a top-level `<beans/>` element. The following example shows the basic structure of XML-based configuration metadata:
>
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <beans xmlns="http://www.springframework.org/schema/beans"
> 	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
> 	xsi:schemaLocation="http://www.springframework.org/schema/beans
> 		https://www.springframework.org/schema/beans/spring-beans.xsd">
> 
> 	<bean id="..." class="...">
> 		<!-- collaborators and configuration for this bean go here -->
> 	</bean>
> 
> 	<bean id="..." class="...">
> 		<!-- collaborators and configuration for this bean go here -->
> 	</bean>
> 
> 	<!-- more bean definitions go here -->
> 
> </beans>
> ```
>
> 1. The `id` attribute is a string that identifies the individual bean definition.
> 2. The `class` attribute defines the type of the bean and uses the fully qualified class name.
>
> The value of the `id` attribute can be used to refer to collaborating objects. The XML for referring to collaborating objects is not shown in this example. See [Dependencies](https://docs.spring.io/spring-framework/reference/core/beans/dependencies.html) for more information.

总结：基于XML的配置元数据将这些`bean`作为顶级元素`<beans/>`内部的`<bean/>`元素进行配置。`<bean/>`元素有两个属性——`id`和`name`，`id`使用字符串唯一标识一个bean定义，`name`通过使用类的完全限定名称定义了bean的类型。`id`属性的值可用于引用协作对象。

> For instantiating a container, the location path or paths to the XML resource files need to be supplied to a `ClassPathXmlApplicationContext` constructor that let the container load configuration metadata from a variety of external resources, such as the local file system, the Java `CLASSPATH`, and so on.
>
> ```java
> ApplicationContext context = new ClassPathXmlApplicationContext("services.xml", "daos.xml");
> ```
>
> 

总结：为了实例化容器，需要在`ClassPathXmlApplicationContext`的构造函数中指定XML源文件的路径，以让容器从外部源加载配置元数据，例如本地文件系统、Java的`CLASSPATH`等等。

> It can be useful to have bean definitions span multiple XML files. Often, each individual XML configuration file represents a logical layer or module in your architecture.
>
> You can use the `ClassPathXmlApplicationContext` constructor to load bean definitions from XML fragments. This constructor takes multiple `Resource` locations, as was shown in the [previous section](https://docs.spring.io/spring-framework/reference/core/beans/basics.html#beans-factory-xml). Alternatively, use one or more occurrences of the `<import/>` element to load bean definitions from another file or files. The following example shows how to do so:
>
> ```xml
> <beans>
> 	<import resource="services.xml"/>
> 	<import resource="resources/messageSource.xml"/>
> 	<import resource="/resources/themeSource.xml"/>
> 
> 	<bean id="bean1" class="..."/>
> 	<bean id="bean2" class="..."/>
> </beans>
> ```
>
> 

总结：通常为应用结构中的一个逻辑层或模块配置一个XML配置文件，然后让容器扫描多个XML文件来获取Bean的定义（使用`ClassPathXmlApplicationContext`的构造函数加载XML文件）。可选地，使用一个或多个`<import/>`元素从其他的文件加载bean定义，`ClassPathXmlApplicationContext`就可以只加载使用`<import/>`元素的XML文件。

> The `ApplicationContext` is the interface for an advanced factory capable of maintaining a registry of different beans and their dependencies. By using the method `T getBean(String name, Class<T> requiredType)`, you can retrieve instances of your beans.
>
> The `ApplicationContext` lets you read bean definitions and access them, as the following example shows:
>
> ```java
> // create and configure beans
> ApplicationContext context = new ClassPathXmlApplicationContext("services.xml", "daos.xml");
> 
> // retrieve configured instance
> PetStoreService service = context.getBean("petStore", PetStoreService.class);
> 
> // use configured instance
> List<String> userList = service.getUsernameList();
> ```
>
> 

总结：`ApplicationContext`是一个高级工厂的接口，它能够维护一个有不同beans及它们依赖项的登记表。通过使用方法`T getBean(String name, Class<T> requiredType)`可以获取bean的实例。通过`ApplicationContext`可以读取beans的定义和访问它们。

> The most flexible variant is `GenericApplicationContext` in combination with reader delegates — for example, with `XmlBeanDefinitionReader` for XML files, as the following example shows:
>
> ```java
> GenericApplicationContext context = new GenericApplicationContext();
> new XmlBeanDefinitionReader(context).loadBeanDefinitions("services.xml", "daos.xml");
> context.refresh();
> ```
>
> 

总结：让容器加载XML配置文件，除了`ClassPathXmlApplicationContext`的构造函数外，还可以使用灵活的变体`GenericApplicationContext`和读取器委托结合，例如对于XML文件使用`XmlBeanDefinitionReader`读取器。

> You can mix and match such reader delegates on the same `ApplicationContext`, reading bean definitions from diverse configuration sources.
>
> You can then use `getBean` to retrieve instances of your beans. The `ApplicationContext` interface has a few other methods for retrieving beans, but, ideally, your application code should never use them. Indeed, your application code should have no calls to the `getBean()` method at all and thus have no dependency on Spring APIs at all. For example, Spring’s integration with web frameworks provides dependency injection for various web framework components such as controllers and JSF-managed beans, letting you declare a dependency on a specific bean through metadata (such as an autowiring annotation).

总结：可以在同样的`ApplicationContext`上混合和匹配使用类似读取器委托，从不同的配置源读取bean的定义。虽然`ApplicationContext`接口提供了不只`getBean()`一种方法获取bean的实例，但是在实际的开发中是不会调用这些Spring的API，因为获取bean实例一点都不依赖于这些API。例如，Spring整合Web框架提供对多种Web框架组件（如controller、管理JSF的bean）的依赖注入，让开发者通过元数据（如自动装配的注解）为特定的bean声明依赖。

> A Spring IoC container manages one or more beans. These beans are created with the configuration metadata that you supply to the container (for example, in the form of XML `<bean/>` definitions).
>
> Within the container itself, these bean definitions are represented as `BeanDefinition` objects, which contain (among other information) the following metadata:
>
> + A package-qualified class name: typically, the actual implementation class of the bean being defined.
> + Bean behavioral configuration elements, which state how the bean should behave in the container (scope, lifecycle callbacks, and so forth).
> + References to other beans that are needed for the bean to do its work. These references are also called collaborators or dependencies.
> + Other configuration settings to set in the newly created object — for example, the size limit of the pool or the number of connections to use in a bean that manages a connection pool.

总结：Spring IoC容器管理一个或多个bean。这些bean是使用提供给容器的配置元数据创建的。在容器本身中，这些bean的定义被表示为`BeanDefinition`对象，该对象包含如下的元数据：

+ 包限定类名：通常是被定义的bean的真实实现类
+ bean的行为配置元素，用于说明bean在容器中的行为方式（范围/作用域，生命周期回调等）
+ 引用bean工作需要的其他bean。这种引用也称为协作者或依赖项。
+ 在新创建的对象中设置的其他配置设置，比如在管理连接池的bean使用的连接池大小和连接数量。

> This metadata translates to a set of properties that make up each bean definition. The following table describes these properties:
>
> | Property                 | Explained in…                                                |
> | :----------------------- | :----------------------------------------------------------- |
> | Class                    | [Instantiating Beans](https://docs.spring.io/spring-framework/reference/core/beans/definition.html#beans-factory-class) |
> | Name                     | [Naming Beans](https://docs.spring.io/spring-framework/reference/core/beans/definition.html#beans-beanname) |
> | Scope                    | [Bean Scopes](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html) |
> | Constructor arguments    | [Dependency Injection](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html) |
> | Properties               | [Dependency Injection](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html) |
> | Autowiring mode          | [Autowiring Collaborators](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-autowire.html) |
> | Lazy initialization mode | [Lazy-initialized Beans](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-lazy-init.html) |
> | Initialization method    | [Initialization Callbacks](https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html#beans-factory-lifecycle-initializingbean) |
> | Destruction method       | [Destruction Callbacks](https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html#beans-factory-lifecycle-disposablebean) |

总结：这些元数据会被转换为每个bean定义的一组属性，包括`Class`（类）、`Name`（名称）、`Scope`（范围/作用域）、`Constructor arguments`（构造函数参数）、`Properties`（属性）、`Autowiring mode`（自动装配模式）、`Lazy initialization mode`（延迟初始化模式）、`initialization method`（初始化方法）、`Destruction method`（销毁方法）。

> Bean metadata and manually supplied singleton instances need to be registered as early as possible, in order for the container to properly reason about them during autowiring and other introspection steps. While overriding existing metadata and existing singleton instances is supported to some degree, the registration of new beans at runtime (concurrently with live access to the factory) is not officially supported and may lead to concurrent access exceptions, inconsistent state in the bean container, or both.

总结：需要尽可能早地注册bean的元数据和手动提供的单例实例，以便容器在自动装配和其他内省的步骤中正确推理它们。虽然在一定程度上支持覆盖存在的元数据和单例实例，但是在运行时注册新的bean（同时进行工厂的实时访问）不受官方支持，并且可能导致并行访问异常，bean容器中状态不一致，或两种情况都有。

> Bean overriding occurs when a bean is registered using an identifier that is already allocated. While bean overriding is possible, it makes the configuration harder to read.
>
> Bean overriding will be deprecated in a future release.
>
> To disable bean overriding altogether, you can set the `allowBeanDefinitionOverriding` flag to `false` on the `ApplicationContext` before it is refreshed. In such a setup, an exception is thrown if bean overriding is used.

总结：当使用已分配的标识符注册bean时会发生bean的覆盖。虽然bean的覆盖是可能的，但是它使得配置难以阅读。在未来的发行版本中bean覆盖将被弃用。若要完全禁用bean覆盖，可以在`ApplicationContext`刷新前设置它的`allowBeanDefinitionOverriding`标志为`false`。这样设置后，当发生bean覆盖则会抛出异常。

> Every bean has one or more identifiers. These identifiers must be unique within the container that hosts the bean. A bean usually has only one identifier. However, if it requires more than one, the extra ones can be considered aliases.
>
> In XML-based configuration metadata, you use the `id` attribute, the `name` attribute, or both to specify bean identifiers. The `id` attribute lets you specify exactly one `id`. Conventionally, these names are alphanumeric ('myBean', 'someService', etc.), but they can contain special characters as well. If you want to introduce other aliases for the bean, you can also specify them in the `name` attribute, separated by a comma (`,`), semicolon (`;`), or white space. Although the `id` attribute is defined as an `xsd:string` type, bean `id` uniqueness is enforced by the container, though not by XML parsers.
>
> You are not required to supply a `name` or an `id` for a bean. If you do not supply a `name` or `id` explicitly, the container generates a unique name for that bean. However, if you want to refer to that bean by name, through the use of the `ref` element or a Service Locator style lookup, you must provide a name. Motivations for not supplying a name are related to using [inner beans](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-properties-detailed.html#beans-inner-beans) and [autowiring collaborators](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-autowire.html).

总结：在容器托管的bean中，每一个bean有一个或多个标识符唯一地标识这些bean。在基于XML配置的元数据中，使用`id`或`name`去指定bean的标识。虽然`id`属性被作为`xsd:string`类型定义，但是bean的`id`的唯一性是通过容器强制（执行），而不是XML解析器。如果没有为bean提供`name`或`id`，那么容器会为bean生成一个唯一的`name`。如果要使用`ref`元素来引用bean的name，那么必须提供`name`。

>The convention is to use the standard Java convention for instance field names when naming beans. That is, bean names start with a lowercase letter and are camel-cased from there. Examples of such names include `accountManager`, `accountService`, `userDao`, `loginController`, and so forth.
>
>Naming beans consistently makes your configuration easier to read and understand. Also, if you use Spring AOP, it helps a lot when applying advice to a set of beans related by name.

总结：在为bean命名时最好遵循Java对实例字段名称的命名规范，bean的命名以小写字母开头、采用驼峰命名。保持bean命名规范的一致性可以使得配置容易阅读和理解。同样，在使用Spring AOP时，有助于将`advice`应用于一组命名相关的bean。

> A bean definition is essentially a recipe for creating one or more objects. The container looks at the recipe for a named bean when asked and uses the configuration metadata encapsulated by that bean definition to create (or acquire) an actual object.
>
> If you use XML-based configuration metadata, you specify the type (or class) of object that is to be instantiated in the `class` attribute of the `<bean/>` element. This `class` attribute (which, internally, is a `Class` property on a `BeanDefinition` instance) is usually mandatory. (For exceptions, see [Instantiation by Using an Instance Factory Method](https://docs.spring.io/spring-framework/reference/core/beans/definition.html#beans-factory-class-instance-factory-method) and [Bean Definition Inheritance](https://docs.spring.io/spring-framework/reference/core/beans/child-bean-definitions.html).)

总结：一个bean的定义（`Bean Definition`）本质上是创建一个或多个对象的一个”配方“（方针）。当被”询问“时，容器查找命名的bean的”配方“，并使用配置元数据封装的这个bean的定义来创建（或获取）一个实际的对象。如果使用基于XML配置的配置元数据，必须在`<bean/>`元素的属性`class`中指定对象的类型（或类）才实例化对象。`class`属性（在内部，是`BeanDefinition`实例的`class`属性）通常是必须的，除非使用某实例工厂方法实例化对象，以及在bean定义的继承中。

> When you create a bean by the constructor approach, all normal classes are usable by and compatible with Spring. That is, the class being developed does not need to implement any specific interfaces or to be coded in a specific fashion. Simply specifying the bean class should suffice. However, depending on what type of IoC you use for that specific bean, you may need a default (empty) constructor.
>
> The Spring IoC container can manage virtually any class you want it to manage. It is not limited to managing true JavaBeans. Most Spring users prefer actual JavaBeans with only a default (no-argument) constructor and appropriate setters and getters modeled after the properties in the container. You can also have more exotic non-bean-style classes in your container. If, for example, you need to use a legacy connection pool that absolutely does not adhere to the JavaBean specification, Spring can manage it as well.

总结：通过构造函数的方法创建一个bean，所有普通的类都能被Spring使用和Spring兼容。这意味着类在开发的时候不需要实现任何特定的接口或按特定的方式编码，只需要指明bean的类就够。然而依赖于所使用的特定bean的IoC类型，需要提供一个默认的（空的）构造函数，即无参数、空语句。Spring Ioc容器可以管理你想要它管理的几乎所有的类。它不仅限于管理真实的Java Beans。大多数Spring用户更喜欢只有一个默认（无参）构造函数，以及适当的`setter`和`getter`方法的实际Java Beans。也可以在容器中有一些奇特的非bean类型的类。例如，如果需要使用一个完全不符合JavaBean规范的遗留连接池，Spring也同样可以管理它。

> When defining a bean that you create with a static factory method, use the `class` attribute to specify the class that contains the `static` factory method and an attribute named `factory-method` to specify the name of the factory method itself. You should be able to call this method (with optional arguments, as described later) and return a live object, which subsequently is treated as if it had been created through a constructor. One use for such a bean definition is to call `static` factories in legacy code.

> The following bean definition specifies that the bean will be created by calling a factory method. The definition does not specify the type (class) of the returned object, but rather the class containing the factory method. In this example, the `createInstance()` method must be a `static` method. The following example shows how to specify a factory method:
>
> ```xml
> <bean id="clientService"
> 	class="examples.ClientService"
> 	factory-method="createInstance"/>
> ```
>
> The following example shows a class that would work with the preceding bean definition:
>
> ```java
> public class ClientService {
> 	private static ClientService clientService = new ClientService();
> 	private ClientService() {}
> 
> 	public static ClientService createInstance() {
> 		return clientService;
> 	}
> }
> ```
>
> 

总结：当定义一个使用静态工厂方法创建的bean时，需要使用`class`属性指定含有静态工厂方法的类并且在名为`factory-method`属性中指明工厂方法自身的方法名。要确保能够调用（访问控制符应为`public static`）这个方法（可选参数）并且返回一个活的对象，随后将其视为通过构造函数构造的。

> Similar to instantiation through a [static factory method](https://docs.spring.io/spring-framework/reference/core/beans/definition.html#beans-factory-class-static-factory-method) , instantiation with an instance factory method invokes a non-static method of an existing bean from the container to create a new bean. To use this mechanism, leave the `class` attribute empty and, in the `factory-bean` attribute, specify the name of a bean in the current (or parent or ancestor) container that contains the instance method that is to be invoked to create the object. Set the name of the factory method itself with the `factory-method` attribute. The following example shows how to configure such a bean:
>
> ```xml
> <!-- the factory bean, which contains a method called createClientServiceInstance() -->
> <bean id="serviceLocator" class="examples.DefaultServiceLocator">
> 	<!-- inject any dependencies required by this locator bean -->
> </bean>
> 
> <!-- the bean to be created via the factory bean -->
> <bean id="clientService"
> 	factory-bean="serviceLocator"
> 	factory-method="createClientServiceInstance"/>
> ```
>
> The following example shows the corresponding class:
>
> ```java
> public class DefaultServiceLocator {
> 
> 	private static ClientService clientService = new ClientServiceImpl();
> 
> 	public ClientService createClientServiceInstance() {
> 		return clientService;
> 	}
> }
> ```
>
> 

总结：通过实例工厂方法实例化会调用一个容器中已经存在的bean的非静态工厂方法去创建新的bean。要使用这种机制，`class`属性留空，在`factory-bean`属性中指明在当前（或者父级、祖先级）容器中含有被调用创建对象的实例方法的bean的名字`name`，在`factory-method`属性中设置工厂方法自己的名称。

> The runtime type of a specific bean is non-trivial to determine. A specified class in the bean metadata definition is just an initial class reference, potentially combined with a declared factory method or being a `FactoryBean` class which may lead to a different runtime type of the bean, or not being set at all in case of an instance-level factory method (which is resolved via the specified `factory-bean` name instead). Additionally, AOP proxying may wrap a bean instance with an interface-based proxy with limited exposure of the target bean’s actual type (just its implemented interfaces).
>
> The recommended way to find out about the actual runtime type of a particular bean is a `BeanFactory.getType` call for the specified bean name. This takes all of the above cases into account and returns the type of object that a `BeanFactory.getBean` call is going to return for the same bean name.

总结：要确定一个特定bean的运行时类型不是一个简单的事情。在bean元数据中定义的特定bean仅仅是初始化类的引用，可能与声明式工厂方法结合或作为一个`FactoryBean`类，这会导致bean不同的运行时类型。要查看一个特定bean的实际运行时类型推荐的方式是`BeanFactory.getType`方法调用这个特定的bean名称，它会返回相同bean名称的对象类型。

##### 依赖注入

> Dependency injection (DI) is a process whereby objects define their dependencies (that is, the other objects with which they work) only through constructor arguments, arguments to a factory method, or properties that are set on the object instance after it is constructed or returned from a factory method. The container then injects those dependencies when it creates the bean. This process is fundamentally the inverse (hence the name, Inversion of Control) of the bean itself controlling the instantiation or location of its dependencies on its own by using direct construction of classes or the Service Locator pattern.

总结：依赖注入是一个过程：对象仅通过构造函数参数、工厂方法参数、一个对象实例被构造或从某工厂方法返回后被设置为属性，来定义它们之间的依赖关系。容器在创建bean时注入这些依赖。这个过程根本上是bean自身，通过直接类构造器或服务定位器模式，自行控制它的依赖项实例或位置的反转（因此得名“控制反转”）。

> DI exists in two major variants: [Constructor-based dependency injection](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html#beans-constructor-injection) and [Setter-based dependency injection](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html#beans-setter-injection).

总结：目前推荐的依赖注入方式有：基于构造函数的依赖注入、基于`Setter`的依赖注入。

> Constructor-based DI is accomplished by the container invoking a constructor with a number of arguments, each representing a dependency. Calling a `static` factory method with specific arguments to construct the bean is nearly equivalent, and this discussion treats arguments to a constructor and to a `static` factory method similarly. 

总结：基于构造函数的依赖注入通过IoC容器调用带参数的构造函数来实现，其中每个参数代表一个依赖项。这和通过调用有特定参数的静态工厂方法去构造Bean是几乎等效的，它将参数视作一个构造函数或一个相似的静态工厂方法。

> Constructor argument resolution matching occurs by using the argument’s type. If no potential ambiguity exists in the constructor arguments of a bean definition, the order in which the constructor arguments are defined in a bean definition is the order in which those arguments are supplied to the appropriate constructor when the bean is being instantiated.

总结：构造函数参数解析匹配是使用参数的类型。如果在bean定义的构造函数参数中不存在潜在的歧义，那么该构造函数参数定义的顺序就是bean在被实例化时提供给相应构造函数的顺序。

这说明了在定义构造函数时，构造函数的顺序需要考虑是否导致“歧义”，尤其是当参数间存在继承关系时。

> Setter-based DI is accomplished by the container calling setter methods on your beans after invoking a no-argument constructor or a no-argument `static` factory method to instantiate your bean.

总结：基于`Setter`的依赖注入实现通过容器在调用一个无参构造函数或一个无参静态工厂方法后，再调用`setter`方法去实例化bean。

> The `ApplicationContext` supports constructor-based and setter-based DI for the beans it manages. It also supports setter-based DI after some dependencies have already been injected through the constructor approach. 

总结：`Application`支持它管理的bean使用基于构造函数和基于`setter`的依赖注入。它也支持bean即使已通过构造函数的方式注入了一些依赖后，再使用`setter`注入。

> Since you can mix constructor-based and setter-based DI, it is a good rule of thumb to use constructors for mandatory dependencies and setter methods or configuration methods for optional dependencies. Note that use of the [@Autowired](https://docs.spring.io/spring-framework/reference/core/beans/annotation-config/autowired.html) annotation on a setter method can be used to make the property be a required dependency; however, constructor injection with programmatic validation of arguments is preferable.
>
> The Spring team generally advocates constructor injection, as it lets you implement application components as immutable objects and ensures that required dependencies are not `null`. Furthermore, constructor-injected components are always returned to the client (calling) code in a fully initialized state. As a side note, a large number of constructor arguments is a bad code smell, implying that the class likely has too many responsibilities and should be refactored to better address proper separation of concerns.
>
> Setter injection should primarily only be used for optional dependencies that can be assigned reasonable default values within the class. Otherwise, not-null checks must be performed everywhere the code uses the dependency. One benefit of setter injection is that setter methods make objects of that class amenable to reconfiguration or re-injection later. Management through [JMX MBeans](https://docs.spring.io/spring-framework/reference/integration/jmx.html) is therefore a compelling use case for setter injection.
>
> Use the DI style that makes the most sense for a particular class. Sometimes, when dealing with third-party classes for which you do not have the source, the choice is made for you. For example, if a third-party class does not expose any setter methods, then constructor injection may be the only available form of DI.

总结：可以混合使用基于构造函数和基于`setter`的方法注入依赖，但是推荐的做法是：对于一些强制的、必选的依赖，宜采用构造函数注入；对于一些可选的依赖，宜采用`setter`方法注入。若在`setter`方法上使用注解`@Autowire`，则该方法注入的依赖为必须的。Spring团队推荐使用构造函数注入，因为它使得注入的依赖为不可变对象（final），同时保证不为`null`。但是也要注意将参数数量设置过多的槽糕写法。虽然`setter`方法用于注入可选的依赖，但还是最好保证可以设置默认的值或在调用时进行参数验证。使用`setter`方法的一个作用就是可以在对象注入后重新配置或注入依赖。在使用某些第三方类且未暴露`setter`方法时，基于构造函数的注入则为唯一可用方法。

> The container performs bean dependency resolution as follows:
>
> + The `ApplicationContext` is created and initialized with configuration metadata that describes all the beans. Configuration metadata can be specified by XML, Java code, or annotations.
> + For each bean, its dependencies are expressed in the form of properties, constructor arguments, or arguments to the static-factory method (if you use that instead of a normal constructor). These dependencies are provided to the bean, when the bean is actually created.
> + Each property or constructor argument is an actual definition of the value to set, or a reference to another bean in the container.
> + Each property or constructor argument that is a value is converted from its specified format to the actual type of that property or constructor argument. By default, Spring can convert a value supplied in string format to all built-in types, such as `int`, `long`, `String`, `boolean`, and so forth.
>
> The Spring container validates the configuration of each bean as the container is created. However, the bean properties themselves are not set until the bean is actually created. Beans that are singleton-scoped and set to be pre-instantiated (the default) are created when the container is created. Scopes are defined in [Bean Scopes](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html). Otherwise, the bean is created only when it is requested. Creation of a bean potentially causes a graph of beans to be created, as the bean’s dependencies and its dependencies' dependencies (and so on) are created and assigned. Note that resolution mismatches among those dependencies may show up late — that is, on first creation of the affected bean.

总结：容器的bean依赖解析过程：1.创建以及使用描述所有bean的配置元数据初始化`ApplicationContext`。2.对于每一个bean，它的依赖被表示在属性表、构造函数参数或静态工厂方法参数中。当bean被真正创建时，这些依赖被提供给bean。3.每个属性或构造函数参数是一个待设置的真实的定义值，或对容器中其他bean的引用。4.作为值的每一个属性或构造函数参数从它指定的格式转换为属性或构造函数参数实际的类型。默认，Spring可以将字符串形式的值转换为所有的基本数据类型。

Spring容器在创建容器时会验证每一个bean的配置。然后，在bean被实际创建之前bean自身的属性不会被设置。容器创建时，单例作用域的bean和设置为预实例化（默认）的bean被创建。否则，当bean被请求时才创建bean。创建bean的过程可能创建bean图，因为bean的依赖和它依赖的依赖是被创建和分配的。解析不匹配的依赖可能延迟显示。

>Circular dependencies
>
>If you use predominantly constructor injection, it is possible to create an unresolvable circular dependency scenario.
>
>For example: Class A requires an instance of class B through constructor injection, and class B requires an instance of class A through constructor injection. If you configure beans for classes A and B to be injected into each other, the Spring IoC container detects this circular reference at runtime, and throws a `BeanCurrentlyInCreationException`.
>
>One possible solution is to edit the source code of some classes to be configured by setters rather than constructors. Alternatively, avoid constructor injection and use setter injection only. In other words, although it is not recommended, you can configure circular dependencies with setter injection.
>
>Unlike the typical case (with no circular dependencies), a circular dependency between bean A and bean B forces one of the beans to be injected into the other prior to being fully initialized itself (a classic chicken-and-egg scenario).

总结：如果都使用构造函数注入依赖，则可能导致循环依赖。循环依赖的简单例子：A类需要一个B类实例，B类又需要一个A类实例，且都通过构造函数注入。IoC容器在运行时检测到循环引用，会抛出`BeanCurrentlyInCreationException`异常。一种解决方法就是编辑源代码使用`setter`注入而不是构造函数注入。A类和B类之间的循环依赖会强制某个bean在完全初始化完成之前先注入另一个bean（类似经典的“先有鸡还是先有蛋”）。

> You can generally trust Spring to do the right thing. It detects configuration problems, such as references to non-existent beans and circular dependencies, at container load-time. Spring sets properties and resolves dependencies as late as possible, when the bean is actually created. This means that a Spring container that has loaded correctly can later generate an exception when you request an object if there is a problem creating that object or one of its dependencies — for example, the bean throws an exception as a result of a missing or invalid property. This potentially delayed visibility of some configuration issues is why `ApplicationContext` implementations by default pre-instantiate singleton beans. At the cost of some upfront time and memory to create these beans before they are actually needed, you discover configuration issues when the `ApplicationContext` is created, not later. You can still override this default behavior so that singleton beans initialize lazily, rather than being eagerly pre-instantiated.

总结：Spring在加载时会检查配置问题，比如引用不存在的bean、循环依赖。在bean被真正创建时，Spring会尽可能地延迟设置属性和解决依赖。这意味着如果创建对象或其依赖出现问题时，则正确加载的Spring容器会在需要一个因为缺少或无效的属性异常的bean后抛出异常。这种对某些配置问题的潜在延迟可见性是 `ApplicationContext` 实现默认预先实例化单例 bean 的原因。在实际需要bean 之前创建 bean 需要花费一些前置时间和内存，但可以在创建 `ApplicationContext` 时发现配置问题，而不是以后。

> By default, `ApplicationContext` implementations eagerly create and configure all [singleton](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html#beans-factory-scopes-singleton) beans as part of the initialization process. Generally, this pre-instantiation is desirable, because errors in the configuration or surrounding environment are discovered immediately, as opposed to hours or even days later. When this behavior is not desirable, you can prevent pre-instantiation of a singleton bean by marking the bean definition as being lazy-initialized. A lazy-initialized bean tells the IoC container to create a bean instance when it is first requested, rather than at startup.
>
> This behavior is controlled by the `@Lazy` annotation or in XML the `lazy-init` attribute on the `<bean/>` element, 

> However, when a lazy-initialized bean is a dependency of a singleton bean that is not lazy-initialized, the `ApplicationContext` creates the lazy-initialized bean at startup, because it must satisfy the singleton’s dependencies. The lazy-initialized bean is injected into a singleton bean elsewhere that is not lazy-initialized.

> You can also control lazy-initialization for a set of beans by using the `@Lazy` annotation on your `@Configuration` annotated class or in XML using the `default-lazy-init` attribute on the `<beans/>` element, 

总结：默认情况下，`Application`的实现会尽早地创建和配置所有的单例bean作为容器初始化过程的一部分。通常这样的行为是希望进行的，因为它可以让配置或周围环境中的错误在起始阶段立即被发现，而不是几个小时或几天之后。如果要取消这个行为，那么需要在bean定义上标记延迟预初始化来防止单例bean的预实例化。一个延迟初始化的bean告诉IoC容器当bean首次需要时创建，而不是起始时。

可以在类或配置类上使用`Lazy`注解，或者在XML配置对`<bean/>`元素使用`lazy-init`属性，或`<beans/>`元素使用`default-lazy-init`属性。

然而，当一个延迟初始化的bean作为一个非延迟初始化的单例bean的依赖时，`Application`仍然会在启动阶段创建这个延迟初始化bean，因为它必须满足单例bean的依赖。

> The Spring Framework supports six scopes, four of which are available only if you use a web-aware `ApplicationContext`. You can also create [a custom scope.](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html#beans-factory-scopes-custom)

> | Scope                                                        | Description                                                  |
> | :----------------------------------------------------------- | :----------------------------------------------------------- |
> | [singleton](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html#beans-factory-scopes-singleton) | (Default) Scopes a single bean definition to a single object instance for each Spring IoC container. |
> | [prototype](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html#beans-factory-scopes-prototype) | Scopes a single bean definition to any number of object instances. |
> | [request](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html#beans-factory-scopes-request) | Scopes a single bean definition to the lifecycle of a single HTTP request. That is, each HTTP request has its own instance of a bean created off the back of a single bean definition. Only valid in the context of a web-aware Spring `ApplicationContext`. |
> | [session](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html#beans-factory-scopes-session) | Scopes a single bean definition to the lifecycle of an HTTP `Session`. Only valid in the context of a web-aware Spring `ApplicationContext`. |
> | [application](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html#beans-factory-scopes-application) | Scopes a single bean definition to the lifecycle of a `ServletContext`. Only valid in the context of a web-aware Spring `ApplicationContext`. |
> | [websocket](https://docs.spring.io/spring-framework/reference/web/websocket/stomp/scope.html) | Scopes a single bean definition to the lifecycle of a `WebSocket`. Only valid in the context of a web-aware Spring `ApplicationContext`. |

总结：Spring提供有六种bean的作用域（范围）：`singletom`、`prototype`、`request`、`session`、`application`、`websocket`，后四种仅当`ApplicationContext`是Web感知类型时有效。也可以自定义bean的作用域。

> Only one shared instance of a singleton bean is managed, and all requests for beans with an ID or IDs that match that bean definition result in that one specific bean instance being returned by the Spring container.
>
> To put it another way, when you define a bean definition and it is scoped as a singleton, the Spring IoC container creates exactly one instance of the object defined by that bean definition. This single instance is stored in a cache of such singleton beans, and all subsequent requests and references for that named bean return the cached object. 

> The singleton scope is the default scope in Spring. 

总结：Spring中默认bean的作用域（范围）为`singleton`（单例）。`singleton`的bean意味着IoC容器仅仅管理该单例bean定义的一个实例对象，且存储在此类单例bean的缓存中，对单例bean名称的所有请求和引用容器都返回缓存的对象。

> The non-singleton prototype scope of bean deployment results in the creation of a new bean instance every time a request for that specific bean is made. That is, the bean is injected into another bean or you request it through a `getBean()` method call on the container. As a rule, you should use the prototype scope for all stateful beans and the singleton scope for stateless beans.

> A data access object (DAO) is not typically configured as a prototype, because a typical DAO does not hold any conversational state. It was easier for us to reuse the core of the singleton diagram.

> In contrast to the other scopes, Spring does not manage the complete lifecycle of a prototype bean. The container instantiates, configures, and otherwise assembles a prototype object and hands it to the client, with no further record of that prototype instance. Thus, although initialization lifecycle callback methods are called on all objects regardless of scope, in the case of prototypes, configured destruction lifecycle callbacks are not called. The client code must clean up prototype-scoped objects and release expensive resources that the prototype beans hold. To get the Spring container to release resources held by prototype-scoped beans, try using a custom [bean post-processor](https://docs.spring.io/spring-framework/reference/core/beans/factory-extension.html#beans-factory-extension-bpp) which holds a reference to beans that need to be cleaned up.

总结：`prototype`（原型）作用域的bean当每请求一次这个bean，容器都会创建一个新的实例对象。Spring对于原型的bean不会完全地管理它的生命周期，容器仅实例化、配置bean，其他对bean实例对象的处理由客户端（开发者）完成，容器不会再进一步记录原型bean实例。要使容器释放原型作用域bean所持有的资源，可以使用自定义bean的后处理器（`post-processor`）实现。

建议：对有状态的bean使用原型作用域，对无状态的bean使用单例作用域。数据访问对象（`DAO`）宜采用单例作用域。





## 核心技术

***Spring的核心技术中最重要的是Inversion of Control（IoC，控制反转）和Spring的Aspect-Oriented Programming（面向切面编程）技术。***

### Inversion of Control,IoC（控制反转）

#### IoC容器与Bean介绍

IoC容器可以视作一个管理Java对象（Spring中称为**Bean**）实例化、配置、组装的“容器”，它通过读取Bean的配置元数据来“知晓”Bean的类型、依赖（可以简单理解为在一个Bean中将其他Bean定义为该Bean的成员对象）、作用域等实例化配置，在需要使用Bean时由它进行Bean的创建、管理（包括销毁）等操作，开发者可以专注于应用程序的业务逻辑开发。IoC容器在Bean的创建过程中是一种反向的过程，所以得名“控制反转”。

实现Ioc容器的主要是`org.springframework.beans` 和 `org.springframework.context`两个包，前者提供**BeanFactory**接口用于Bean的管理，后者提供**ApplicationContext**接口在实现**BeanFactory**的功能之外，还提供在企业开发中所需的功能。

IoC容器将开发者编写的类识别或读取为Bean是通过配置元数据（告诉IoC容器Bean的相关信息）实现的，主要有三种方式：

1. 基于XML文件的配置。编写XML文件，根元素是`<beans/>`，在其子元素`<bean/>`中定义Bean的配置信息。然后，在IoC容器实例化前指定XML文件路径。
2. 基于注解的配置。在类上使用基于注解的配置元数据。
3. 基于Java的配置。编写配置类。

在Spring中，构成应用程序并由Spring IoC容器管理的对象称为`bean`。`bean`是由Spring IoC容器实例化、组装和管理的对象。一个`bean`仅是应用程序中许多对象中的一个。Beans和它们之间的依赖关系被反映在容器使用的配置元数据中。



#### Dependencies（依赖项）





