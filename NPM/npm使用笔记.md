# NPM 使用

## NPM是什么

**npm** 是 **Node Package Manager** 的缩写，是 **Node.js 生态中的包管理工具**。

**Node.js**：JavaScript 运行时（类似 JVM）。**npm**：随 Node.js 一起安装的包管理器。

从技术本质上看，npm 同时指代三样东西：

1. **一个命令行工具（CLI）**
2. **一个包规范与依赖管理机制**
3. **一个公共的包仓库（registry）**

可以将它与Java包管理工具**Maven**进行类比，**npm**对Node.js的包进行管理；与Maven通过`pom.xml`引入包依赖类似，npm通过项目的`package.json`文件进行包引入。

通常**npm**主要负责：1.下载项目需要的依赖（包/库/组件）；2.管理项目和依赖的版本；3.解决依赖之间的嵌套关系。



## 项目元数据管理`package.json`文件

每个**npm**项目都有一个 **`package.json`**文件，它相当于：项目的“项目说明书 + 依赖清单 + 构建入口定义”。一个`package.json`示例：

```json
{
  "name": "demo-my-vue",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "engines": {
    "node": "^20.19.0 || >=22.12.0"
  },
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "format": "prettier --write --experimental-cli src/"
  },
  "dependencies": {
    "pinia": "^3.0.4",
    "vue": "^3.5.25",
    "vue-router": "^4.6.3"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^6.0.2",
    "prettier": "3.6.2",
    "vite": "^7.2.4",
    "vite-plugin-vue-devtools": "^8.0.5"
  }
}
```

+ 开头的`name`、`version`、`private`、`type`、`engines`等对项目的基本描述管理。
+ `scripts`：可执行命令，通过`npm run <属性名>`执行，比如`npm run dev`就是在执行`vite`命令。
+ `dependencies`：运行时依赖（类似 Maven 的 `<dependency>`）。
+ `devDependencies`：开发时依赖，仅开发 / 构建期需要。

这里说明一下**npm**对版本的管理——版本号规则（语义化版本），npm 使用 **SemVer**：

```
主版本.次版本.补丁
1.2.3
```

常见写法：

- `^1.2.3`：允许升级 minor（次版本） / patch（补丁版本）
- `~1.2.3`：只允许 patch 升级
- `1.2.3`：完全锁死



## npm项目结构

npm的基本项目（目录）结构如下：

```
demo-my-vue/
├─ package.json        ← npm 核心配置
├─ package-lock.json   ← 依赖锁
├─ node_modules/       ← 所有依赖
├─ src/
├─ vite.config.js
```

+ `node_modules`：当使用npm安装依赖时，它会读取 `package.json`文件的内容、解析依赖树、下载对应的依赖包、把依赖安装到 `node_modules/`目录。
+ `package-lock.json`：依赖锁定。它的作用：锁定**精确版本**，保证多人协作、CI 环境依赖一致。



## npm常用命令

基础命令：

```bash
npm init           # 初始化项目
npm install        # 安装所有依赖
npm install vue    # 安装某个依赖
npm run dev        # 执行脚本
npm uninstall xxx  # 删除依赖
```



### npm install （依赖安装）

`npm install`命令用于安装依赖。

如果没有指定安装的依赖名，则读取 `package.json`文件 → 按 `package-lock.json` 精确安装 → 生成 / 更新 `node_modules`中的依赖包。

如果制定了依赖名，如`npm install element-plus --save` ，将安装`element-plus`依赖到 `node_modules`，并写入 `package.json`的`dependencies`中。

通过执行`npm install <依赖>`可以在下载安装依赖的同时将依赖信息写入`package.json`文件中，不用手动编写依赖在执行安装，这和`Maven`有所区别。

如果在安装时需要指定依赖的版本，使用`npm install <package-name>@<x.x.x>`，比如`npm install vue@3.4.0`。

关于`npm install`命令有几个参数需要说明：

| 参数 | 全称         | 作用核心             | 是否写入 package.json | 典型用途         |
| ---- | ------------ | -------------------- | --------------------- | ---------------- |
| `-S` | `--save`     | 保存为**运行时依赖** | 是（dependencies）    | 项目运行必须     |
| `-D` | `--save-dev` | 保存为**开发期依赖** | 是（devDependencies） | 构建、测试、工具 |
| `-g` | `--global`   | **全局安装**         | 否（项目无感知）      | CLI 工具         |

示例：

+ `-S`：`npm install axios -S`，下载 axios、写入 `package.json` 的`dependencies`、安装到项目 `node_modules`。
+ `-D`：`npm install vite -D`，下载 vite、写入 `devDependencies` 、本地开发 / 构建期可用。
+ `-g`：`npm install -g typescript`，安装到全局目录、提供全局命令（如 `tsc`）、**不会写入项目 `package.json`**。

