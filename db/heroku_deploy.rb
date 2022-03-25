namespace :deploy do
  desc 'Deploy the application'
  task :production do
    app    = "heroku"
    remote = "git@heroku.com:#{app}.git"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Changing to maintenance mode to on..."
    system "heroku maintenance:on --app #{app}"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Git checking out master..."
    system "git checkout master"
    system "git merge --no-ff develop"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Pushing application to origin master..."
    system "git push origin master"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Pushing application to heroku master..."
    system "git push #{remote} master"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Migrating database..."
    system "heroku run rake db:migrate --app #{app}"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Precompiling assets..."
    system "heroku run rake assets:precompile --app #{app}"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Switching back to origin develop..."
    system "git checkout develop"
    puts ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Switching back to application..."
    system "heroku maintenance:off --app #{app}"
  end
end
