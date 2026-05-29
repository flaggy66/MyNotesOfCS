# JWT介绍

> 内容信息来自：
>
> 1. 网站：https://www.jwt.io/
> 2. 人工智能：ChartGPT、Google Gemini

JSON Web Token（JWT）。



## JWT是什么

> JSON Web Token (JWT) is an open standard ([RFC 7519](https://tools.ietf.org/html/rfc7519)) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the **HMAC** algorithm) or a public/private key pair using **RSA** or **ECDSA**.

JSON Web Token（JWT）是一个以紧凑且自包含的**`JSON`对象**为基础在各方之间**安全传输信息的开放标准**。



## JWT的结构（组成）

>In its compact form, JSON Web Tokens consist of three parts separated by dots (`.`), which are:
>
>- Header
>- Payload
>- Signature
>
>Therefore, a JWT typically looks like the following:
>
>```
>xxxxx.yyyyy.zzzzz
>```

JWT由三个被点号`.`分隔的部分组成：头部`Header`、负载`Payload`、签名`Signature`。



### 头部`Header`

>The header *typically* consists of two parts: the type of the token, which is JWT, and the signing algorithm being used, such as HMAC SHA256 or RSA.
>
>For example:
>
>```json
>{
>  "alg": "HS256",
>  "typ": "JWT"
>}
>```
>
>Then, this JSON is **Base64Url** encoded to form the first part of the JWT.

头部是一个被`Base64Url`编码的`JSON`对象，该`JSON`对象通常包含两个内容：`token`的类型——即`JWT`，签名使用的算法。



### 负载`Payload`

>The second part of the token is the payload, which contains the claims. Claims are statements about an entity (typically, the user) and additional data. There are three types of claims: *registered*, *public*, and *private* claims.
>
>+ [**Registered claims**](https://tools.ietf.org/html/rfc7519#section-4.1): These are a set of predefined claims which are not mandatory but recommended, to provide a set of useful, interoperable claims. Some of them are: **iss** (issuer), **exp** (expiration time), **sub** (subject), **aud** (audience), and [others](https://tools.ietf.org/html/rfc7519#section-4.1).
>+ [**Public claims**](https://tools.ietf.org/html/rfc7519#section-4.2): These can be defined at will by those using JWTs. But to avoid collisions, they should be defined in the [IANA JSON Web Token Registry](https://www.iana.org/assignments/jwt/jwt.xhtml) or be defined as a URI that contains a collision-resistant namespace.
>+ [**Private claims**](https://tools.ietf.org/html/rfc7519#section-4.3): These are the custom claims created to share information between parties that agree on using them and are neither *registered* or *public* claims.
>
>```json
>{
>  "sub": "1234567890",
>  "name": "John Doe",
>  "admin": true
>}
>```
>
>The payload is then **Base64Url** encoded to form the second part of the JSON Web Token.

负载也是一个被`Base64Url`编码的`JSON`对象，该对象一般含有一些声明（对JWT的说明，或者是传输的信息）。

声明有三种类型：注册声明（Registered claim）、公共声明（Public claim）、私有声明（Private claim），这些声明是非强制的，且可以自定义。一般需要考虑的有：JWT的过期时间、JWT要携带的信息等。

>Notice that the claim (Registered claim) names are only three characters long, as JWT is meant to be compact.

为了使JWT更紧凑，建议声明的名称不要过长，如注册声明通常只有3个字符。



### 签名（Signature）

>To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.
>
>For example, if you want to use the HMAC SHA256 algorithm, the signature will be created in the following way:
>
>```
>HMACSHA256(
>  base64UrlEncode(header) + "." +
>  base64UrlEncode(payload),
>  secret)
>```
>
>The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is.

签名需要利用已经编码的头部`Header`和负载`Payload`，使用一个密钥及加密算法去生成（“签名”），同样地JWT的签名部分也需要使用`Base64Url`编码。

签名的作用有2个：

1. 检测头部和负载的内容是否被篡改。
2. 校验该JWT的来源是否可信任。



### 组合

> The output is three Base64-URL strings separated by dots that can be easily passed in HTML and HTTP environments, while being more compact when compared to XML-based standards such as SAML.

最终的JWT是三个由点`.`分隔的 `Base64-URL` 字符串，可以轻松地在 HTML 和 HTTP 环境中传递，并且与基于 XML 的标准（如 SAML）相比更为紧凑。



## JWT的编码（Encoding）与解码（Decoding）

### 编码（Encoding）

> Encoding a JWT involves transforming the header and payload into a compact, URL-safe format. The header, which states the signing algorithm and token type, and the payload, which includes claims like subject, expiration, and issue time, are both converted to JSON then Base64URL encoded. These encoded parts are then concatenated with a dot, after which a signature is generated using the algorithm specified in the header with a secret or private key. This signature is also Base64URL encoded, resulting in the final JWT string that represents the token in a format suitable for transmission or storage.

JWT的编码：将头部（声明有签名算法和令牌类型）和负载（包含其他声明和信息）分别转换为 `JSON` 然后进行 `Base64URL` 编码，再将这些编码后的部分通过点`.`连接起来，之后使用头部中指定的算法和密钥或私钥生成签名，这个签名也进行 `Base64URL` 编码，也用点`.`与之前的编码连接起来，最终形成 JWT 字符串。



### 解码（Decoding）

>Decoding a JWT reverses this process by converting the Base64URL encoded header and payload back into JSON, allowing anyone to read these parts without needing a key. However, "decoding" in this context often extends to include verification of the token's signature. This verification step involves re-signing the decoded header and payload with the same algorithm and key used initially, then comparing this new signature with the one included in the JWT. If they match, it confirms the token's integrity and authenticity, ensuring it hasn't been tampered with since issuance.

解码JWT的过程就是逆转编码的过程：（狭义的解码）将`Base64URL` 编码的头部和负载转换回 JSON 格式，至此解码完成。

实际应用中，“解码”还需要对JWT的签名进行校验：使用最初使用的相同算法和密钥对解码后的头部和负载重新签名，然后将这个新签名与 JWT 中包含的签名进行比较。如果它们匹配，则确认令牌的完整性和真实性，确保自签发以来未被篡改。



## JWT的作用（用途）

>**Authorization**: This is the most common scenario for using JWT. Once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token. Single Sign On is a feature that widely uses JWT nowadays because of its small overhead and its ability to be easily used across different domains.
>
>**Information Exchange**: JSON Web Tokens are a good way of securely transmitting information between parties. Because JWTs can be signed—for example, using public/private key pairs—you can be sure the senders are who they say they are. Additionally, as the signature is calculated using the header and the payload, you can also verify that the content hasn't been tampered with.

JWT的主要用途（都要是因为JWT的签名可检验的特性）：

+ 授权/鉴权：用户登录系统后生成一个JWT给用户，因为JWT的签名部分使用了密钥加密，可以检验该JWT是否为系统生成，同时JWT可以携带非敏感的用户信息，所以可以用于授权或鉴权。
+ 信息交换：在非对称加密（接收双方各有公/私密钥对）的场景下，使用JWT传输、交换信息时可以检验信息发送方是否可信任。又因为JWT的签名部分是根据头部和负载使用加密算法生成，若将信息放入负载中传输可以检验信息是否被篡改。



## JWT的验证（validation）与检验（verification）

> JSON Web Token (JWT) validation and verification are crucial for security, but they address slightly different aspects of JWT security: validation ensures the token is well-formed and contains enforceable claims; verification ensures the token is genuine and unmodified.

+ 验证（validation）确保 JWT 格式正确且包含可执行的声明；
+ 校验（varification）确保 JWT 真实且未被篡改。

在日常使用中，两者被合并为人们俗称的“JWT 验证”的过程，该过程涵盖了验证和确认，以进行全面的安全保护检查。尽管如此，它们的区别仍然存在。



## JWT的使用建议

### JWT的内容大小

> Note that if you send JWT tokens through HTTP headers, you should try to prevent them from getting too big. Some servers don't accept more than 8 KB in headers. If you are trying to embed too much information in a JWT token, like by including all the user's permissions, you may need an alternative solution, like [Auth0 Fine-Grained Authorization](https://fga.dev/).

当要通过HTTP头部发送JWT时，不建议在JWT中存放过多的内容，比如有些服务器在头信息中不接受超过 8 KB 的内容。



### Authorization头部规范

>Whenever the user wants to access a protected route or resource, the user agent should send the JWT, typically in the **Authorization** header using the **Bearer** schema. The content of the header should look like the following:
>
>```
>Authorization: Bearer <token>
>```

用户代理应该在请求头部的 `Authorization` 标头中使用 Bearer 模式发送 JWT，也即 `Authorization` 标头的内容类似：`Bearer {{token}}`，`Bearer`和 JWT 之间有空格。





