1. Самый частый пример использования промежуточных переменных: обычные циклы без использования генераторов или
map/reduce/filter функций, причем там же в основном и происходят ошибки. Также часто происходит хранение
промежуточных переменных как поля класса, чтобы сигнатура публичных интерфейсов была более ясная и чистая, 
а все вычисления проводились внутри, в таком случае помогает организация таких переменных в структуры данных
, например, в датаклассы и последующая передача на вход этим методам.
2. Данная система должна в целом обладать такой структурой типов данных, которые содержат в себе помимо самих
значений еще и метаинформацию как логи/ошибки/какие-либо состояния. Тогда весь код проекта будет изначально
работать с подобными типами данных, то не придется хранить промежуточные состояния отдельно, они будут в потоке 
чистых функций и сразу же использоваться вычисляться. Приложение при старте сразу же передает каждому модулю
его настройки, константы в входные данные конкретных функций. ОЧевидно, что это должно быть чистое функциональное ядро,
возможно похоже на модель акторов, где на информация возникает только по запросу, а не хранится 24/7.