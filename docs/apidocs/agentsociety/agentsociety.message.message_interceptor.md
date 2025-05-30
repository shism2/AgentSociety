# {py:mod}`agentsociety.message.message_interceptor`

```{py:module} agentsociety.message.message_interceptor
```

```{autodoc2-docstring} agentsociety.message.message_interceptor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MessageBlockBase <agentsociety.message.message_interceptor.MessageBlockBase>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockBase
    :summary:
    ```
* - {py:obj}`MessageInterceptor <agentsociety.message.message_interceptor.MessageInterceptor>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor
    :summary:
    ```
* - {py:obj}`MessageBlockListenerBase <agentsociety.message.message_interceptor.MessageBlockListenerBase>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DEFAULT_ERROR_STRING <agentsociety.message.message_interceptor.DEFAULT_ERROR_STRING>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.DEFAULT_ERROR_STRING
    :summary:
    ```
* - {py:obj}`logger <agentsociety.message.message_interceptor.logger>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.logger
    :summary:
    ```
* - {py:obj}`__all__ <agentsociety.message.message_interceptor.__all__>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.__all__
    :summary:
    ```
* - {py:obj}`BlackSetEntry <agentsociety.message.message_interceptor.BlackSetEntry>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.BlackSetEntry
    :summary:
    ```
* - {py:obj}`BlackSet <agentsociety.message.message_interceptor.BlackSet>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.BlackSet
    :summary:
    ```
* - {py:obj}`MessageIdentifierEntry <agentsociety.message.message_interceptor.MessageIdentifierEntry>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageIdentifierEntry
    :summary:
    ```
* - {py:obj}`MessageIdentifier <agentsociety.message.message_interceptor.MessageIdentifier>`
  - ```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageIdentifier
    :summary:
    ```
````

### API

````{py:data} DEFAULT_ERROR_STRING
:canonical: agentsociety.message.message_interceptor.DEFAULT_ERROR_STRING
:value: <Multiline-String>

```{autodoc2-docstring} agentsociety.message.message_interceptor.DEFAULT_ERROR_STRING
```

````

````{py:data} logger
:canonical: agentsociety.message.message_interceptor.logger
:value: >
   'getLogger(...)'

```{autodoc2-docstring} agentsociety.message.message_interceptor.logger
```

````

````{py:data} __all__
:canonical: agentsociety.message.message_interceptor.__all__
:value: >
   ['MessageBlockBase', 'MessageInterceptor', 'MessageBlockListenerBase']

```{autodoc2-docstring} agentsociety.message.message_interceptor.__all__
```

````

````{py:data} BlackSetEntry
:canonical: agentsociety.message.message_interceptor.BlackSetEntry
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} agentsociety.message.message_interceptor.BlackSetEntry
```

````

````{py:data} BlackSet
:canonical: agentsociety.message.message_interceptor.BlackSet
:value: >
   None

```{autodoc2-docstring} agentsociety.message.message_interceptor.BlackSet
```

````

````{py:data} MessageIdentifierEntry
:canonical: agentsociety.message.message_interceptor.MessageIdentifierEntry
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageIdentifierEntry
```

````

````{py:data} MessageIdentifier
:canonical: agentsociety.message.message_interceptor.MessageIdentifier
:value: >
   None

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageIdentifier
```

````

`````{py:class} MessageBlockBase(name: str = '')
:canonical: agentsociety.message.message_interceptor.MessageBlockBase

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockBase
```

```{rubric} Initialization
```

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockBase.__init__
```

````{py:property} name
:canonical: agentsociety.message.message_interceptor.MessageBlockBase.name
:type: str

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockBase.name
```

````

````{py:method} forward(llm: agentsociety.llm.LLM, from_id: int, to_id: int, msg: str, violation_counts: dict[int, int], black_set: agentsociety.message.message_interceptor.BlackSet) -> tuple[bool, str]
:canonical: agentsociety.message.message_interceptor.MessageBlockBase.forward
:abstractmethod:
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockBase.forward
```

````

`````

`````{py:class} MessageInterceptor(blocks: list[agentsociety.message.message_interceptor.MessageBlockBase], llm_config: list[agentsociety.llm.LLMConfig], queue: ray.util.queue.Queue, max_blocked_messages_per_round: typing.Optional[int] = None, max_communicated_agents_per_round: typing.Optional[int] = None, max_communication_length_cn: typing.Optional[int] = None, max_communication_length_en: typing.Optional[int] = None, max_total_cut_edges: typing.Optional[int] = None, max_total_blocked_agents: typing.Optional[int] = None, black_set: agentsociety.message.message_interceptor.BlackSet = set())
:canonical: agentsociety.message.message_interceptor.MessageInterceptor

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor
```

```{rubric} Initialization
```

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.__init__
```

