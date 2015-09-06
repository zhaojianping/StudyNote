
#### mybatis 代码生成

``` xml
<plugin>
	<groupId>org.mybatis.generator</groupId>
	<artifactId>mybatis-generator-maven-plugin</artifactId>
	<version>1.3.2</version>
	<configuration>
		<configurationFile>generatorConfig.xml</configurationFile>
		<verbose>true</verbose>
		<overwrite>true</overwrite>
	</configuration>
	<executions>
		<execution>
			<id>Generate MyBatis Artifacts</id>
			<goals>
				<goal>generate</goal>
			</goals>
		</execution>
	</executions>
	<dependencies>
		<dependency>
			<groupId>org.mybatis.generator</groupId>
			<artifactId>mybatis-generator-core</artifactId>
			<version>1.3.2</version>
		</dependency>
	</dependencies>
</plugin>
```


``` xml 
	<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE generatorConfiguration  
  PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"  
  "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">
<generatorConfiguration>
	<classPathEntry location="D:\RuntimeSoftWare\maven\m2\repository\mysql\mysql-connector-java\5.1.20\mysql-connector-java-5.1.20.jar"/>
	<context id="DB2Tables" targetRuntime="MyBatis3">
		<jdbcConnection driverClass="com.mysql.jdbc.Driver"
			connectionURL="jdbc:mysql://10.101.13.208:3306/busEnginEV?useUnicode=true" 
				userId="bus" password="bus">
		</jdbcConnection>
		<javaTypeResolver>
			<property name="forceBigDecimals" value="false" />
		</javaTypeResolver>
		<javaModelGenerator targetPackage="com.autonavi.qa.bus.eval.entity"
			targetProject="D:/codeGen/entity">
			<property name="enableSubPackages" value="true" />
			<property name="trimStrings" value="true" />
		</javaModelGenerator>
		<sqlMapGenerator targetPackage="com.autonavi.qa.bus.eval.mapper"
			targetProject="D:/codeGen/mapper">
			<property name="enableSubPackages" value="true" />
		</sqlMapGenerator>
		<javaClientGenerator type="XMLMAPPER"
			targetPackage="com.autonavi.qa.bus.eval.mapper" targetProject="D:/codeGen/mapper">
			<property name="enableSubPackages" value="true" />
		</javaClientGenerator>
		<table tableName="bus_eval_scheme_similarity" domainObjectName="BusEvalSchemeSimilarity" enableCountByExample="false" enableSelectByExample="false" enableUpdateByExample="false" enableDeleteByExample="false">
			<property name="rootClass" value="com.autonavi.qa.bus.commons.entity.IdEntity&lt;Integer&gt;" />
		</table>
		<table tableName="bus_eval_sort_factor" domainObjectName="BusEvalSortFactor" enableCountByExample="false" enableSelectByExample="false" enableUpdateByExample="false" enableDeleteByExample="false">
			<property name="rootClass" value="com.autonavi.qa.bus.commons.entity.IdEntity&lt;Integer&gt;" />
		</table>
	</context>
</generatorConfiguration> 
```


``` sh
mvn mybatis-generator:generate -X

```

报错

``` sh

[ERROR] Failed to execute goal org.mybatis.generator:mybatis-generator-maven-plugin:1.3.2:generate (default-cli) on project Evaluate_Platform: Execution default-cli of goal org.mybatis.generator:mybatis-generator-maven-plugin:1.3.2:generatefailed: Cannot resolve classpath entry: E:\workspace\alibaba-svn\Evaluate_Platf
orm\src\main\java\** -> [Help 1]

```

使用命令正确

``` sh
java -jar D:\RuntimeSoftWare\maven\m2\repository\org/mybatis/generator/mybatis-generator-core/1.3.2/mybatis-generator-core-1.3.2.jar \
-configfile generatorConfig.xml  
```