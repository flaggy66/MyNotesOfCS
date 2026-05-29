# Maven 学习笔记

## Maven介绍

Maven是一个***Java项目管理和构建工具***，它可以**定义项目结构、项目依赖**，并使用统一的方式进行自动化构建。

Maven提供了一套标准化的项目结构——使得使用不同开发工具创建的项目结构是一致的（如不使用maven，则在eclipse和IDEA上创建的项目结构是不同的）。同时也提供了一套标准化的构建流程（编译、测试、打包、发布……）。

它还提供了一套依赖管理机制——如果使用传统管理，会导致项目的依赖包过大，占用磁盘空间，计算机间传输速度慢；使用maven管理依赖包，通过中央仓库的方式统一管理所有依赖包（jar包），降低依赖占用的空间，同时在一定程度上解决了依赖之间的冲突问题（如jar包版本问题）。

## Maven安装

Maven是一个java工具，所以必须先安装JDK，即Java环境。

到[官网]([Maven – Welcome to Apache Maven](https://maven.apache.org/))下载Maven安装包。

修改Maven的一些配置信息（修改安装包中conf目录下的setting.xml）。一般修改Maven在本机的仓库地址（默认为user目录下的.m2目录下），以及Maven下载的镜像地址（Maven的官方地址在国内下载较慢）。本地仓库地址根据个人需要修改为磁盘上的地址，镜像地址推荐阿里云和华为云。

配置系统环境变量。

在cmd中输入`mvn -v`验证Maven安装是否成功。

## Maven配置

Maven配置文件`settings.xml`的[官方文档说明](https://maven.apache.org/settings.html)。

`settings.xml`文件一般位于两个位置：

+ 用户目录下——`/user/.m2/settings.xml`
+ Maven安装目录下——`${maven.home}/conf/settings.xml`

Maven安装目录下的成为全局配置，用户目录下的称为用户配置。如果两个都存在，内容会覆盖，并且用户配置的优先级高。

`settings.xml`文件中的顶级元素（elements）：

```xml
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 https://maven.apache.org/xsd/settings-1.0.0.xsd">
  <localRepository/>
  <interactiveMode/>
  <offline/>
  <pluginGroups/>
  <servers/>
  <mirrors/>
  <proxies/>
  <profiles/>
  <activeProfiles/>
</settings>
```

可以在`settings.xml`中使用以下表达式插值：

+ `${user.home}`以及其他的系统属性
+ `${env.HOME}`等环境变量

*注意：在`settings.xml`文件中定义的属性不能用于插值。*

**localRepository**

该元素的值规定了构建项目时的本地仓库地址，默认值为`${user.home}/.m2/repository`。可以自己指定本地仓库的地址，如`<localRepository>D:\Maven\repository</localRepository>`。

**interactiveMode**

该元素的值只能为`true`和`false`（默认`false`）。`true`：会在输入时提示。`false`：在输入时不提示。

**offline**

该元素的值只能为`true`和`false`（默认`false`），用于设定Maven是否在无网络的情况下完成构建系统的操作（true：可在无网络环境下操作）。

**Mirrors**

这是一个十分重要的配置，用于设置中央仓库的镜像地址，提高下载效率。

每一个镜像仓库定义在`mirror`元素中，所有的镜像仓库包含于父元素`mirrors`。

`mirror`有子元素`id`、`name`、`url`、`mirrorOf`。

+ `id`、`name`：是镜像间唯一的标识和用户友好的命名。`id`必须可以和其他镜像的`id`区分，并在连接到镜像时从`servers`部分中选取对应的凭据（有关`servers`参见[官方文档](https://maven.apache.org/settings.html#servers)）。（注：这里的`id`是自己本地的一种镜像区分）
+ `url`：镜像仓库的基本URL地址。在构建系统时将会使用这个URL去连接远程仓库，而不是原始的仓库URL。
+ `mirrorOf`：这是镜像仓库某种意义上的真实“id”。例如，要指向Maven的`central`仓库（官方地址：https://repo.maven.apache.org/maven2/，也可以自定义），请将此元素的值设为`central`（默认情况下包含主Maven Central存储库的ID是“central”）。更高级的映射，如`repo1`、`repo2`或`*`、`!inhouse`也是可能的。该值不能与`id`元素值匹配。

更多的关于Mirrors的介绍，可见[Maven – Guide to Mirror Settings (apache.org)](https://maven.apache.org/guides/mini/guide-mirror-settings.html)。

使用不同的镜像实例，可以按需要配置一下内容（注：请不要直接复制，根据镜像仓库的实际内容编写）：

```xml
  <mirrors>
    <mirror>
      <id>other-mirror</id>
      <name>Other Mirror Repository</name>
      <url>https://other-mirror.repo.other-company.com/maven2</url>
      <mirrorOf>central</mirrorOf>
    </mirror>
  </mirrors>
```

***注意：给定的一个仓库（repository）最多只能有一个镜像（mirror）。换句话说，我们不能将单个仓库映射到一组定义了相同`mirrorOf`值的镜像中。Maven不会聚合镜像，而只是选择第一个匹配的项。如果要提供多个仓库的组合视图，请改用仓库管理器（[repository manager](https://maven.apache.org/repository-management.html)）。***

官方Maven仓库地址：(https://repo.maven.apache.org/maven2)。

`mirrorOf`的一些特定语法：

+ `*`：匹配所有的仓库id。
+ `external:*`：匹配除使用localhost或基于文件的仓库（存储库）之外的所有仓库。当需要排除为集成测试定义的重定向存储库时，将使用此选项。
+ `external:http:*`：从Maven 3.8.0开始，匹配所有使用HTTP的存储库，但使用localhost的存储库除外。
+ `repo,repo1`：匹配repo或repo1
+ `*,!repo1`：匹配所有，但除了repo1

注意：不要在逗号分隔的列表中的标识符或通配符周围包含多余的空格。例如，`!repo1, *`不会匹配任何镜像，而`!repo1,*`匹配所有，除了repo1。

当使用高级语法兵配置多个镜像时，声明的顺序很重要。当Maven查找某个仓库的镜像时，它首先检查与`mirrorOf`值（仓库标识符）完全匹配的镜像。如果未找到直接匹配项，Maven将根据上述规则（如果有）选择第一个匹配的镜像声明。因此在`settings.xml`中声明的镜像顺序会影响镜像匹配的顺序。

## 在IDEA中设置Maven

在IDEA中打开设置（需要打开任意一个项目或文件，settings -> Build，Excecution，…… -> Build Tools -> Maven，按照自己的Maven配置进行设置。

## 创建Maven项目

一、通过IDEA编辑器提供的工具。

二、使用Maven命令：mvn archetype:generate。此命令可创建一个脚手架（即提供了Maven项目最基本的项目结构）

## Maven的项目结构

Maven通过“约定”的方式，指定各级目录所放置的内容，实现项目构建过程的自动化完成。

1. pom.xml

	此文件标志着这是一个Maven项目，也相当于Maven项目的配置文件。

2. main

	放置项目的主体文件，如Java类、应用配置资源等。

3. test

	放置测试文件。

4. java

	放置Java文件，如类、包等。
	java路径下的包名通过创建项目时的groupid生成

5. resources

	放置应用配置文件、资源文件等。

## pom.xml文件

1. 坐标信息
    通过三个标签——\<groupId>、\<artifactId>、\<version>确定jar包或本工程项目所属的仓库位置。
    引用依赖时，也是通过坐标信息去仓库中下载依赖。
    groupId：组织名(类似域名反过来），如：com\.baidu
    artifactId：项目名，如：HelloWorld
    version：版本号
    ***如果当前构建的文件仅仅是某个项目的子模块，则groupId向下包括该项目名，如：com.baidu.HelloWorld，artifactId是此模块名，如xxxLogin。***

2. 通过坐标信息引入依赖
  ```
  <dependendies>
  	<dependency>
  		<groupId>xxxx</groupId>
  		<artifactId>xxxx</artifactId>
  		<version>xxxx</version>
  	</dependency>
  </dependendies>
  ```
  Maven会先去本地仓库寻找，若没有，再去中央仓库寻找下载。

3. 属性、变量信息
    通过标签\<properties>\</properties>中的子属性（子标签）设置。
    通常设置版本信息，如在\<properties>\</properties>中定义了\<javax.servlet.version>3.1.2\</javax.servlet.version>，则可以在引入依赖时，通过${javax.servlet.version}去替代\<version>\</version>标签中具体的值。

4. 设置打包方式
    如打包为war包``<packaging>war</packaging>``，默认为jar包。
    
5. 依赖范围
	在\<dependendcy>\</dependendcy>内通过子标签（属性）\<scope>\</scope>设置依赖所处的范围（编译、测试、运行/打包等），属性值：compile、test、runtime、system、provided等。
	test：仅在测试有用
	provided：编译、测试有用
	compile：编译、测试、打包有用，是默认的
	runtime：测试、打包有用，可作用于反射，如数据库驱动
	system：编译、测试有用，但不会仓库中的jar包，而是引用本地物理路径中的jar包，通过设置\<systemPath>\</systemPath>
	通常使用默认的（即不用自己设置）就能够满足需要，在引用中央仓库的依赖时，部分依赖在中央仓库中带有\<scope>\</scope>标签，还有在IDEA编辑器中会有自动提示。

## 依赖传递

需要引入的依赖本身还对其他依赖有引入。通常在引入前者时，后者就会自动引入。但有时为了不引入后者，可以设置\<scope>\<scope>或\<optional>\</optional>限制。

## 依赖排除

在\<dependency>\</dependency>中设置属性\<exclusions>\</exclusions>中的\<exclusion>\</exclusion>，在其中通过坐标信息指定排除的依赖，即可排除依赖所引入的依赖。

## 依赖覆盖

手动添加依赖，系统会自动覆盖依赖传递中的间接依赖。

## 通过依赖图查看依赖链

使用IDEA提供的工具查看依赖链。

## Maven聚合

将多个Maven项目整合为一个Maven项目。
1. 删除src
2. 在pom.xml中修改\<packaging>\</packaging>为pom
3. 把各个项目进行管理

## Maven继承

在子项目的Maven的pom.xml文件中添加\<parent>\</parent>标签和相应的坐标信息。