建议使用`-S`的情况：1.代码在**运行时 `import / require`**；2.构建后的产物依赖它；3.服务器启动必须存在。

建议使用`-D`的判断标准：这个包是否会被打包进最终运行产物？比如像测试框架、编译器、构建工具、Lint / Format格式化工具等就使用`-D`。

建议使用`-g`的情况：安装的是工具，而不是项目依赖。

注意：**npm 5以上（包括5）的版本对于`npm install`命令默认行为就是 `-S`。也就是说：`-S` 已经是显式冗余参数，虽然npm仍然支持，但不再必需。**



### npm run （脚本运行）

使用`npm run`可以执行在`package.json`文件中自定义的脚本，比如：

```json
"scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "format": "prettier --write --experimental-cli src/"
  }
```

对应的执行命令为：

```bash
npm run dev
npm run build
npm run preview
npm run format
```

如果在执行命令时需要传递参数，在命令和参数之间使用`--`，比如：

```bash
npm run build -- --mode=prod
```

npm也内置一些快捷命令，可以省略`run`：

```bash
npm start
npm test
npm stop
```



### npm uninstall （依赖移除）

移除依赖使用`npm uninstall`命令，比如：

```bash
npm uninstall axios
```

该命令会删除 `node_modules`中的`axios`依赖，同步更新 项目的`package.json` 和 `package-lock.json`文件。

同样可以使用`-D`、`-g`参数指定依赖的类型，如：`npm uninstall vite -D`。



### npm list （查看依赖树）

```bash
npm list
npm list --depth=0

# 查看指定包的依赖树
npm list <包名>
```

+ `--depth=0`：只看一级依赖。相应的有多级依赖，如——`--depth=2`

若某级依赖中，包名后面显示`deduped`，说明项目中存在“**重复依赖**”（如项目中同时安装A和B两个依赖，而B本身又依赖A），且NPM已经将该依赖包去重。

如要看全局依赖（即安装时使用`-g`参数的依赖），在命令后面加上`-g`参数，如`npm list -g`。



### npm outdated （查看可升级依赖）

```bash
npm outdated
```



### npm update（升级依赖）

```bash
npm update
```

升级规则：按 `package.json` 的版本范围升级，不会突破 `^` （允许升级 次版本 / patch补丁版本）或 `~`（只允许 补丁升级） 限制。

如果要指定升级的依赖，则命令中要给出依赖（包）名，比如`npm update vue`。



### npm cache （缓存管理）

当出现：包下载异常、hash 校验失败等问题时，可以尝试通过清除npm的缓存进行解决。

```bash
npm cache clean --force
```

+ `--force`参数——强制执行。



### npm info / view （查看依赖/包信息）

命令的格式：

```bash
npm view <包名>
npm view <包名> versions
npm info <包名>
```

可查看：版本列表；依赖；入口文件。

**注意：该命令会从包仓库获取包的信息，而不是本地。所以使用该命令可以有助于选取包的版本信息。**



### npm init （初始化项目）

1. 交互式初始化

   ```bash
   npm init
   ```

   npm一步步引导完成项目的初始化，通过键盘输入项目的基本信息，最终在当前目录下生成一个`package.json`的文件。

2. 快速初始化

   ```bash
   npm init -y
   ```

   npm采用默认设置自动生成一个`package.json`文件。

*** Vue / Vite 脚手架本质上也是在生成“ package.json”***。



### npm config （配置管理）

1. 查看npm的配置信息

   ```bash
   npm config list
   ```

2. 查看npm特定配置信息

   ```
   npm config get <配置名>
   ```

   如查看`regisatry`（包仓库/镜像）——`npm config get registry`

3. **设置npm的镜像（包仓库）**——常用

   ```bash
   npm config set registry <镜像地址>
   ```

   如设置阿里npm镜像：`npm config set registry https://registry.npmmirror.com`。



### npm audit （安全检查）

```bash
npm audit
npm audit fix
```

作用：

- 扫描已知漏洞
- 自动修复（可能升级版本）

**企业项目中常见于 CI**。



### 常见命令参数说明

| 参数                 | 含义               |
| -------------------- | ------------------ |
| `-D`                 | `--save-dev`       |
| `-g`                 | 全局安装           |
| `--force`            | 强制执行           |
| `--legacy-peer-deps` | 忽略 peer 依赖冲突 |
| `--production`       | 仅安装生产依赖     |



## 使用建议

1. **不要手动改 node_modules**
2. **提交 `package-lock.json`**
3. CI 使用 `npm ci`
4. 本地尽量避免 `-g`
5. 遇到依赖冲突，先看 `peerDependencies`



