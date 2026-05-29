# Spring的AOP技术

***内容来源：[Spring 官网参考](https://docs.spring.io/spring-framework/reference)，人工智能问答（ChatGPT、Google Gemini等）***

>One of the key components of Spring is the AOP framework. While the Spring IoC container does not depend on AOP (meaning you do not need to use AOP if you don’t want to), AOP complements Spring IoC to provide a very capable middleware solution.

> Spring provides simple and powerful ways of writing custom aspects by using either a [schema-based approach](https://docs.spring.io/spring-framework/reference/6.2/core/aop/schema.html) or the [@AspectJ annotation style](https://docs.spring.io/spring-framework/reference/6.2/core/aop/ataspectj.html). Both of these styles offer fully typed advice and use of the AspectJ pointcut language while still using Spring AOP for weaving.



## Spring AOP中的一些特殊概念

> Introduction: Declaring additional methods or fields on behalf of a type. Spring AOP lets you introduce new interfaces (and a corresponding implementation) to any advised object. For example, you could use an introduction to make a bean implement an `IsModified` interface, to simplify caching. (An introduction is known as an inter-type declaration in the AspectJ community.)

`Introduction`（引入）：代表一个类型声明附加的方法或字段。Spring AOP 允许你为任何被通知对象引入新的接口（以及相应的实现）。（在 AspectJ 社区中，引入被称为跨类型声明。）



## Spring AOP的通知（Advice）类型

>- Before advice: Advice that runs before a join point but that does not have the ability to prevent execution flow proceeding to the join point (unless it throws an exception).
>- After returning advice: Advice to be run after a join point completes normally (for example, if a method returns without throwing an exception).
>- After throwing advice: Advice to be run if a method exits by throwing an exception.
>- After (finally) advice: Advice to be run regardless of the means by which a join point exits (normal or exceptional return).
>- Around advice: Advice that surrounds a join point such as a method invocation. This is the most powerful kind of advice. Around advice can perform custom behavior before and after the method invocation. It is also responsible for choosing whether to proceed to the join point or to shortcut the advised method execution by returning its own return value or throwing an exception.

五种通知类型：

1. `Before advice`：连接点之前的通知（比如方法调用前）。但它不能阻止连接点（比如目标方法调用）的继续执行。
2. `After returning advice`：连接点正常完成（运行结束）后的通知。
3. `After throwing advice`：连接点抛出异常退出后的通知。
4. `After (finally) advice`：不管连接点正常或异常退出都要执行的通知。
5. `Around advice`：连接点周围的通知，可以作用于连接点前、连接点后，甚至是连接点执行中。

> Around advice is the most general kind of advice. Since Spring AOP, like AspectJ, provides a full range of advice types, we recommend that you use the least powerful advice type that can implement the required behavior. For example, if you need only to update a cache with the return value of a method, you are better off implementing an after returning advice than an around advice, although an around advice can accomplish the same thing. Using the most specific advice type provides a simpler programming model with less potential for errors. For example, you do not need to invoke the `proceed()` method on the `JoinPoint` used for around advice, and, hence, you cannot fail to invoke it.

**建议**：使用合适作用范围的通知类型。



## Spring AOP的能力和目标

> Spring Framework  6.2.15
>
> Spring AOP currently supports only method execution join points (advising the execution of methods on Spring beans). Field interception is not implemented, although support for field interception could be added without breaking the core Spring AOP APIs. If you need to advise field access and update join points, consider a language such as AspectJ.

在Spring Framework的目前版本（6.2.15）中，Spring AOP只支持Spring Bean的“方法执行”的连接点。对于完整连接点的AOP功能，可以考虑使用AspectJ。

> Spring AOP’s approach to AOP differs from that of most other AOP frameworks. The aim is not to provide the most complete AOP implementation (although Spring AOP is quite capable). Rather, the aim is to provide a close integration between AOP implementation and Spring IoC, to help solve common problems in enterprise applications.

Spring AOP 的目的并非提供最完整的 AOP 实现，而是提供 AOP 实现与 Spring IoC 的紧密集成，以帮助企业应用程序解决常见问题。

> You have the choice of AspectJ, Spring AOP, or both. You also have the choice of either the @AspectJ annotation-style approach or the Spring XML configuration-style approach. 

基于`@AspectJ`注解风格和Spring XML配置风格的AOP风格是可选的。



## Spring AOP的代理类型

> Spring AOP defaults to using standard JDK dynamic proxies for AOP proxies. This enables any interface (or set of interfaces) to be proxied.

Spring AOP默认使用标准**JDK动态代理**作为AOP的代理，它能对任何接口（或一组接口）进行代理。

> Spring AOP can also use CGLIB proxies. This is necessary to proxy classes rather than interfaces. By default, CGLIB is used if a business object does not implement an interface. As it is good practice to program to interfaces rather than classes, business classes normally implement one or more business interfaces. It is possible to [force the use of CGLIB](https://docs.spring.io/spring-framework/reference/6.2/core/aop/proxying.html), in those (hopefully rare) cases where you need to advise a method that is not declared on an interface or where you need to pass a proxied object to a method as a concrete type.

Spring AOP 还可以使用**CGLIB**代理。这是为了代理类而不是接口。默认情况下，如果业务对象没有实现接口，则会使用 CGLIB。



## 对`@AspectJ`的支持

> @AspectJ refers to a style of declaring aspects as regular Java classes annotated with annotations. The @AspectJ style was introduced by the [AspectJ project](https://www.eclipse.org/aspectj) as part of the AspectJ 5 release. Spring interprets the same annotations as AspectJ 5, using a library supplied by AspectJ for pointcut parsing and matching. The AOP runtime is still pure Spring AOP, though, and there is no dependency on the AspectJ compiler or weaver.

`@AspectJ`指的是将一种将切面声明为带有注解的常规 Java 类的风格。

`@AspectJ`风格由 AspectJ 项目作为 AspectJ 5 版本的一部分引入。**Spring 解释与 AspectJ 5 相同的注解，并使用 AspectJ 提供的库进行切入点解析和匹配**。

不过，**Spring AOP 运行时仍然是纯粹的 Spring AOP，并且不依赖于 AspectJ 编译器或织入器**。



### 启用`@AspectJ`支持

> To use @AspectJ aspects in a Spring configuration, you need to enable Spring support for configuring Spring AOP based on @AspectJ aspects and auto-proxying beans based on whether or not they are advised by those aspects. 
>
> The @AspectJ support can be enabled with programmatic or XML configuration. In either case, you also need to ensure that AspectJ’s `org.aspectj:aspectjweaver` library is on the classpath of your application (version 1.9 or later).

+ 通过代码编程配置——在配置类上**使用`@EnableAspectJAutoProxy`注解**

  ```java
  @Configuration
  @EnableAspectJAutoProxy
  public class ApplicationConfiguration {
  }
  ```

+ XML配置

  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
  	   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  	   xmlns:aop="http://www.springframework.org/schema/aop"
  	   xsi:schemaLocation="http://www.springframework.org/schema/beans
  			https://www.springframework.org/schema/beans/spring-beans.xsd
  			http://www.springframework.org/schema/aop
  			https://www.springframework.org/schema/aop/spring-aop.xsd">
  
  	<aop:aspectj-autoproxy />
  </beans>
  ```

  



### 声明（创建）切面（Aspect）

> With @AspectJ support enabled, any bean defined in your application context with a class that is an @AspectJ aspect (has the `@Aspect` annotation) is automatically detected by Spring and used to configure Spring AOP. 

开启对`@AspectJ`支持后，任何用`@Aspect`注解修饰的常规Spring Bean类会被Spring检测识别为`@AspectJ`切面类，并用于配置 Spring AOP。

1. 切面需要是一个被Spring管理的Bean。
2. 在类上使用`@Aspect`注解修饰。

>Autodetecting aspects through component scanning
>
>You can register aspect classes as regular beans in your Spring XML configuration, via `@Bean` methods in `@Configuration` classes, or have Spring autodetect them through classpath scanning — the same as any other Spring-managed bean. However, note that the `@Aspect` annotation is not sufficient for autodetection in the classpath. For that purpose, you need to add a separate `@Component` annotation (or, alternatively, a custom stereotype annotation that qualifies, as per the rules of Spring’s component scanner).

**补充**：可以通过组件扫描自动检测切面（Aspect），给切面加一个符合 Spring 组件扫描器规则的限定自定义原型注解，如`@Component`。

> Aspects (classes annotated with `@Aspect`) can have methods and fields, the same as any other class. They can also contain pointcut, advice, and introduction (inter-type) declarations.

切面（使用 `@Aspect` 注解的类）可以像其他类一样拥有方法和字段。它们还可以包含切入点（Pointcut）、通知（Advice）和引入（introduction）声明。

>Advising aspects with other aspects?
>
>In Spring AOP, aspects themselves cannot be the targets of advice from other aspects. The `@Aspect` annotation on a class marks it as an aspect and, hence, excludes it from auto-proxying.

**在 Spring AOP 中，切面本身不能成为其他切面的通知目标**。



### 声明（创建）切点（Pointcut）

> Pointcuts determine join points of interest and thus enable us to control when advice runs. Spring AOP only supports method execution join points for Spring beans, so you can think of a pointcut as matching the execution of methods on Spring beans. A pointcut declaration has two parts: a signature comprising a name and any parameters and a pointcut expression that determines exactly which method executions we are interested in. In the @AspectJ annotation-style of AOP, a pointcut signature is provided by a regular method definition, and the pointcut expression is indicated by using the `@Pointcut` annotation (the method serving as the pointcut signature must have a `void` return type).

切点（Pointcut）决定着通知（Advice）在哪个连接点（Spring AOP 仅支持 Spring Bean的方法执行作为连接点）上执行。

一个切点的声明由两部分组成：

+ 一个名称和任意参数构成的`签名（signature）`
+ `切点表达式（pointcut expression）`：真正决定（匹配）哪些方法作为切点。

在`@Aspectj`注解风格的 AOP 中，切入点签名由一个常规方法定义提供，而切入点表达式通过使用 `@Pointcut` 注解来指示（作为切入点签名的该方法必须具有 `void` 返回类型）。如：

```java
@Pointcut("execution(* transfer(..))") // the pointcut expression
private void anyOldTransfer() {} // the pointcut signature
```

上面的示例代码：定义了一个名叫`anyOldTransfer`的切点，该切点将匹配所有方法名为`transfer`的方法作为切点。

> The pointcut expression that forms the value of the `@Pointcut` annotation is a regular AspectJ pointcut expression. For a full discussion of AspectJ’s pointcut language, see the [AspectJ Programming Guide](https://www.eclipse.org/aspectj/doc/released/progguide/index.html) (and, for extensions, the [AspectJ 5 Developer’s Notebook](https://www.eclipse.org/aspectj/doc/released/adk15notebook/index.html)) or one of the books on AspectJ (such as *Eclipse AspectJ*, by Colyer et al., or *AspectJ in Action*, by Ramnivas Laddad).

`@Pointcut` 注解的值所形成的切点表达式是一个标准的 `AspectJ pointcut` 表达式。



#### 支持的切点指定符（Pointcut Designators）

>Spring AOP supports the following AspectJ pointcut designators (PCD) for use in pointcut expressions:
>
>- `execution`: For matching method execution join points. This is the primary pointcut designator to use when working with Spring AOP.
>- `within`: Limits matching to join points within certain types (the execution of a method declared within a matching type when using Spring AOP).
>- `this`: Limits matching to join points (the execution of methods when using Spring AOP) where the bean reference (Spring AOP proxy) is an instance of the given type.
>- `target`: Limits matching to join points (the execution of methods when using Spring AOP) where the target object (application object being proxied) is an instance of the given type.
>- `args`: Limits matching to join points (the execution of methods when using Spring AOP) where the arguments are instances of the given types.
>- `@target`: Limits matching to join points (the execution of methods when using Spring AOP) where the class of the executing object has an annotation of the given type.
>- `@args`: Limits matching to join points (the execution of methods when using Spring AOP) where the runtime type of the actual arguments passed have annotations of the given types.
>- `@within`: Limits matching to join points within types that have the given annotation (the execution of methods declared in types with the given annotation when using Spring AOP).
>- `@annotation`: Limits matching to join points where the subject of the join point (the method being run in Spring AOP) has the given annotation.
>
>Because Spring AOP limits matching to only method execution join points, the preceding discussion of the pointcut designators gives a narrower definition than you can find in the AspectJ programming guide. In addition, AspectJ itself has type-based semantics and, at an execution join point, both `this` and `target` refer to the same object: the object executing the method. Spring AOP is a proxy-based system and differentiates between the proxy object itself (which is bound to `this`) and the target object behind the proxy (which is bound to `target`).

由于 Spring AOP 仅将匹配限制在方法执行连接点，因此前面关于切入点指定符的讨论给出了比 AspectJ 编程指南中更狭窄的定义。

Spring AOP 是一个基于代理的系统，它区分代理对象本身（绑定到 `this` ）和代理后面的目标对象（绑定到 `target` ）。

> Due to the proxy-based nature of Spring’s AOP framework, calls within the target object are, by definition, not intercepted. For JDK proxies, only public interface method calls on the proxy can be intercepted. With CGLIB, public and protected method calls on the proxy are intercepted (and even package-visible methods, if necessary). However, common interactions through proxies should always be designed through public signatures.

对于 JDK 代理，只有代理上的`public`接口方法调用可以被拦截。使用 CGLIB 时，代理上的`public`和`protected`方法调用会被拦截（如果需要，甚至可以拦截包可见方法）。

>The full AspectJ pointcut language supports additional pointcut designators that are not supported in Spring: `call`, `get`, `set`, `preinitialization`, `staticinitialization`, `initialization`, `handler`, `adviceexecution`, `withincode`, `cflow`, `cflowbelow`, `if`, `@this`, and `@withincode`. Use of these pointcut designators in pointcut expressions interpreted by Spring AOP results in an `IllegalArgumentException` being thrown.
>
>The set of pointcut designators supported by Spring AOP may be extended in future releases to support more of the AspectJ pointcut designators.



#### 组合的切点表达式

> You can combine pointcut expressions by using `&&,` `||` and `!`. You can also refer to pointcut expressions by name. 

你可以使用 `&&,` `||` 和 `!` 来组合切入点表达式。你也可以通过名称引用切入点表达式。

示例代码：

```java
package com.xyz;

public class Pointcuts {

	@Pointcut("execution(public * *(..))")
	public void publicMethod() {}

	@Pointcut("within(com.xyz.trading..*)")
	public void inTrading() {}

	@Pointcut("publicMethod() && inTrading()")
	public void tradingOperation() {}
}
```

>`publicMethod` matches if a method execution join point represents the execution of any public method.
>
>`inTrading` matches if a method execution is in the trading module.
>
>`tradingOperation` matches if a method execution represents any public method in the trading module.

>It is a best practice to build more complex pointcut expressions out of smaller *named pointcuts*, as shown above. When referring to pointcuts by name, normal Java visibility rules apply (you can see `private` pointcuts in the same type, `protected` pointcuts in the hierarchy, `public` pointcuts anywhere, and so on). Visibility does not affect pointcut matching.

构建更复杂的切入点表达式通常是通过将较小的命名切入点组合而成，如上所示。在通过名称引用切入点时，将应用普通的 Java 可见性规则（你可以看到同一类型的 `private` 切入点、层次结构中的 `protected` 切入点、任何地方的 `public` 切入点等）。可见性不会影响切入点匹配。



#### 切点表达式示范

>Spring AOP users are likely to use the `execution` pointcut designator the most often. The format of an execution expression follows:
>
>```
>execution(modifiers-pattern?
>			ret-type-pattern
>			declaring-type-pattern?name-pattern(param-pattern)
>			throws-pattern?)
>```
>
>All parts except the returning type pattern (`ret-type-pattern` in the preceding snippet), the name pattern, and the parameters pattern are optional. The returning type pattern determines what the return type of the method must be in order for a join point to be matched. `*` is most frequently used as the returning type pattern. It matches any return type. A fully-qualified type name matches only when the method returns the given type. The name pattern matches the method name. You can use the `*` wildcard as all or part of a name pattern. If you specify a declaring type pattern, include a trailing `.` to join it to the name pattern component. The parameters pattern is slightly more complex: `()` matches a method that takes no parameters, whereas `(..)` matches any number (zero or more) of parameters. The `(*)` pattern matches a method that takes one parameter of any type. `(*,String)` matches a method that takes two parameters. The first can be of any type, while the second must be a `String`. 

在Spring AOP的多数使用者中，常用`execution`切点指定符去定义切点表达式。用`execution`的切点表达式有以下部分组成：`modifiers-pattern`、`ret-type-pattern`、`declaring-type-pattern`、`name-pattern`、`param-pattern`、`throws-pattern`。因为Spring AOP只支持Spring Bean类的方法执行拦截，所以切点表达式通常是一个方法的声明，上述选项分别对应`方法的访问修饰符`、`方法返回值类型`、`方法声明类型（即方法所在类的完整包名）`、`方法名`、`方法参数`、`方法抛的异常`。

`execution`的切点表达式中`modifiers-pattern`、`declaring-type-pattern`、`throws-pattern`这三个内容是可选的。

对于`ret-type-pattern`：要么明确给出返回值的类型，要么使用`*`匹配任何返回值类型。

对于`name-pattern`：可以使用`*`匹配方法名的部分或全部字符。如果使用了`declaring-type-pattern`，需要在`declaring-type-pattern`和`name-pattern`之间使用`.`连接，就像`com.abc.service.userservice.login()`那样。

对于`param-pattern`有以下情况：

+ `()`：匹配不接受任何参数的方法，即无参方法。
+ `(..)`：匹配任意数量（零个或更多）的参数的方法。
+ `(*)`：匹配接受一个任何类型的参数的方法，即方法的参数只有一个，且参数类型任意。
+ `(*,type)`：匹配接受两个参数的方法，且第二个参数的类型指定为`type`，例如`(*,String)`，第一个可以是任何类型，而第二个必须是 `String`。

举例：

>- The execution of any public method:
>
>  ```
>  execution(public * *(..))
>  ```
>
>- The execution of any method with a name that begins with `set`:
>
>  ```
>  execution(* set*(..))
>  ```
>
>- The execution of any method defined by the `AccountService` interface:
>
>  ```
>  execution(* com.xyz.service.AccountService.*(..))
>  ```
>
>- The execution of any method defined in the `service` package:
>
>  ```
>  execution(* com.xyz.service.*.*(..))
>  ```
>
>- The execution of any method defined in the service package or one of its sub-packages:
>
>  ```
>  execution(* com.xyz.service..*.*(..))
>  ```



#### 切点编写建议

> For optimal performance of matching, you should think about what you are trying to achieve and narrow the search space for matches as much as possible in the definition. The existing designators naturally fall into one of three groups: kinded, scoping, and contextual:
>
> - Kinded designators select a particular kind of join point: `execution`, `get`, `set`, `call`, and `handler`.
> - Scoping designators select a group of join points of interest (probably of many kinds): `within` and `withincode`
> - Contextual designators match (and optionally bind) based on context: `this`, `target`, and `@annotation`
>
> A well written pointcut should include at least the first two types (kinded and scoping). You can include the contextual designators to match based on join point context or bind that context for use in the advice. Supplying only a kinded designator or only a contextual designator works but could affect weaving performance (time and memory used), due to extra processing and analysis. Scoping designators are very fast to match, and using them means AspectJ can very quickly dismiss groups of join points that should not be further processed. A good pointcut should always include one if possible.

为了实现最佳匹配效果，你应该思考你想要达成的目标，并在定义中尽可能缩小匹配的搜索范围。

一个编写良好的切点至少应包含两种类型的指定符（Designator）：类型化（kinded）和作用域（scoping）。你可以包含上下文的指定符（contextual），根据连接点上下文进行匹配或绑定该上下文以在通知中使用。仅提供类型化指定符或仅提供上下文指定符可以工作，但由于额外的处理和分析，可能会影响织入性能（时间和内存使用）。作用域指定符（kinded）匹配非常快，使用它们意味着 AspectJ 可以非常快速地排除那些不应进一步处理的连接点组。一个良好的切点如果可能的话，应始终包含一个作用域指定符。



### 声明（创建）通知（Advice）

>Advice is associated with a pointcut expression and runs before, after, or around method executions matched by the pointcut. The pointcut expression may be either an *inline pointcut* or a reference to a *named pointcut*.

> You can have multiple advice declarations (and other members as well), all inside the same aspect. We show only a single advice declaration in these examples to focus the effect of each one.

通知（Advice）和切点以及连接点联系在一起，切点可以是内联切点（切点表达式），或者已声明的切点名。

在一个切面（Aspect）中可以有不只一个通知（Advice），也可以有其他的成员（如切点、属性、一般方法等）。



#### Before Advice

>You can declare before advice in an aspect by using the `@Before` annotation.
>
>The following example uses an inline pointcut expression.
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.Before;
>
>@Aspect
>public class BeforeExample {
>
>	@Before("execution(* com.xyz.dao.*.*(..))")
>	public void doAccessCheck() {
>		// ...
>	}
>}
>```
>
>If we use a named pointcut, we can rewrite the preceding example as follows:
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.Before;
>
>@Aspect
>public class BeforeExample {
>
>	@Before("com.xyz.CommonPointcuts.dataAccessOperation()")
>	public void doAccessCheck() {
>		// ...
>	}
>}
>```

在一个`@Aspect`修饰的切面类中编写通知（Advice）方法——用AOP功能做的具体事情，再在通知方法上使用`@Before`注解修饰，其中`@Before`注解的属性为切点表达式或某个已声明切点的名称。

上面示例代码中`com.xyz.CommonPointcuts.dataAccessOperation()`是定义了一个`CommonPointcuts`类用来收集切点规则（表达式），`dataAccessOperation()`是声明的一个切点，如：

```java
package com.xyz;

import org.aspectj.lang.annotation.Pointcut;

public class CommonPointcuts {

	/**
	 * A join point is in the web layer if the method is defined
	 * in a type in the com.xyz.web package or any sub-package
	 * under that.
	 */
	@Pointcut("within(com.xyz.web..*)")
	public void inWebLayer() {}

	/**
	 * A join point is in the service layer if the method is defined
	 * in a type in the com.xyz.service package or any sub-package
	 * under that.
	 */
	@Pointcut("within(com.xyz.service..*)")
	public void inServiceLayer() {}

	/**
	 * A join point is in the data access layer if the method is defined
	 * in a type in the com.xyz.dao package or any sub-package
	 * under that.
	 */
	@Pointcut("within(com.xyz.dao..*)")
	public void inDataAccessLayer() {}

	/**
	 * A business service is the execution of any method defined on a service
	 * interface. This definition assumes that interfaces are placed in the
	 * "service" package, and that implementation types are in sub-packages.
	 *
	 * If you group service interfaces by functional area (for example,
	 * in packages com.xyz.abc.service and com.xyz.def.service) then
	 * the pointcut expression "execution(* com.xyz..service.*.*(..))"
	 * could be used instead.
	 *
	 * Alternatively, you can write the expression using the 'bean'
	 * PCD, like so "bean(*Service)". (This assumes that you have
	 * named your Spring service beans in a consistent fashion.)
	 */
	@Pointcut("execution(* com.xyz..service.*.*(..))")
	public void businessService() {}

	/**
	 * A data access operation is the execution of any method defined on a
	 * DAO interface. This definition assumes that interfaces are placed in the
	 * "dao" package, and that implementation types are in sub-packages.
	 */
	@Pointcut("execution(* com.xyz.dao.*.*(..))")
	public void dataAccessOperation() {}

}
```



#### After Returning Advice

>After returning advice runs when a matched method execution returns normally. You can declare it by using the `@AfterReturning` annotation.
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.AfterReturning;
>
>@Aspect
>public class AfterReturningExample {
>
>	@AfterReturning("execution(* com.xyz.dao.*.*(..))")
>	public void doAccessCheck() {
>		// ...
>	}
>}
>```
>
>Sometimes, you need access in the advice body to the actual value that was returned. You can use the form of `@AfterReturning` that binds the return value to get that access, as the following example shows:
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.AfterReturning;
>
>@Aspect
>public class AfterReturningExample {
>
>	@AfterReturning(
>		pointcut="execution(* com.xyz.dao.*.*(..))",
>		returning="retVal")
>	public void doAccessCheck(Object retVal) {
>		// ...
>	}
>}
>```
>
>The name used in the `returning` attribute must correspond to the name of a parameter in the advice method. When a method execution returns, the return value is passed to the advice method as the corresponding argument value. A `returning` clause also restricts matching to only those method executions that return a value of the specified type (in this case, `Object`, which matches any return value).
>
>Please note that it is not possible to return a totally different reference when using after returning advice.

在一个`@Aspect`修饰的切面类中编写通知（Advice）方法，再在通知方法上使用`@AfterReturning`注解修饰，其中`@AfterReturning`注解的属性为切点表达式或某个已声明切点的名称。

若要在通知（Advice）方法中访问切点目标方法正常返回的返回值，需要在`@AfterReturning`的`returning`属性中绑定通知方法的形参名，才能在通知方法中使用返回值，且`returning`属性值必须与通知方法的形参名一致。

 `returning` 属性还限制匹配仅限于返回指定类型（形参类型）值（在示例代码中为 `Object` ，它匹配任何返回值）的方法执行。



#### After Throwing Advice

>After throwing advice runs when a matched method execution exits by throwing an exception. You can declare it by using the `@AfterThrowing` annotation, as the following example shows:
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.AfterThrowing;
>
>@Aspect
>public class AfterThrowingExample {
>
>	@AfterThrowing("execution(* com.xyz.dao.*.*(..))")
>	public void doRecoveryActions() {
>		// ...
>	}
>}
>```
>
>Often, you want the advice to run only when exceptions of a given type are thrown, and you also often need access to the thrown exception in the advice body. You can use the `throwing` attribute to both restrict matching (if desired — use `Throwable` as the exception type otherwise) and bind the thrown exception to an advice parameter. The following example shows how to do so:
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.AfterThrowing;
>
>@Aspect
>public class AfterThrowingExample {
>
>	@AfterThrowing(
>		pointcut="execution(* com.xyz.dao.*.*(..))",
>		throwing="ex")
>	public void doRecoveryActions(DataAccessException ex) {
>		// ...
>	}
>}
>```
>
>The name used in the `throwing` attribute must correspond to the name of a parameter in the advice method. When a method execution exits by throwing an exception, the exception is passed to the advice method as the corresponding argument value. A `throwing` clause also restricts matching to only those method executions that throw an exception of the specified type (`DataAccessException`, in this case).
>
>Note that `@AfterThrowing` does not indicate a general exception handling callback. Specifically, an `@AfterThrowing` advice method is only supposed to receive exceptions from the join point (user-declared target method) itself but not from an accompanying `@After`/`@AfterReturning` method.

在一个`@Aspect`修饰的切面类中编写通知（Advice）方法，再在通知方法上使用`@AfterThrowing`注解修饰，其中`@AfterThrowing`注解的属性为切点表达式或某个已声明切点的名称。

如果要对切点抛出异常时做这些判断或处理：1. 获取抛出的异常；2. 仅当抛出的异常为特定类型时才执行通知。这时需要在`AfterThrowing`的`throwing`属性中绑定通知方法的形参名，且只有在切点抛出的异常为通知方法形参类型时才执行通知方法。`throwing`属性值必须与通知方法的形参名一致。



#### After (Finally) Advice

>After (finally) advice runs when a matched method execution exits. It is declared by using the `@After` annotation. After advice must be prepared to handle both normal and exception return conditions. It is typically used for releasing resources and similar purposes. The following example shows how to use after finally advice:
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.After;
>
>@Aspect
>public class AfterFinallyExample {
>
>	@After("execution(* com.xyz.dao.*.*(..))")
>	public void doReleaseLock() {
>		// ...
>	}
>}
>```

后置通知（`After Advice`）必须准备好处理正常和异常返回条件。它通常用于释放资源等目的。

在一个`@Aspect`修饰的切面类中编写通知（Advice）方法，再在通知方法上使用`@After`注解修饰，其中`@After`注解的属性为切点表达式或某个已声明切点的名称。



####  Around Advice

>Around advice runs "around" a matched method’s execution. It has the opportunity to do work both before and after the method runs and to determine when, how, and even if the method actually gets to run at all. Around advice is often used if you need to share state before and after a method execution in a thread-safe manner – for example, starting and stopping a timer.
>
>Around advice is declared by annotating a method with the `@Around` annotation. The method should declare `Object` as its return type, and the first parameter of the method must be of type `ProceedingJoinPoint`. Within the body of the advice method, you must invoke `proceed()` on the `ProceedingJoinPoint` in order for the underlying method to run. Invoking `proceed()` without arguments will result in the caller’s original arguments being supplied to the underlying method when it is invoked. For advanced use cases, there is an overloaded variant of the `proceed()` method which accepts an array of arguments (`Object[]`). The values in the array will be used as the arguments to the underlying method when it is invoked.
>
>```java
>import org.aspectj.lang.annotation.Aspect;
>import org.aspectj.lang.annotation.Around;
>import org.aspectj.lang.ProceedingJoinPoint;
>
>@Aspect
>public class AroundExample {
>
>	@Around("execution(* com.xyz..service.*.*(..))")
>	public Object doBasicProfiling(ProceedingJoinPoint pjp) throws Throwable {
>		// start stopwatch
>		Object retVal = pjp.proceed();
>		// stop stopwatch
>		return retVal;
>	}
>}
>```

在一个`@Aspect`修饰的切面类中编写通知（Advice）方法，再在通知方法上使用`@Around`注解修饰，其中`@Around`注解的属性为切点表达式或某个已声明切点的名称。

**`Around Advice`有几个要注意的点**：

+ `Around Advice`类型的通知方法最好**使用`Object`作为方法返回值类型**。
+ `Around Advice`类型的通知方法必须**使用`ProceedingJoinPoint`类型的参数作为方法的第一个形参**。
+ `Around Advice`类型的通知若要**执行切点目标方法，通过`ProceedingJoinPoint.proceed()`调用底层方法（即切点目标方法）**。

> The value returned by the around advice is the return value seen by the caller of the method. For example, a simple caching aspect could return a value from a cache if it has one or invoke `proceed()` (and return that value) if it does not. Note that `proceed` may be invoked once, many times, or not at all within the body of the around advice. All of these are legal.
>
> If you declare the return type of your around advice method as `void`, `null` will always be returned to the caller, effectively ignoring the result of any invocation of `proceed()`. It is therefore recommended that an around advice method declare a return type of `Object`. The advice method should typically return the value returned from an invocation of `proceed()`, even if the underlying method has a `void` return type. However, the advice may optionally return a cached value, a wrapped value, or some other value depending on the use case.

`Around Advice`类型的**通知方法返回值就是调用切点目标方法的调用者看到的返回值**。

若是将`Around Advice`类型的**通知方法的返回值定义为`void`类型，则将始终返回`null`值给切点目标方法调用者**，从而实际上忽略了 `proceed()` 的任何调用结果。根据使用情况，advice 可以选择返回缓存的值、包装的值或其他值。

在`Around Advice`类型的通知方法中`proceed()`可能调用一次、多次或不调用，所有这些都是合法的。



### Advice参数

>Any advice method may declare, as its first parameter, a parameter of type `org.aspectj.lang.JoinPoint`. Note that around advice is required to declare a first parameter of type `ProceedingJoinPoint`, which is a subclass of `JoinPoint`.
>
>The `JoinPoint` interface provides a number of useful methods:
>
>- `getArgs()`: Returns the method arguments.
>- `getThis()`: Returns the proxy object.
>- `getTarget()`: Returns the target object.
>- `getSignature()`: Returns a description of the method that is being advised.
>- `toString()`: Prints a useful description of the method being advised.
>
>See the [javadoc](https://www.eclipse.org/aspectj/doc/released/runtime-api/org/aspectj/lang/JoinPoint.html) for more detail.

任何通知方法都可以将其第一个参数声明为类型是 `org.aspectj.lang.JoinPoint` 的参数。`Around`通知方法必须声明一个类型为 `ProceedingJoinPoint` 的第一个参数，它是 `JoinPoint` 的子类。

`JointPoint`接口提供一些有用的方法获取切点目标方法的信息：

+ `getArgs()`：返回方法的参数
+ `getThis()`：返回代理对象
+ `getTarget()`：返回目标对象
+ `getSignature()`：返回切点目标方法的签名
+ `toString()`：打印切点目标方法的描述信息



**关于Advice通知的参数官方文档有详细介绍**

