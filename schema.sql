drop table if exists events;
drop table if exists posts;


create table events(id, updated TEXT, calendar_title TEXT, event_title TEXT, start_time INTEGER,
                    end_time INTEGER, location TEXT, status TEXT, description TEXT,
                    is_all_day INTEGER, thumbnail TEXT, full_image TEXT, endowment_title TEXT);


create table posts(id, updated TEXT, title TEXT, published INTEGER, content TEXT, categories TEXT,
                   summary TEXT);
