import pusher

pusher_client = pusher.Pusher(
  app_id='1286235',
  key='7799888a6bb007b7e9cd',
  secret='0444db8d50a705398faf',
  cluster='eu',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})