````{py:method} init()
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.init
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.init
```

````

````{py:method} close()
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.close
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.close
```

````

````{py:property} llm
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.llm
:type: agentsociety.llm.LLM

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.llm
```

````

````{py:method} black_set() -> agentsociety.message.message_interceptor.BlackSet
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.black_set
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.black_set
```

````

````{py:method} add_to_black_set(black_set: typing.Union[agentsociety.message.message_interceptor.BlackSet, agentsociety.message.message_interceptor.BlackSetEntry])
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.add_to_black_set
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.add_to_black_set
```

````

````{py:method} remove_from_black_set(to_remove_black_set: typing.Union[agentsociety.message.message_interceptor.BlackSet, agentsociety.message.message_interceptor.BlackSetEntry])
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.remove_from_black_set
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.remove_from_black_set
```

````

````{py:method} set_black_set(black_set: typing.Union[agentsociety.message.message_interceptor.BlackSet, agentsociety.message.message_interceptor.BlackSetEntry])
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.set_black_set
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.set_black_set
```

````

````{py:method} blocks() -> list[agentsociety.message.message_interceptor.MessageBlockBase]
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.blocks
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.blocks
```

````

````{py:method} insert_block(block: agentsociety.message.message_interceptor.MessageBlockBase, index: typing.Optional[int] = None)
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.insert_block
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.insert_block
```

````

````{py:method} pop_block(index: typing.Optional[int] = None) -> agentsociety.message.message_interceptor.MessageBlockBase
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.pop_block
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.pop_block
```

````

````{py:method} set_blocks(blocks: list[agentsociety.message.message_interceptor.MessageBlockBase])
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.set_blocks
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.set_blocks
```

````

````{py:method} violation_counts() -> dict[int, int]
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.violation_counts
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.violation_counts
```

````

````{py:method} check_message(from_id: int, to_id: int, msg: str)
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.check_message
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.check_message
```

````

````{py:method} add_message(from_id: int, to_id: int, msg: str) -> None
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.add_message
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.add_message
```

````

````{py:method} forward()
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.forward
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.forward
```

````

````{py:method} update_blocked_agent_ids(blocked_agent_ids: typing.Optional[list[int]] = None)
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.update_blocked_agent_ids
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.update_blocked_agent_ids
```

````

````{py:method} update_blocked_social_edges(blocked_social_edges: typing.Optional[list[tuple[int, int]]] = None)
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.update_blocked_social_edges
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.update_blocked_social_edges
```

````

````{py:method} modify_validation_dict(validation_dict: agentsociety.message.message_interceptor.MessageIdentifier) -> agentsociety.message.message_interceptor.MessageIdentifier
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.modify_validation_dict
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.modify_validation_dict
```

````

````{py:method} get_blocked_agent_ids() -> list[int]
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.get_blocked_agent_ids
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.get_blocked_agent_ids
```

````

````{py:method} clear_validation_dict() -> None
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.clear_validation_dict
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.clear_validation_dict
```

````

````{py:method} get_validation_dict() -> agentsociety.message.message_interceptor.MessageIdentifier
:canonical: agentsociety.message.message_interceptor.MessageInterceptor.get_validation_dict
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageInterceptor.get_validation_dict
```

````

`````

`````{py:class} MessageBlockListenerBase(queue: ray.util.queue.Queue)
:canonical: agentsociety.message.message_interceptor.MessageBlockListenerBase

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase
```

```{rubric} Initialization
```

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase.__init__
```

````{py:property} queue
:canonical: agentsociety.message.message_interceptor.MessageBlockListenerBase.queue
:type: ray.util.queue.Queue

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase.queue
```

````

````{py:method} forward(msg: typing.Any)
:canonical: agentsociety.message.message_interceptor.MessageBlockListenerBase.forward
:abstractmethod:
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase.forward
```

````

````{py:method} _listen()
:canonical: agentsociety.message.message_interceptor.MessageBlockListenerBase._listen
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase._listen
```

````

````{py:method} init()
:canonical: agentsociety.message.message_interceptor.MessageBlockListenerBase.init

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase.init
```

````

````{py:method} close()
:canonical: agentsociety.message.message_interceptor.MessageBlockListenerBase.close
:async:

```{autodoc2-docstring} agentsociety.message.message_interceptor.MessageBlockListenerBase.close
```

````

`````
