<div align="center">
    <h2>Data Storage System challenge</h2>
    <p align="center">
        <p>Because using an existent database is too mainstream :sunglasses:</p>
    </p>
</div>


## Welcome

It is with great pride that we launch our first coding challenge.

In this challenge, there will be a coding problem that you’ll have to solve within 48 hours. Your submission will later be rated and [scored](#score-system).

## Contents

* [Challenge Description](#challenge-description)
* [Requirements](#requirements)
    * [Storage Engine](#storage-engine)
    * [Query Interpreter](#query-interpreter)
    * [Example usage](#example-usage)
* [How to submit](#how-to-submit)
* [Score system](#score-system)
* [Price](#price)
* [Winner](#winner)

## Challenge Description

In this challenge, we will be building a data storage system with its own query language. Something similar to a database engine, but from scratch ;)

We will call it `Data Storage System`, and it's a simple, yet very handy, system/module that can be used by application developers to store their data.

The challenge consists of two parts:
- Storage Engine: How the data will be stored,
- Query Interpreter: How to interpret the queries and evaluate them.


## Requirements

The solution can be written in any technology or language, as long as it respects the requirements.


### Storage Engine

The storage engine should store data in a persistance storage (e.g: We don't lose the data if the PC reboots). 

Also, make sure to design and implement an efficient storage logic, because its efficiency will affect your overall submission [score](#score).

### Query Interpreter

The second subsystem, is the query interpreter, which is the program that will keep reading queries from the standard input, and execute them.

Your interpreter should be able to understand the query language described in the following sections, and it should be interactive, see [Example usage](#example-usage)


#### Description language

To describe a schema, the directive `DECLARE` should be used, where it's syntax is the following:

> `DECLARE` ENTITY_NAME `AS` FIELD1, [[FIELD2], FIELD3]

For example to declare an `entity` named: **user** that contains two fields, `firstname` and `lastname`, the query should be:

> `DECLARE` users `AS` firstname, lastname

- The first field of any entity is its primary key, making it unique
- Every entity should contain at least one field (the primary key).
- To make things easy, all fields are of type `string`

**The interpreter should print `OK` if the query is executed successfully, otherwise it should print `ERROR`**

#### Query language

Using our query language, we should be able to perform three actions: `add`, `delete`, `find`, and `update`.

##### Add

The syntax of the `ADD` directive is the following:

> `ADD` (FIELD1, [[FIELD2], FIELD3]) `TO` ENTITY_NAME

For example to add an entry of type `user`, the query should look like:

> `ADD` ("Ali", "Baba") `TO` users

**The interpreter should print `OK` if the query is executed successfully, otherwise it should print `ERROR`**

##### Delete

The syntax of the `Delete` directive is the following:

> `DELETE` PRIMARY_KEY_VALUE `FROM` ENTITY_NAME

For example, to delete the user with the primary key *Ali*, the query should look like:

> `DELETE` "Ali" `FROM` users

**The interpreter should print `OK` if the query is executed successfully, otherwise it should print `ERROR`**

##### Find

The syntax of the `Find` directive is the following:

> `FIND` [PRIMARY_KEY_VALUE | ALL] `IN` ENTITY_NAME

For example, to find the user with the primary key *Ali*, the query should look like:

> `FIND` "Ali" `IN` users

And to find all the users the query should be:

> `FIND ALL IN` users

**The interpreter should print the results if there is any, otherwise it should print nothing**

See [Example usage](#example-usage) to better understand the syntax

##### Update

The syntax of the `Update` directive is the following:

> `UPDATE` PRIMARY_KEY_VALUE `IN` ENTITY_NAME `SET` FIELDNAME=NEW_VALUE

For example, to update the `lastname` of an element of type `users` (declared above), the syntax should be the following:

> `UPDATE` "Ali" `IN` users `SET` lastname="Dada"

**The interpreter should print `OK` if the query is executed successfully, otherwise it should print `ERROR`**

#### Types

For now, only strings are supported. Both simple `('TEST')` and double quotes `("TEST")` are supported.


### Example usage

```shell
> DECLARE users AS firstname, lastname
* OK
> ADD ("Ali", "Baba") TO users
* OK
> ADD ("Ali", "Baba", "Extra field") TO users
* ERROR
> FIND "Ali" IN users
* 'Ali', 'Baba'
> UPDATE "Ali" IN users SET lastname="Dada"
* OK
> FIND "Ali" IN users
* 'Ali', 'Dada'
> UPDATE "Ali" IN users SET wrong_field="iT"
* ERROR
> WRONG COMMAND
* ERROR
> ADD ("Ni'kola", "Tesla") TO users
* OK
> FIND ALL IN users
* 'Ali', 'Baba'
* 'Ni\'kola', 'Tesla'
> DELETE "Ali" FROM users
* OK
> DELETE "Ali" FROM users
* ERROR
> FIND ALL IN users
* 'Ni\'kola', 'Tesla'
> DELETE "Ni'kola" FROM users
* OK
> FIND ALL IN users
> 

```


## How to submit

To submit your solution, fill this [form](https://goo.gl/forms/2qWbZAQeNmfDsamZ2) and attach it as a `zip` file.

## Prizes

There will be three prizes:
- First place: [Oculus Rift VR](https://www.oculus.com/)
- Second place: [Amazon Echo](https://www.amazon.com/Amazon-Echo-And-Alexa-Devices/b?ie=UTF8&node=9818047011)
- Third place: [Chrome cast](https://store.google.com/product/chromecast_2015)

**Only submissions with a score of 40 and higher will be eligible for prizes.**

## Score system

Each submission will be scored according to the following criteria:

- A working solution: 20 points
- Performance: 10 points
- Code Quality: 10 points


### Extra points

If you submit your solution within the first 24 hours, you get an extra 5 points. 

You will get extra 5 points if you make a library for your solution, so it can be used through a programming language API.

You will also be granted extra 5 points if you manage to make a very simple [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) for your solution, to abstract the query language and use a Object Oriented approach.


### Performance
The interpreter will be benchmarked using `test samples` to measure its performance.

The performance of your solution will highly depend on how well your storage engine is designed.

### Code Quality: 

Having a neat and structured code is a must. The code quality metric will be checked manually by our lead engineers. Your score on this metric depends on how structured your code is, are you following good conventions that your language advices to follow, ...etc.

> PS: You don't have to put comments every where


## Winner

The winner will be announced at [Think-iT Facebook page](https://www.facebook.com/thinkit/), and the winning submission will be published in this repo.


------------------

Designed by [Think.iT](http://www.think-it.io/), with ♥.