drop table if exists cars;

create table cars (
  _id text primary key,
  make text not null,
  year text not null,
  color text not null,
  price text not null,
  hasSunroof boolean not null,
  isFourWheelDrive boolean not null,
  hasLowMiles boolean not null,
  hasPowerWindows boolean not null,
  hasNavigation boolean not null,
  hasHeatedSeats boolean not null
);
